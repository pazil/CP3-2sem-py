import pytest
from ex14 import classificar_nota

def test_classificar_nota():
    assert classificar_nota(95) == "A"
    assert classificar_nota(85) == "B"
    assert classificar_nota(75) == "C"
    assert classificar_nota(65) == "D"
    assert classificar_nota(55) == "F"
