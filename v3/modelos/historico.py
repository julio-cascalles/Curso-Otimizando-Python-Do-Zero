from datetime import datetime, timedelta
from modelos import base
from modelos.mongo_table import MongoTable

ONTEM = datetime.today() - timedelta(days=1)


class Historico(base.Historico, MongoTable):

    @classmethod
    def ultimos(cls, empresa: str) -> list:
        return cls.find(
            empresa=empresa,
            dia={'$gte': datetime.today() - timedelta(days=10)}
        )

    @staticmethod
    def registra_variacao(empresa: str, total: int):
        ultimo = Historico.ultimos(empresa)[-1]
        tendencia = total / 1000
        Historico(
            empresa=empresa,
            cotacao=ultimo.cotacao + tendencia
        ).save()
