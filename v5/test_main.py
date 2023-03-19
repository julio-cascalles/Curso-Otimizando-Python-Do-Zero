import pytest
from fastapi.testclient import TestClient
from rotas.app import create_app
from modelos.mongo_table import MongoTable
from testes.pessoa import grava_grupo, melhor_escolha
from testes.movimento import investe33, resgata_tudo


client = TestClient(
    create_app()
)
MongoTable.DATABASE_NAME = 'teste'


@pytest.mark.order(1) # pip install pytest-order !!!!
def test_cria_pessoas():
    assert grava_grupo(client)

@pytest.mark.order(2)
def test_investimentos():    
    assert investe33(client)

@pytest.mark.order(3)
def test_resgates():
    assert resgata_tudo(client)

@pytest.mark.order(4)
def test_escolha():
    assert melhor_escolha(client) == '6'
