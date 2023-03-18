import uvicorn
from modelos.mongo_table import MongoTable
from rotas.app import create_app


MongoTable.DATABASE_NAME = 'teste' #  'bolsa-valores'

uvicorn.run(
    create_app()
)
