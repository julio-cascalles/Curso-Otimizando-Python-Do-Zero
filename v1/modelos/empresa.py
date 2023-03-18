from modelos import base
from modelos.mongo_table import MongoTable


class Empresa(base.Empresa, MongoTable):
    pass
