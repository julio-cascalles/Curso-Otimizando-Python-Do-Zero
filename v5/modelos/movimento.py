from modelos import base
from modelos.mongo_table import MongoTable
from modelos.historico import Historico
from modelos.pessoa import Pessoa


class Movimento(base.Movimento, MongoTable):
    def save(self):
        pessoa = Pessoa.find(id=self.pessoa)[0]
        ultimo = Historico.ultimos(self.empresa)[-1]
        self.cotacao = ultimo.cotacao
        self.valida(
            historico=ultimo,
            pessoa=pessoa,
        )
        pessoa.capital -= (ultimo.cotacao * self.quantidade)
        pessoa.save()
        super().save()

    def valida(self, **args):
        pass

    @classmethod
    def total(cls, **args):
        class_list = cls.__subclasses__() + [cls]
        return sum(mov.quantidade
            for sub in class_list
            for mov in sub.find(**args)
        )
