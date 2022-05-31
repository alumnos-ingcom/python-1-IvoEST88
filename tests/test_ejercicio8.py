"""
Tests de los ejercicios en la carpeta src
"""
import pytest

from src.ejercicio8 import es_primo

def test_es_primo():
    numero = 2
    resultado = es_primo(numero)
    assert isinstance (resultado, int), "El resultado esperado es True"
    assert resultado == True, "El resultado esperado es True"
def test_es_primo_neg():
    numero = -2
    resultado = es_primo(numero)
    assert isinstance (resultado, int), "El resultado esperado es True"
    assert resultado == True, "El resultado esperado es True"
def test_es_primo_falso():
    numero = 8
    resultado = es_primo(numero)
    assert isinstance (resultado, int), "El resultado esperado es False"
    assert resultado == False, "El resultado esperado es False"
def test_es_primo_falso_neg(): 
    numero = -8
    resultado = es_primo(numero)
    assert isinstance (resultado, int), "El resultado esperado es False"
    assert resultado == False, "El resultado esperado es False"
    