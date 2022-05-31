"""
Tests de los ejercicios en la carpeta src
"""
import pytest

from src.ejercicio3 import compara

def test_compara_menor():
    """
    Test donde el primer numero es menor al segundo
    """
    num1 = 5
    num2 = 10
    resultado = compara(num1, num2)
    assert isinstance(resultado, int), "El resultado debe ser -1"
    assert resultado ==-1.0, "Se obtuvo el resultado esperado"
def test_compara_igual():
    """
    Test donde ambos numeros son iguales
    """
    num1 = 5
    num2 = 5
    resultado = compara(num1, num2)
    assert isinstance(resultado, int), "El resultado debe ser 0"
    assert resultado ==0, "Se obtuvo el resultado esperado"
def test_compara_mayor():
    """
    Test donde el primer numero es mayor al segundo
    """
    num1 = 10
    num2 = 5
    resultado = compara(num1, num2)
    assert isinstance(resultado, int), "El resultado debe ser 5"
    assert resultado ==1, "Se obtuvo el resultado esperado"
    