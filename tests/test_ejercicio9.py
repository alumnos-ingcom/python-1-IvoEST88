"""
Tests de los ejercicios en la carpeta src
"""
import pytest

from src.ejercicio9 import factores_primos
def test_factores_primos():
    numero = 18
    resultado = factores_primos(numero)
    esperado = 2, 3, 3
    assert isinstance (resultado, tuple), "El resultado debe ser (2, 3, 3)"
    assert resultado == esperado, "No se obtuvo el resultado esperado"