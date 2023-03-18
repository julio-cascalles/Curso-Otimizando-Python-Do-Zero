import pytest
from modelos.mongo_table import MongoTable
from modelos.empresa import Empresa

ID_EMPRESA_TESTE = '00000'

@pytest.mark.skip(reason='Carregando dados de teste')
def grava_dados():
    MongoTable.DATABASE_NAME = 'teste'
    Empresa(
        id=ID_EMPRESA_TESTE,
        nome='Companhia ABC',
        capital=123_456,
        cotas=7890,
    ).save()

grava_dados()


def test_capital_empresa():
    dados = Empresa.find(id=ID_EMPRESA_TESTE)[0]
    assert dados.capital == 123_456

def test_cotas_empresa():
    dados = Empresa.find(id=ID_EMPRESA_TESTE)[0]
    assert dados.cotas == 7890
