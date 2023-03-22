from fastapi import APIRouter, HTTPException
from modelos import base
from modelos.historico import Historico, ONTEM
from modelos.movimento import Movimento
from modelos.investimento import Investimento
from modelos.resgate import Resgate

router = APIRouter()


@router.post('/limpa_historico/{empresa}')
def limpa_historico(empresa: str):
    Historico.delete(empresa=empresa, id={'$ne':empresa})
    Investimento.delete(empresa=empresa)
    Resgate.delete(empresa=empresa)

@router.put('/investimento')
def faz_investimento(dados: base.Movimento):
    try:
        Investimento(**dados.__dict__).save()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.errors())

@router.put('/resgate')
def resgata(dados: base.Movimento):
    try:
        Resgate(**dados.__dict__).save()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.errors())

@router.post('/fecha_dia/{empresa}')
def fecha_dia(empresa: str):
    Historico.registra_variacao(
        empresa, Movimento.total(empresa=empresa,
        dia={'$gt': ONTEM})
    )
