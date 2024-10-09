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

# Caminho do arquivo JSON
caminho_arquivo = input("Digite o nome do arquivo JSON que deseja ler: ")

# Leitura do arquivo
dados = ler_arquivo_json(caminho_arquivo)

# Exibição dos dados lidos
if dados is not None:
    print("Conteúdo do arquivo JSON:")
    print(dados)
else:
    print("Não foi possível ler o arquivo JSON.")
