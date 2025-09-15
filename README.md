# Lux - LLM Especialista em Futebol ⚽

## Descrição do Projeto:

Trata-se de um projeto que integra uma **IA LLM especializada em futebol, consumindo um modelo de linguagem avançado via API**, programada para responder exclusivamente a perguntas relacionadas a esse tema.

Caso o usuário faça uma pergunta fora do escopo de futebol, o assistente informa que não sabe responder, e orienta que o usuário consulte Guilherme Andrei Klabunde:

<img width="760" height="591" alt="Screenshot 2025-09-14 203517" src="https://github.com/user-attachments/assets/ca0aff70-c81b-47be-86bb-c4c5adb0c197" />

---
Exemplo de resposta a perguntas não relacionadas ao futebol:

<img width="740" height="508" alt="Screenshot 2025-09-14 203615" src="https://github.com/user-attachments/assets/f1be2a96-add9-45af-9264-3d7bafe8e790" />

## Estrutura do Projeto:

- **Groq - Llama3** 
    Este projeto utiliza o  'Groq - Llama3' para gerar as respostas ao usuário por não ser necessário o cadastro de um método de pagamento para sua utilização.
    Porém, o mesmo raciocínio de desenvolvimento e a estrutura base poderá ser reutilizada com pequenas alterações para outros modelos como "ChatGPT", "Gemini" e etc.

- **main.py**  
  Configura o prompt, o modelo de linguagem e a cadeia de execução (`chain`).

- **servidor.py**  
  Cria uma API com **FastAPI** e expõe o endpoint `/lux` para consumir o modelo.

## Tecnologias Utilizadas:

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)  
  - `langchain_core`  
  - `langchain_groq`  
  - `langserve`
- [Groq](https://groq.com/) (Modelo: `llama-3.3-70b-versatile`)
- [Uvicorn](https://www.uvicorn.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (Carregamento de variáveis de ambiente)
