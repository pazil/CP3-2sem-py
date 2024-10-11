from pymongo import MongoClient

def excluir_aluno_por_nome(nome_banco, nome_colecao):
    """
    Conecta ao MongoDB, exibe os documentos da coleção e remove um aluno pelo nome.

    :param nome_banco: Nome do banco de dados no MongoDB.
    :param nome_colecao: Nome da coleção no MongoDB.
    """
    try:
        # Conectar ao MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client[nome_banco]
        colecao = db[nome_colecao]

        # Exibir todos os documentos na coleção para ver como os dados estão armazenados
        print(f"Documentos na coleção '{nome_colecao}':")
        documentos = colecao.find()
        for documento in documentos:
            print(documento)

        # Solicitar o nome do aluno até que seja encontrado na coleção
        while True:
            nome_aluno = input("\nDigite o nome do aluno: ")

            # Verificar se o aluno existe na coleção (usando expressão regular para ignorar maiúsculas/minúsculas)
            aluno_existe = colecao.find_one({"Nome": {"$regex": f"^{nome_aluno}$", "$options": "i"}})

            if aluno_existe:
                break
            else:
                print(f"O aluno '{nome_aluno}' não foi encontrado. Por favor, tente novamente.")

        # Remover o documento que corresponde ao nome do aluno
        resultado = colecao.delete_one({"Nome": {"$regex": f"^{nome_aluno}$", "$options": "i"}})

        if resultado.deleted_count > 0:
            print(f"Documento do aluno '{nome_aluno}' excluído com sucesso.")
        else:
            print(f"Nenhum documento encontrado para o aluno '{nome_aluno}'.")

    except Exception as e:
        print("Erro ao excluir o documento no MongoDB:", e)

def main():
    """
    Função principal que solicita o nome do banco de dados e da coleção, e chama a função para excluir um aluno.
    """
    # Solicitar o nome do banco de dados e da coleção ao usuário
    nome_banco = input("Digite o nome do banco de dados: ")
    nome_colecao = input("Digite o nome da coleção: ")

    # Chamar a função para excluir um aluno pelo nome
    excluir_aluno_por_nome(nome_banco, nome_colecao)

# Executar a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
