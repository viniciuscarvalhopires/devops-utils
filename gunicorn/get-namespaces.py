from kubernetes import client, config

def app(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
    ]
    response_body = b'''
        <html>
        <head><meta http-equiv="refresh" content="3"></head>
        <body>
        <h2>Desafio com script python</h2>
        <ul>
        '''

    # Estabelece a conexão com o cluster
    config.load_incluster_config()
    api = client.CoreV1Api()
    namespaces = api.list_namespace().items
    for namespace in namespaces:
        response_body += f"<li>{namespace.metadata.name}</li>".encode("utf-8")
    response_body += b''' 
        </ul>
        </body>
        </html>
        '''      
    start_response(status, response_headers)
    return [response_body]; 

