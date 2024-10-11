import csv

def ler_arquivo_csv(caminho_arquivo):
    """
    Lê um arquivo CSV e retorna as linhas lidas.

    :param caminho_arquivo: Caminho para o arquivo CSV.
    :return: Lista de linhas lidas do arquivo ou None em caso de erro.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            linhas = [linha for linha in leitor_csv]
            return linhas
    except Exception as e:
        print("Erro ao ler o arquivo CSV:", e)
        return None
