from main import chain
from fastapi import FastAPI
from langserve import add_routes


# Cria uma API pra ser consumida externamente.
app = FastAPI(
  title="Lux",
  version="1.0",
  description="Lux, seu amigo especialista em futebol.",
)

# Adiciona as rotas (aplicação (app), resposta para o usuário(chain) e o path (endpoint da aplicação)).
add_routes(
    app,
    chain,
    path="/lux",
)

# Informa onde a aplicação está rodando (neste projeto, localmente na porta 8000).
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)