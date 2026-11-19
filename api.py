# Importa o FastAPI e o servidor Uvicorn para execução da API.
from fastapi import FastAPI
import uvicorn
from routes.estado_routes import router as estado_router

# Inicializa a aplicação FastAPI com metadados para a documentação automática (Swagger / OpenAPI).
app = FastAPI(
    title="API de Endereços - CRUD de Estados",
    description="API REST desenvolvida com FastAPI e MySQL para gerenciamento de Estados.",
    version="1.0.0",
)

# Registra as rotas de Estado na aplicação principal.
app.include_router(estado_router)

# Rota raiz para verificação de status da API.
@app.get("/", tags=["Status"])
def raiz():
    return {
        "mensagem": "API de Estados em execução!",
        "documentacao": "Acesse /docs para visualizar o Swagger UI",
    }


# Ponto de partida da API ao executar diretamente o arquivo api.py.
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)