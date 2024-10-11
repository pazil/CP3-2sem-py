from pymongo import MongoClient

def consultar_documentos(nome_banco, nome_colecao):
    """
    Conecta ao MongoDB e consulta todos os documentos em uma coleção especificada.

    :param nome_banco: Nome do banco de dados no MongoDB.
    :param nome_colecao: Nome da coleção no MongoDB.
    :return: Lista de documentos encontrados ou None em caso de erro.
    """
    try:
        # Conectar ao MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client[nome_banco]
        colecao = db[nome_colecao]

        # Consultar todos os documentos na coleção
        documentos = list(colecao.find())
        
        # Exibir os documentos encontrados
        for documento in documentos:
            print(documento)
        
        return documentos

    except Exception as e:
        print("Erro ao consultar documentos no MongoDB:", e)
        return None

def main():
    """
    Função principal que solicita o nome do banco e da coleção e exibe os documentos encontrados.
    """
    # Solicitar o nome do banco de dados e da coleção ao usuário
    nome_banco = input("Digite o nome do banco de dados: ")
    nome_colecao = input("Digite o nome da coleção: ")

    # Consultar os documentos na coleção especificada
    documentos = consultar_documentos(nome_banco, nome_colecao)
    
    # Verificar se os documentos foram encontrados e exibir o resultado
    if documentos is not None:
        print(f"\nDocumentos encontrados na coleção '{nome_colecao}':")
        if documentos:
            for documento in documentos:
                print(documento)
        else:
            print("Nenhum documento encontrado.")
    else:
        print("Não foi possível consultar os documentos.")

# Executar a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
