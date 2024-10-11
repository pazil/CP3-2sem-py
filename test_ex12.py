import pytest
from ex12 import encontrar_maior_numero

def test_encontrar_maior_numero():
    assert encontrar_maior_numero(10, 5, 3) == 10
    assert encontrar_maior_numero(5, 15, 3) == 15
    assert encontrar_maior_numero(5, 3, 20) == 20
    assert encontrar_maior_numero(-1, -5, -3) == -1
