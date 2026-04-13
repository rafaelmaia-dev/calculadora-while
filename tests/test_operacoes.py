import pytest
import math
from operacoes import operacao_aritmetica

def teste_soma():
    assert math.isclose(operacao_aritmetica(1.0, 1.0, '+'), 2.0) 

def teste_sub():
    assert math.isclose(operacao_aritmetica(3.0, 2.0, '-'), 1.0)

def teste_multi():
    assert math.isclose(operacao_aritmetica(3.0, 3.0, '*'), 9.0)

def teste_div_zero():
    with pytest.raises(ValueError, match = "Divisão por zero"):
        operacao_aritmetica(10.0, 0, '/')

def test_operador_valido():
    with pytest.raises(ValueError):
        operacao_aritmetica(1, 1, '%')



