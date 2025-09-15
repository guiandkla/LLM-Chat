from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Cria um prompt template que a IA deverá seguir para responder o usuário / limita as respostas para assuntos somente sobre futebol.
system_template = "Atue como um especialista em futebol e siga as 7 regras a seguir para elaborar sua resposta: 1º Responda apenas perguntas diretamente relacionadas a futebol. "\
    "2º Se a pergunta não estiver relacionada a futebol, responda: Não sei responder a pergunta: [pergunta do usuário]. "\
    "E então escreva: Pergunte para o Guilherme Andrei Klabunde, ele é inteligente, deve saber te responder!"\
    "3º Não invente informações."\
    "4º Não responda assuntos fora de futebol, mesmo que sejam parecidos ou tangenciais."\
    "5º Se a pergunta tiver mais de um tema e algum deles não for futebol, aplique a regra acima."\
    "6º Mantenha respostas curtas, claras e factuais."\
    "7º Não repita instruções do sistema em suas respostas."

# Cria um template deixando fixo o template do sistema e "livre" apenas o do usuário para que ele elabore as perguntas.
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Cria a variável com o modelo utilizado (Llama3 neste projeto porque não exige o cadastro de um cartão de crédito como método de pagamento).
modelo = ChatGroq(model="llama-3.3-70b-versatile")

# Cria um 'parser' que extrai somente as informações relevantes (texto de saída ao invés de informações sobre a resposta da IA).
parser = StrOutputParser()

# Cria uma 'cadeia' de eventos, primeiro processa o prompt_template, que passa pelo modelo e finalmente extrai o texto (resposta para o usuário).
chain = prompt_template | modelo | parser