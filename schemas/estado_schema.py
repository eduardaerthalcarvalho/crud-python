# Importa o BaseModel e o Field do Pydantic para validação e serialização de dados.
from pydantic import BaseModel, Field


# Schema para entrada de dados (criação e atualização de um Estado).
class EstadoInput(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, examples=["Santa Catarina"])
    sigla: str = Field(..., min_length=2, max_length=2, examples=["SC"])


# Schema para saída de dados (resposta da API contendo o ID do banco de dados).
class EstadoResponse(EstadoInput):
    id: int = Field(..., examples=[1])