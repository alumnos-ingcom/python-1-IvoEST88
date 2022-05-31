"""
Tests de los ejercicios en la carpeta src
"""
import pytest

from src.ejercicio10 import es_palindromo

def test_es_palindromo_true():
    """
    Test con frase palindromo
    """
    texto= "Isaac no ronca asi"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, int), "El resultado esperado es True"
    assert resultado is True, "El resultado es el esperado"
def test_es_palindromo_false():
    """
    Test con una palabra no palindromo
    """
    texto= "Roma"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, int), "El resultado esperado es False"
    assert resultado is False, "El resultado es el esperado"
    