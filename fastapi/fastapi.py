from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from kubernetes import client, config
import json

app = FastAPI()

config.load_incluster_config()

api = client.CoreV1Api()

class Namespace(BaseModel):
    name: str

@app.get("/")
async def index():
    html_content = '''<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <form action="/delete" method="POST">
            <h2>Deletar namespace</h2>
            <label for="namespace">Nome do namespace</label>
            <input type="text" name="namespace" id="namespace" required>
            <input type="submit" value="Deletar">
        </form>

        <form action="/create" method="POST">
            <h2>Criar namespace</h2>
            <label for="namespace">Nome do namespace</label>
            <input type="text" name="namespace" id="namespace" required>
            <input type="submit" value="Criar">
        </form>
        <form action="/namespaces" method="GET">
        <label for="list">Lista de namespaces</label>
        <input type="submit" id="list" value="Listar namespaces">
        </form>
    </body>
    </html>'''
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/namespaces")
async def get_namespaces():
    namespaces = api.list_namespace()
    namespace_json = client.ApiClient().sanitize_for_serialization(namespaces)
    return JSONResponse(content=namespace_json, status_code=200)


@app.post("/delete")
async def delete_namespace(namespace: str = Form(...)):
    name = name = jsonable_encoder(namespace)
    api.delete_namespace(name=name)

    return f"O namespace {name} foi deletado com sucesso, acesse o endpoint /namespaces para verificar"


@app.post("/create")
async def create_namespace(namespace: str = Form(...)):
    name = jsonable_encoder(namespace)
    api.create_namespace(body=client.V1Namespace(
        metadata=client.V1ObjectMeta(name=name)))

    return f"O namespace {name} foi criado com sucesso, acesse o endpoint /namespaces para verificar"
