from pymongo import MongoClient

def listar_bancos_de_dados():
    """
    Conecta ao MongoDB e lista os bancos de dados disponíveis.

    :return: Lista de nomes dos bancos de dados disponíveis ou None em caso de erro.
    """
    try:
        # Conectar ao MongoDB
        client = MongoClient("mongodb://localhost:27017/")

        # Listar os bancos de dados disponíveis
        databases = client.list_database_names()
        print("Bancos de dados disponíveis:", databases)
        return databases

    except Exception as e:
        print("Erro ao conectar ao MongoDB:", e)
        return None

def main():
    """
    Função principal que chama listar_bancos_de_dados e exibe os resultados.
    """
    # Chamar a função para listar os bancos de dados
    bancos = listar_bancos_de_dados()
    
    # Verificar se o retorno não é None e exibir os bancos de dados
    if bancos is not None:
        print("Os bancos de dados disponíveis são:")
        for banco in bancos:
            print(f"- {banco}")
    else:
        print("Não foi possível listar os bancos de dados.")

# Executar a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
