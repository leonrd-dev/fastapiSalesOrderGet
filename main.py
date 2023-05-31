
from fastapi import FastAPI
from router import routering

app = FastAPI()
app.include_router(routering.RouterSO)


@app.get('/hello')
def index():
    return {'message': 'Hello, world'}


