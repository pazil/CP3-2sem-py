import pytest
import json
from unittest.mock import mock_open, patch
from ex4 import ler_arquivo_json

def test_ler_arquivo_json_valido():
    # Simulando dados JSON válidos
    dados_json = '{"nome": "João", "idade": 30}'

    with patch("builtins.open", mock_open(read_data=dados_json)):
        dados = ler_arquivo_json("arquivo_valido")
        assert dados == {"nome": "João", "idade": 30}

def test_ler_arquivo_json_invalido():
    # Simulando dados JSON inválidos
    dados_json_invalido = '{"nome": "João", "idade": 30'

    with patch("builtins.open", mock_open(read_data=dados_json_invalido)):
        dados = ler_arquivo_json("arquivo_invalido")
        assert dados is None

def test_ler_arquivo_json_nao_encontrado():
    # Simulando erro de arquivo não encontrado
    with patch("builtins.open", side_effect=FileNotFoundError):
        dados = ler_arquivo_json("arquivo_nao_existente")
        assert dados is None
