from modelos import base
from modelos.mongo_table import MongoTable


class Pessoa(base.Pessoa, MongoTable):
    pass
