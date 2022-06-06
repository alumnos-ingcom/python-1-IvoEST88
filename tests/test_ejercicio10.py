"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio10 import es_palindromo


def test_es_palindromo_true():
    """
    Test con frase palindromo
    """
    texto= "Isaac no ronca asi"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, int), "El resultado debe ser True"
    assert resultado is True, "No se obtuvo el resultado esperado"


def test_es_palindromo_false():
    """
    Test con una palabra no palindromo
    """
    texto= "Roma"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, int), "El resultado debe ser False"
    assert resultado is False, "No se obtuvo el resultado esperado"
