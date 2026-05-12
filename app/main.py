from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello Luca!", "v": "0.1"}


@app.get("/api/ip")
def get_ip(request: Request):
    return {"ip": request.client.host}


@app.get("/ip", response_class=HTMLResponse)
def ip_page(request: Request):
    return f"<h1>Din publika IP-address är {request.client.host}</h1>"