"""
Tests de los ejercicios en la carpeta src
"""
import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

def test_ordenar_mayor_a_menor():
    uno = 1
    dos = 2
    tres = 3
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    esperado = 3, 2, 1
    assert isinstance (resultado, tuple), "El resultado debe ser (3, 2, 1)"
    assert resultado== esperado, "Se obtuvo el resultado esperado"

def test_ordenar_menor_a_mayor():
    uno = 1
    dos = 2
    tres = 3
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    esperado = 1, 2, 3
    assert isinstance (resultado, tuple), "El resultado debe ser (1, 2, 3)"
    assert resultado == esperado, "Se obtuvo el resultado esperado"