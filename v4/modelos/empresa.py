from csv import DictReader
from modelos import base
from modelos.mongo_table import MongoTable
from modelos.historico import Historico


class Empresa(base.Empresa, MongoTable):
    def save(self):
        if not Historico.find(empresa=self.id):
            Historico(
                id=self.id, empresa=self.id,
                cotacao=self.capital/self.cotas
            ).save()
        super().save()

    @classmethod
    def importa(cls, arquivo: str):
        with open(arquivo, 'r', encoding='utf-8') as f:
            for dados in DictReader(f):
                dados['capital']=float(dados['capital'])
                Empresa(**dados).save()

    @staticmethod
    def evolucao(empresa: str) -> float:
        # dados = Historico.ultimos(empresa=empresa)
        TEMPORARIO = {
            '17': [
                Historico(empresa='17', cotacao=18.00),
                Historico(empresa='17', cotacao=19.00),
            ],
            '45': [
                Historico(empresa='45', cotacao=13.50),
                Historico(empresa='45', cotacao=20.00),
            ]
        }
        # ----------------------------------------
        dados = TEMPORARIO[empresa]
        return sum(
            (prox.cotacao - ant.cotacao) * i
            for i, (ant, prox) in enumerate(
                zip(dados, dados[1:]), start=1
            )
        )
