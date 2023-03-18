from datetime import datetime, timedelta
from modelos import base
from modelos.mongo_table import MongoTable

HOJE = datetime.today()
ONTEM = HOJE - timedelta(days=1)


class Historico(base.Historico, MongoTable):

    @classmethod
    def ultimos(cls, empresa: str) -> list:
        return cls.find(
            empresa=empresa,
            dia={'$gte': HOJE - timedelta(days=10)}
        )

    @staticmethod
    def registra_variacao(empresa: str, total: int, dt_ref=HOJE):
        ultimo = Historico.ultimos(empresa)[-1]
        tendencia = total / 1000
        Historico(
            empresa=empresa, dia=dt_ref,
            cotacao=ultimo.cotacao + tendencia
        ).save()
