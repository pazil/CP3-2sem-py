import pytest
from unittest.mock import mock_open, patch
from ex3 import ler_arquivo_csv

def test_ler_arquivo_csv_valido():
    # Simulando dados de um arquivo CSV válido
    dados_csv = "nome,idade\nJoão,30\nMaria,25\n"

    # Mockando a função open para simular a leitura de um arquivo CSV
    with patch("builtins.open", mock_open(read_data=dados_csv)):
        resultado = ler_arquivo_csv("dados.csv")
        assert resultado == [["nome", "idade"], ["João", "30"], ["Maria", "25"]]

def test_ler_arquivo_csv_arquivo_nao_encontrado():
    # Simulando erro de arquivo não encontrado
    with patch("builtins.open", side_effect=FileNotFoundError):
        resultado = ler_arquivo_csv("arquivo_inexistente.csv")
        assert resultado is None

def test_ler_arquivo_csv_erro_generico():
    # Simulando um erro genérico ao abrir o arquivo
    with patch("builtins.open", side_effect=Exception("Erro desconhecido")):
        resultado = ler_arquivo_csv("dados.csv")
        assert resultado is None
