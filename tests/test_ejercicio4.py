"""
Tests de los ejercicios en la carpeta src
"""
import pytest

from src.ejercicio4 import suma_lenta

def suma_lenta_pos_ambos():
    """
    Test donde ambos numeros son positivos
    """
    num1 = 5
    num2 = 5
    resultado = suma_lenta(num1, num2)
    assert isinstance(resultado, int), "El resultado debe ser 10"
    assert resultado ==10, "Se obtuvo el resultado esperado"
def suma_lenta_neg_ambos():
    """
    Test donde ambos numeros son negativos
    """
    num1 = -5
    num2 = -5
    resultado = suma_lenta(num1, num2)
    assert isinstance(resultado, int), "El resultado debe ser -10"
    assert resultado ==-10, "Se obtuvo el resultado esperado"
def suma_lenta_pos_neg():
    """
    Test donde num1 es positivo y num2 negativo
    """
    num1 = 5
    num2 = -5
    resultado = suma_lenta(num1, num2)
    assert isinstance(resultado, int), "El resultado debe ser 0"
    assert resultado ==0, "Se obtuvo el resultado esperado"
def suma_lenta_neg_pos():
    """
    Test donde num1 es negativo y num2 positivo
    """
    num1 = -5
    num2 = 5
    resultado = suma_lenta(num1, num2)
    assert isinstance(resultado, int), "El resultado debe ser 0"
    assert resultado ==0, "Se obtuvo el resultado esperado"
    