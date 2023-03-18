from modelos.historico import HOJE, ONTEM
from testes.const import LISTA_CPF


def investe33(client) -> bool:
    client.post('/limpa_historico/33')
    for cpf in LISTA_CPF:
        resp = client.put(
            '/investimento',
            json=dict(
                pessoa=cpf, empresa='33',
                quantidade=30, dia=ONTEM.isoformat()
            )
        )
        if resp.status_code not in [200, 201]:
            return False
    return True

def resgata_tudo(client) -> bool:
    for cpf in LISTA_CPF:
        resp = client.put(
            '/resgate',
            json=dict(
                pessoa=cpf, empresa='33',
                quantidade=30, dia=HOJE.isoformat()
            )
        )
        if resp.status_code != 200:
            return False
    client.post('/fecha_dia/33')
    return True
