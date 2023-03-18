from modelos import base
from modelos.mongo_table import MongoTable
from modelos.empresa import Empresa


class Pessoa(base.Pessoa, MongoTable):

    @staticmethod
    def escolha(sugestoes: list) -> str:
        """
        Retorna qual empresa é melhor para
        investir, baseado na evolução delas:
        """
        resumo = {
            Empresa.evolucao(ref): ref
            for ref in sugestoes
        }
        melhor = max(resumo.keys())
        return resumo[melhor]
