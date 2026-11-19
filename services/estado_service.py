# Importa a classe Estado da camada de persistência e o schema de entrada.
from estado import Estado
from schemas.estado_schema import EstadoInput


# Classe responsável pelas regras de negócio e intermediação entre as rotas da API e o banco de dados.
class EstadoService:

# Retorna a lista de todos os estados cadastrados.
    def listar_todos(self):
        estado = Estado()
        return estado.listar()

def buscar_por_id(self, estado_id: int):
        estado = Estado()
        estado.id = estado_id
        return estado.buscar_por_id()

# Cria um novo estado no banco de dados e retorna os dados criados.
def criar(self, dados: EstadoInput):
        estado = Estado()
        estado.nome = dados.nome.strip()
        estado.sigla = dados.sigla.strip().upper()

        if estado.salvar():
            return {
                "id": estado.id,
                "nome": estado.nome,
                "sigla": estado.sigla,
            }
        return None

# Atualiza os dados de um estado existente pelo ID.
def atualizar(self, estado_id: int, dados: EstadoInput):
        estado = Estado()
        estado.id = estado_id

        # Verifica se o estado existe antes de atualizar.
        if not estado.buscar_por_id():
            return None

        estado.nome = dados.nome.strip()
        estado.sigla = dados.sigla.strip().upper()
        estado.atualizar()

        return {
            "id": estado.id,
            "nome": estado.nome,
            "sigla": estado.sigla,
        }

# Exclui um estado do banco de dados pelo ID.
def excluir(self, estado_id: int):
        estado = Estado()
        estado.id = estado_id
        return estado.excluir()