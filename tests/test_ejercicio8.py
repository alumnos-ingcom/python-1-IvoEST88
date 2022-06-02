"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio8 import es_primo


def test_es_primo():
    """
    Test con número "2"
    """
    numero = 2
    resultado = es_primo(numero)
    assert isinstance(resultado, int), "El resultado debe ser True"
    assert resultado is True, "No se obtuvo el resultado esperado"


def test_es_primo_neg():
    """
    Test con número "-2"
    """
    numero = -2
    resultado = es_primo(numero)
    assert isinstance(resultado, int), "El resultado debe ser True"
    assert resultado is True, "No se obtuvo el resultado esperado"


def test_es_primo_falso():
    """
    Funcion con número no primo
    """
    numero = 8
    resultado = es_primo(numero)
    assert isinstance(resultado, int), "El resultado debe ser False"
    assert resultado is False, "No se obtuvo el resultado esperado"


def test_es_primo_falso_neg():
    """
    Funcion con número negativo no primo
    """
    numero = -8
    resultado = es_primo(numero)
    assert isinstance(resultado, int), "El resultado debe ser False"
    assert resultado is False, "No se obtuvo el resultado esperado"
