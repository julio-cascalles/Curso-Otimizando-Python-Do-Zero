import pytest
from modelos.empresa import Empresa
from modelos.pessoa import Pessoa


def test_evolucao17():
    resultado = '{:.2f}'.format(
        Empresa.evolucao('17')
    )
    assert resultado == '1.00'

def test_evolucao45():
    resultado = '{:.2f}'.format(
        Empresa.evolucao('45')
    )
    assert resultado == '6.50'

def test_escolha():
    assert Pessoa.escolha(['17', '45']) == '45'
