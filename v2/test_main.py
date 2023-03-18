import os
import pytest
from modelos.mongo_table import MongoTable
from modelos.empresa import Empresa
from modelos.historico import Historico


@pytest.mark.skip(reason='Carregando dados de teste')
def grava_dados():
    MongoTable.DATABASE_NAME = 'teste'
    arquivo = os.path.join(
        os.path.split(__file__)[0],
        'dados/ranking.csv'
    )
    Empresa.importa(arquivo)


grava_dados()


def test_historico():
    dados = Historico.find(empresa='6')
    assert dados[0].cotacao == 12.37

def test_soma_capital():
    soma = sum(e.capital for e in Empresa.find())
    assert soma == 130_023_456
