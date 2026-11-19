# Importa os recursos do FastAPI para definição de rotas, códigos de status e exceções HTTP.
from fastapi import APIRouter, HTTPException, status
from schemas.estado_schema import EstadoInput, EstadoResponse
from services.estado_service import EstadoService

# Define o roteador para agrupar os endpoints relacionados à entidade Estado.
router = APIRouter(prefix="/estados", tags=["Estados"])

# Instancia a camada de serviço de Estado.
service = EstadoService()

# GET /estados - Lista todos os estados cadastrados.
@router.get("/", response_model=list[EstadoResponse], status_code=status.HTTP_200_OK)
def listar_estados():
    return service.listar_todos()

    # POST /estados - Cadastra um novo estado.
@router.post("/", response_model=EstadoResponse, status_code=status.HTTP_201_CREATED)
def criar_estado(dados: EstadoInput):
    novo_estado = service.criar(dados)
    if not novo_estado:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao salvar o estado no banco de dados.",
        )
    return novo_estado

    # PUT /estados/{estado_id} - Atualiza os dados de um estado existente.
@router.put("/{estado_id}", response_model=EstadoResponse, status_code=status.HTTP_200_OK)
def atualizar_estado(estado_id: int, dados: EstadoInput):
    estado_atualizado = service.atualizar(estado_id, dados)
    if not estado_atualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estado não encontrado para atualização.",
        )
    return estado_atualizado

    # DELETE /estados/{estado_id} - Remove um estado pelo ID.
@router.delete("/{estado_id}", status_code=status.HTTP_200_OK)
def excluir_estado(estado_id: int):
    sucesso = service.excluir(estado_id)
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estado não encontrado para exclusão.",
        )
    return {"mensagem": "Estado excluído com sucesso!"}