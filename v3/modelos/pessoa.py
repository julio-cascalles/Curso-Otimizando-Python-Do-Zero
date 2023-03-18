from modelos import base
from modelos.mongo_table import MongoTable
from modelos.historico import Historico, ONTEM


class Pessoa(base.Pessoa, MongoTable):
    pass
