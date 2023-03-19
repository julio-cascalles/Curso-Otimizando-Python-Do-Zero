from pydantic import BaseModel, validator
from datetime import datetime


class Pessoa(BaseModel):
    id: str
    nome: str
    capital: float


class Empresa(Pessoa):
    cotas: int = 100_000


class Historico(BaseModel):
    id: str = ''
    empresa: str
    dia: datetime = datetime.today()
    cotacao: float = 0.00


class Movimento(Historico):
    pessoa: str
    quantidade: int  # Quantas ações compradas ou vendidas

    @validator('quantidade')
    def valida_diferente_de_zero(qtd: int):
        if qtd == 0:
            raise ValueError('A quantidade não pode ser zero.')
        return qtd
