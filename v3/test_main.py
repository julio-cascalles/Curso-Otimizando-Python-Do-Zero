import pytest
from modelos.mongo_table import MongoTable
from modelos.pessoa import Pessoa
from modelos.movimento import Movimento
from modelos.investimento import Investimento
from modelos.resgate import Resgate
from modelos.historico import Historico, ONTEM

BRUNO, YARA, DARIO, LEILA = [
    Pessoa(id='175.948.602-76', nome='Bruno', capital=1000),
    Pessoa(id='630.598.241-42', nome='Yara', capital=1000),
    Pessoa(id='258.764.310-44', nome='Dario', capital=1000),
    Pessoa(id='431.076.895-48', nome='Leila', capital=1000),
]


@pytest.mark.skip(reason='Carregando dados de teste')
def grava_dados():
    MongoTable.DATABASE_NAME = 'teste'
    # --- Limpa o histórico de testes anteriores: ---
    Historico.delete(empresa='6', id={'$ne':'6'})
    Investimento.delete(empresa='6')
    Resgate.delete(empresa='6')
    # -----------------------------------------------
    for pessoa in [BRUNO, YARA, DARIO, LEILA]:
        pessoa.save()
        for _ in range(2):
            Investimento(pessoa=pessoa.id, empresa='6', quantidade=30).save()
    Resgate(pessoa=BRUNO.id, empresa='6', quantidade=10).save()
    Resgate(pessoa=LEILA.id, empresa='6', quantidade=10).save()
    Historico.registra_variacao(
        '6', Movimento.total(empresa='6',
        dia={'$gt': ONTEM})
    )

grava_dados()


def test_valorizacao():
    atual = Historico.find(empresa='6')[-1]
    resultado = '{:.2f}'.format(atual.cotacao)
    assert resultado == '12.59'

def test_saldo_bruno():
    bruno = Pessoa.find(id=BRUNO.id)[0]
    resultado = '{:.1f}'.format(bruno.capital)
    assert resultado == '381.5'  # (1000-50*12.37)

def test_lucro_yara():
    Resgate(pessoa=YARA.id, empresa='6', quantidade=60).save()
    yara = Pessoa.find(id=YARA.id)[0]
    assert yara.capital > 1000

def test_erro_saque():
    try:
        Resgate(pessoa=DARIO.id, emrpesa='6', quantidade=100).save()
        com_erro = False
    except:
        com_erro = True
    assert com_erro
