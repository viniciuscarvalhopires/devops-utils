from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from kubernetes import client, config
import json

app = FastAPI()

# config.load_incluster_config()

# api = client.CoreV1Api()

templates = Jinja2Templates(directory="/app/templates/jinja")

@app.get("/")
async def index():
    return FileResponse("/app/templates/static/index.html")
    

@app.get("/namespaces-json")
async def get_namespaces_json():
    namespaces = api.list_namespace()
    namespace_json = client.ApiClient().sanitize_for_serialization(namespaces)
    return JSONResponse(content=namespace_json, status_code=200)

@app.get("/namespaces")
async def get_namespaces():
    namespaces = api.list_namespace().items

    return HTMLResponse(content=html_content, status_code=200)

@app.post("/delete")
async def delete_namespace(namespace: str = Form(...)):
    name = jsonable_encoder(namespace)
    api.delete_namespace(name=name)

    return f"O namespace {name} foi deletado com sucesso, acesse o endpoint /namespaces para verificar"


@app.post("/create")
async def create_namespace(namespace: str = Form(...)):
    name = jsonable_encoder(namespace)
    api.create_namespace(body=client.V1Namespace(
    metadata=client.V1ObjectMeta(name=name)))

    return f"O namespace {name} foi criado com sucesso, acesse o endpoint /namespaces para verificar"
