"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio5 import division_lenta


def test_division_lenta_pos():
    """
    Test donde tanto el dividendo y el divisor son positivos
    """
    dividendo = 10
    divisor = 2
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, int), "El resultado debe ser 5;0"
    assert resultado == 5; 0, "No se obtuvo el resultado esperado"


def test_division_lenta_neg():
    """
    Test donde ambos valores son negativos
    """
    dividendo = -10
    divisor = -2
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, int), "El resultado debe ser 5;0"
    assert resultado == 5; 0, "No se obtuvo el resultado esperado"


def test_division_lenta_pos_neg():
    """
    Test donde el dividendo es positivo y el divisor es negativo
    """
    dividendo = 10
    divisor = -2
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, int), "El resultado debe ser -5;0"
    assert resultado == -5; 0, "No se obtuvo el resultado esperado"


def test_division_lenta_neg_pos():
    """
    Test donde el dividendo es negativo y el divisor es positivo
    """
    dividendo = -10
    divisor = 2
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, int), "El resultado debe ser -5;0"
    assert resultado == -5; 0, "El resultado es el esperado"
