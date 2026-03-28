import pytest
import math
from python.operacoes import operacao_aritmetica

def teste_soma():
    assert math.isclose(operacao_aritmetica(1.0, 1.0), 2.0) 

def teste_sub():
    assert operacao_aritmetica(3, 2, '-') == 1

def teste_multi():
    assert operacao_aritmetica(3, 3, '*') == 9

def teste_div_zero():
    with pytest.raises(ValueError, match = "Divisão por zero"):
        operacao_aritmetica(10, 0, '/')

def teste_operador_valido():
    with pytest.raises(ValueError):
        operacao_aritmetica(1, 1, '%')
