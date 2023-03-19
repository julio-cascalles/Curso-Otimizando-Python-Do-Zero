from pydantic import BaseModel
from datetime import datetime


class Pessoa(BaseModel):
    id: str
    nome: str
    saldo: float


class Empresa(BaseModel):
    id: str
    nome: str
    capital: float
    cotas: int = 100_000


class Historico(BaseModel):
    id: str = ''
    empresa: str
    dia: datetime = datetime.today()
    cotacao: float