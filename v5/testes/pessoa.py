from modelos import base
from modelos.pessoa import Pessoa
from testes.const import LISTA_CPF, NOMES


def melhor_escolha(client):
    resp = client.get('/melhor_escolha?primeira=6&segunda=33')
    return resp.content.decode("utf-8").replace('"', '')

def grava_grupo(client) -> bool:
    Pessoa.delete()
    for cpf, nome in zip(LISTA_CPF, NOMES):
        dados = base.Pessoa(id=cpf, nome=nome, capital=1000)
        resp = client.put(
            '/grava_pessoa',
            json=dados.dict()
        )
        if resp.status_code not in [200, 201]:
            return False
    return True
