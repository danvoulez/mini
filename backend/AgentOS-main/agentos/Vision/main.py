from fastapi import FastAPI
from vision.routes import network

app = FastAPI()
app.include_router(network.router)


@app.get('/status')
def status():
    return {'status': 'Vision online'}
