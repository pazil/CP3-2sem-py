import json 
import os
import pytest
from ex5 import escrever_arquivo_json 

alunos = {
    "João": 8.5,
    "Maria": 9.0,
    "Pedro": 7.5,
    "Ana": 8.0,
    "Lucas": 9.2
}

# Função para ler um arquivo JSON
def test_escrever_arquivo_json():
    caminho_arquivo = "teste exercício 5"
    resultado = escrever_arquivo_json(alunos, caminho_arquivo)
     
    assert resultado is None
    assert os.path.exists(f"{caminho_arquivo}.json")

    
    with open(f"{caminho_arquivo}.json", 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)
        assert dados == alunos

def test_arquivo_errado():
    caminho_arquivo = "teste JSON inválido"
    


