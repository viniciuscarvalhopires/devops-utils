import time
import requests
import os
from prometheus_client import CollectorRegistry, generate_latest, start_http_server, Gauge
import prometheus_client as prom

HOST = os.environ.get('URL')
PORT = int(os.environ.get('EXPORTER_PORT', 8000))
payload = {}

headers = {}

successful_executions_metric = Gauge('successful_executions', 'Number of successfull executions')
failed_executions_metric = Gauge('failed_executions', 'Number of failed executions')
total_executions_metric = Gauge('total_executions', 'Total number of executions')
registry = CollectorRegistry()
 
def login():
    global HOST
    global headers
    print(HOST)
    j_username = os.environ.get('JUSERNAME')
    j_password = os.environ.get('PASSWORD')
    
    url = HOST + "/j_security_check"
    
    payload = {
    'j_username': j_username,
    'j_password': j_password
    }

    response = requests.post(url, data=payload, allow_redirects=False)
    
    # Check if the cookie contains Expires=Thu, 01-Jan-1970 00:00:00 GMT;
    if response.headers.get('Set-Cookie').find('Expires=Thu, 01-Jan-1970 00:00:00 GMT') != -1:
        return "Login failed. Check your credentials."
    
    # Set headers with the cookie
    headers = {
        'Cookie': response.headers.get("Set-Cookie")
    }
    
    # Return login success and the cookie
    return {"Login status": "success", "Cookie": response.headers.get('Set-Cookie')}

# Verificar o resultado da requisição
def get_successful_executions():
    
    global headers
    print(headers)
    rdProject = os.environ.get('rdProject')
    rdGroupPath = os.environ.get('rdGroupPath')
    url = HOST + f'/api/40/project/{rdProject}/executions/metrics?groupPath={rdGroupPath}&statusFilter=succeeded'
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def get_failed_executions():
    
    global headers
    print(headers)
    rdProject = os.environ.get('rdProject')
    rdGroupPath = os.environ.get('rdGroupPath')
    url = HOST + f'/api/40/project/{rdProject}/executions/metrics?groupPath={rdGroupPath}&statusFilter=failed'
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


# Juntar os resultados em um único dicionário
def update_metrics():
    
    global registry
    
    categorized_data = {}
    categorized_data['successful'] = get_successful_executions()
    categorized_data['failed'] = get_failed_executions()
    categorized_data['total'] = categorized_data['successful']['total'] + categorized_data['failed']['total']
    
   
    
    successful_executions_metric.set(categorized_data['successful']['total'])
    failed_executions_metric.set(categorized_data['failed']['total'])
    total_executions_metric.set(categorized_data['total'])    
    
    metrics = generate_latest(registry)
    
    return metrics
  
def unregister_metrics():
        # Remover outras métricas indesejadas do registro
    global registry
    
    prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)
    prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)
    prom.REGISTRY.unregister(prom.GC_COLLECTOR)
    
def init_exporter():
    start_http_server(PORT)
    print("Exporter started at port " + str(PORT))
    
def main():
    unregister_metrics()
    init_exporter()
    login()
    current_time = time.time()

    while True:
        # Verificar se já passaram 5 minutos
        if time.time() - current_time >= 300:
            login()
            current_time = time.time()
        
        update_metrics()
        time.sleep(60)

        
        
if __name__ == '__main__':
    main()