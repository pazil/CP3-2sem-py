import csv

# Função para ler o arquivo CSV
def ler_csv(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
        return None

# Função para salvar os dados atualizados no arquivo CSV
def salvar_csv(caminho_arquivo, dados):
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(dados)
    print("Arquivo atualizado com sucesso.")

# Caminho do arquivo CSV
caminho_arquivo = 'nomes_e_idades.csv'

# Loop principal
while True:
    dados = ler_csv(caminho_arquivo)

    if dados:
        # Exibindo os dados atuais
        print("Dados atuais:")
        for linha in dados:
            print(linha)
    else:
        print("Não foi possível ler o arquivo.")
        break

    nome_para_atualizar = input("\nDigite o nome da pessoa cuja idade deseja atualizar (ou 'sair' para encerrar): ")
    if nome_para_atualizar.lower() == 'sair':
        break

    # Verificando se o nome existe na lista
    nome_encontrado = False
    for linha in dados:
        if linha[0].lower() == nome_para_atualizar.lower():
            nome_encontrado = True
            break

    if not nome_encontrado:
        print("Nome não encontrado. Tente novamente.")
        continue

    nova_idade = input("Digite a nova idade: ")

    # Verificando se a idade é um número válido
    if not nova_idade.isdigit():
        print("Erro: Por favor, insira um número válido para a idade.")
        continue

    # Atualizando a idade no arquivo
    for linha in dados:
        if linha[0].lower() == nome_para_atualizar.lower():
            linha[1] = nova_idade
            break

    salvar_csv(caminho_arquivo, dados)
