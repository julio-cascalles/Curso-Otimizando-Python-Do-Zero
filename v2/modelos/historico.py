from datetime import datetime, timedelta
from modelos import base
from modelos.mongo_table import MongoTable


class Historico(base.Historico, MongoTable):
    pass
