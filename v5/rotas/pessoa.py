from fastapi import APIRouter, HTTPException
from modelos import base
from modelos.pessoa import Pessoa

router = APIRouter()


@router.get('/melhor_escolha')
def melhor_escolha(primeira: str, segunda: str):
    """
    Devolve qual empresa é melhor para
    investir entre dois id´s de empresas

    Sintaxe: http://.../melhor_escolha?primeira=123,segunda=456
    """
    return Pessoa.escolha([primeira, segunda])


@router.put('/grava_pessoa')
def grava_pessoa(dados: base.Pessoa):
    try:
        Pessoa(**dados.__dict__).save()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e.errors())
