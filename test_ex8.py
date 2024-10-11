import pytest
#unittest.mock para simular o comportamento do mongodb
from unittest.mock import patch, MagicMock
from ex8 import consultar_documentos

def test_consultar_documentos():
    # Mockando a função find para simular o retorno de documentos
    mock_data = [{"Nome": "João"}, {"Nome": "Maria"}]
    with patch("pymongo.MongoClient") as mock_client:
        mock_client_instance = MagicMock()
        mock_client_instance["alunos"]["alunos"].find.return_value = mock_data
        mock_client.return_value = mock_client_instance

        resultado = consultar_documentos("alunos", "alunos")
        assert resultado == mock_data

def test_consultar_documentos_erro():
    # Simulando um erro ao conectar com o MongoDB
    with patch("pymongo.MongoClient", side_effect=Exception("Erro de conexão")):
        resultado = consultar_documentos("alunos", "alunos")
        assert resultado is None
