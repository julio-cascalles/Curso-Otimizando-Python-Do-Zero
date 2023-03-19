from pydantic import BaseModel
from datetime import datetime


class Pessoa(BaseModel):
    id: str  # CPF ou auto-incremento...
    nome: str
    saldo: float


class Empresa(BaseModel):
    id: str # CNPJ ou auto-incremento...
    nome: str
    capital: float
    cotas: int = 100_000


class Historico(BaseModel):
    id: str = '' # Gerado automaticamente
    empresa: str
    dia: datetime = datetime.today()
    cotacao: float