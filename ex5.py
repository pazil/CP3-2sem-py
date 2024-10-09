import json 
alunos = {
    "João": 8.5,
    "Maria": 9.0,
    "Pedro": 7.5,
    "Ana": 8.0,
    "Lucas": 9.2
}

# Função para ler um arquivo JSON
def escrever_arquivo_json(dados, caminho_arquivo):
    try:
        with open(f"{caminho_arquivo}.json", 'w', encoding='utf-8') as arquivo_json:
            dados = json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        return dados
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro: O arquivo não é um JSON válido.")
        return None

escrever_arquivo_json(alunos, "alunos")