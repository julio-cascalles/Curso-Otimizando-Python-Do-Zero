from pydantic import BaseModel
from datetime import datetime, timedelta


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
    cotacao: float
