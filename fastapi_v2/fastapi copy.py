from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from kubernetes import client, config
import json

app = FastAPI()

# config.load_incluster_config()
config.load_kube_config(config_file="/home/vinicius/.kube/lab.yaml")

api = client.CoreV1Api()

templates = Jinja2Templates(directory="/app/templates/jinja")

@app.get("/css")
async def get_css():
    return FileResponse("/app/templates/assets/index-style.css", media_type="text/css")

@app.get("/namespaces-css")
async def get_css():
    return FileResponse("/app/templates/assets/namespaces-css.css", media_type="text/css")

@app.get("/")
async def index():
    return FileResponse("/app/templates/static/index.html")
    

@app.get("/namespaces-json")
async def get_namespaces_json():
    namespaces = api.list_namespace()
    namespace_json = client.ApiClient().sanitize_for_serialization(namespaces)
    return JSONResponse(content=namespace_json, status_code=200)

@app.get("/namespaces")
async def get_namespaces(request: Request):
    namespaces = api.list_namespace().items

    return templates.TemplateResponse("namespaces.html", {"request": request, "namespaces": namespaces})

@app.post("/delete")
async def delete_namespace(request: Request, namespace: str = Form(...)):
    name = jsonable_encoder(namespace)
    api.delete_namespace(name=name)
    return templates.TemplateResponse("response.html", {"request": request, "namespace": namespace, "action": "deletado"})

@app.post("/create")
async def create_namespace(request: Request,namespace: str = Form(...)):
    name = jsonable_encoder(namespace)
    api.create_namespace(body=client.V1Namespace(
    metadata=client.V1ObjectMeta(name=name)))

    return templates.TemplateResponse("response.html", {"request": request, "namespace": namespace, "action": "criado"})

