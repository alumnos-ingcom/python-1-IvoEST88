"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio11 import es_multiplo


def test_es_multiplo_true():
    """
    Test con numero divisible por 2
    """
    numero = 10
    multiplo = 2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser True"
    assert resultado is True, "No se obtuvo el resultado esperado"


def test_es_multiplo_false():
    """
    Test con un numero no divisible por 3
    """
    numero = 10
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser False"
    assert resultado is False, "No se obtuvo el resultado esperado"


def test_es_multiplo_true_numneg():
    """
    Test con numero negativo y multiplo positivo.
    """
    numero = -10
    multiplo = 2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser True"
    assert resultado is True, "No se obtuvo el resultado esperado"


def test_es_multiplo_false_numneg():
    """
    Test con numero negativo y multiplo positivo
    """
    numero = -10
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser False"
    assert resultado is False, "No se obtuvo el resultado esperado"


def test_es_multiplo_true_multiploneg():
    """
    Test con numero positivo y multiplo negativo
    """
    numero = 10
    multiplo = -2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser True"
    assert resultado is True, "No se obtuvo el resultado esperado"


def test_es_multiplo_false_multiploneg():
    """
    Test con numero positivo y multiplo negativo
    """
    numero = 10
    multiplo = -3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, int), "El resultado debe ser False"
    assert resultado is False, "No se obtuvo el resultado esperado"
