from pymongo import MongoClient

try:
    # Solicitar ao usuário o URI de conexão e o nome do banco de dados
    uri = "mongodb://localhost:27017/"
    nome_banco = "alunos"

    # Conectar ao MongoDB
    client = MongoClient(uri)
    db = client[nome_banco]
    colecao = db["alunos"]

    # Dados dos alunos
    dados_alunos = [
        {"Nome": "João", "Idade": 25, "Cidade": "São Paulo"},
        {"Nome": "Maria", "Idade": 30, "Cidade": "Rio de Janeiro"},
        {"Nome": "Ana", "Idade": 22, "Cidade": "Belo Horizonte"}
    ]

    # Inserir os dados na coleção "alunos"
    resultado = colecao.insert_many(dados_alunos)
    
    # Exibir o resultado da inserção
    print(f"{len(resultado.inserted_ids)} documentos inseridos na coleção 'alunos'.")

except Exception as e:
    print("Erro ao criar o banco de dados ou inserir documentos no MongoDB:", e)
