import pytest
from ex20 import converter_temperatura

def test_converter_temperatura():
    assert converter_temperatura(0, "F") == 32
    assert converter_temperatura(100, "F") == 212
    assert converter_temperatura(0, "K") == 273.15
    assert converter_temperatura(100, "K") == 373.15
    assert converter_temperatura(0, "X") == 32
