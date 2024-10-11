import json

# Função para ler um arquivo JSON
def ler_arquivo_json(caminho_arquivo):
    try:
        with open(f"{caminho_arquivo}.json", 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
        return dados
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro: O arquivo não é um JSON válido.")
        return None

# Função principal que interage com o usuário
def main():
    # Caminho do arquivo JSON fornecido pelo usuário
    caminho_arquivo = input("Digite o nome do arquivo JSON que deseja ler: ")

    # Leitura do arquivo
    dados = ler_arquivo_json(caminho_arquivo)

    # Exibição dos dados lidos
    if dados is not None:
        print("Conteúdo do arquivo JSON:")
        print(dados)
    else:
        print("Não foi possível ler o arquivo JSON.")

# Executa a função principal somente se o script for executado diretamente
if __name__ == "__main__":
    main()
