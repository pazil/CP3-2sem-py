import pytest
#unittest.mock para simular o comportamento do mongodb
from unittest.mock import patch, MagicMock
from ex9 import excluir_aluno_por_nome

def test_excluir_aluno_sucesso(mocker):
    # Mock para find_one e delete_one
    mock_delete_result = MagicMock()
    mock_delete_result.deleted_count = 1

    mock_find_result = {"Nome": "João"}

    with patch("pymongo.MongoClient") as mock_client:
        mock_client_instance = MagicMock()
        mock_client_instance["alunos"]["alunos"].find_one.return_value = mock_find_result
        mock_client_instance["alunos"]["alunos"].delete_one.return_value = mock_delete_result
        mock_client.return_value = mock_client_instance

        # Mockando a função input para simular a entrada do usuário
        mocker.patch("builtins.input", return_value="João")

        # Chamar a função para testar
        excluir_aluno_por_nome("alunos", "alunos")

def test_excluir_aluno_nao_encontrado(mocker):
    # Mock para find_one que não encontra o aluno
    mock_find_result = None

    with patch("pymongo.MongoClient") as mock_client:
        mock_client_instance = MagicMock()
        mock_client_instance["alunos"]["alunos"].find_one.return_value = mock_find_result
        mock_client.return_value = mock_client_instance

        # Mockando a função input para simular várias tentativas de entrada do usuário
        mocker.patch("builtins.input", side_effect=["João", "Maria", "José"])

        # Chamar a função para testar
        excluir_aluno_por_nome("alunos", "alunos")

def test_excluir_aluno_erro(mocker):
    # Simulando erro ao conectar ao MongoDB
    with patch("pymongo.MongoClient", side_effect=Exception("Erro ao conectar")):
        # Mockando a função input
        mocker.patch("builtins.input", return_value="João")

        # Chamar a função para testar
        excluir_aluno_por_nome("alunos", "alunos")
