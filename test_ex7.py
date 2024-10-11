import pytest
#unittest.mock para simular o comportamento do mongodb

from unittest.mock import patch, MagicMock
from ex7 import listar_bancos_de_dados

def test_listar_bancos_de_dados():
    # Mockando o método list_database_names para simular bancos de dados disponíveis
    with patch("pymongo.MongoClient") as mock_client:
        mock_client_instance = MagicMock()
        mock_client_instance.list_database_names.return_value = ["admin", "local", "alunos"]
        mock_client.return_value = mock_client_instance

        resultado = listar_bancos_de_dados()
        assert set(resultado) == {"admin", "local", "alunos"}  # Verifica a presença dos itens, independente da ordem


def test_listar_bancos_de_dados_erro():
    # Simulando um erro ao conectar com o MongoDB
    with patch("pymongo.MongoClient", side_effect=Exception("Erro de conexão")):
        resultado = listar_bancos_de_dados()
        assert resultado is None

