"""
Tests de los ejercicios en la carpeta src
"""
import pytest

from src.ejercicio11 import es_multiplo

def test_es_multiplo_true():
    numero = 10
    multiplo = 2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es True"
    assert resultado == True, "El resultado es el esperado"
def test_es_multiplo_false():
    numero = 10
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es False"
    assert resultado == False, "El resultado es el esperado"
def test_es_multiplo_true_numneg():
    numero = -10
    multiplo = 2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es True"
    assert resultado == True, "El resultado es el esperado"
def test_es_multiplo_false_numneg():
    numero = 10
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es False"
    assert resultado == False, "El resultado es el esperado"
def test_es_multiplo_true_multiploneg():
    numero = 10
    multiplo = -2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es True"
    assert resultado == True, "El resultado es el esperado"
def test_es_multiplo_false_multiploneg():
    numero = 10
    multiplo = -3
    resultado = es_multiplo(numero, multiplo)
    assert isinstance (resultado , int), "El resultado esperado es False"
    assert resultado == False, "El resultado es el esperado"
    