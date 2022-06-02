"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio2 import signo


def test_signo_positivo():
    """
    Test con un numero positivo
    """
    numero = 2
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser positivo"
    assert resultado == 1, "No se obtuvo el resultado esperado"


def test_signo_cero():
    """
    Test con 0
    """
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser cero"
    assert resultado == 0, "No se obtuvo el resultado esperado"


def test_signo_negativo():
    """
    Test con un numero negativo
    """
    numero = -2
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser negativo"
    assert resultado == -1, "No se obtuvo el resultado esperado"
