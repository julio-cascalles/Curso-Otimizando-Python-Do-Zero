from fastapi import FastAPI
from rotas  import movimento, pessoa


def create_app():
    app = FastAPI()
    app.include_router(movimento.router)
    app.include_router(pessoa.router)
    return app
