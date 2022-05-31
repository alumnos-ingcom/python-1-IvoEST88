"""
Tests de los ejercicios en la carpeta src
"""
import pytest

from src.ejercicio11 import es_multiplo

def test_es_multiplo_true():
    """
    Test con numero divisible por 2
    """
    numero = 10
    multiplo = 2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es True"
    assert resultado is True, "El resultado es el esperado"
def test_es_multiplo_false():
    """
    Test con un numero no divisible por 3
    """
    numero = 10
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es False"
    assert resultado is False, "El resultado es el esperado"
def test_es_multiplo_true_numneg():
    """
    Test con numero negativo y multiplo positivo.
    """
    numero = -10
    multiplo = 2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es True"
    assert resultado is True, "El resultado es el esperado"
def test_es_multiplo_false_numneg():
    """
    Test con numero negativo y multiplo positivo
    """
    numero = -10
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es False"
    assert resultado is False, "El resultado es el esperado"
def test_es_multiplo_true_multiploneg():
    """
    Test con numero positivo y multiplo negativo
    """
    numero = 10
    multiplo = -2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es True"
    assert resultado is True, "El resultado es el esperado"
def test_es_multiplo_false_multiploneg():
    """
    Test con numero positivo y multiplo negativo
    """
    numero = 10
    multiplo = -3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es False"
    assert resultado is False, "El resultado es el esperado"
    