from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from kubernetes import client, config

app = FastAPI()

@app.get("/")
async def get_namespaces():

    html_content = '''
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
        html_content += f"<li>{namespace.metadata.name}</li>"   

    html_content += ''' 
        </ul>
        </body>
        </html>
        '''   
    return HTMLResponse(content=html_content, status_code=200)
