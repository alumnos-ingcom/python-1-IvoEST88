"""
Tests de los ejercicios en la carpeta src
"""
import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

def test_sexadecimal_a_decimal():
    """
    test para convertir 3 horas 8 minutos y 45 segundos a 11325 segundos
    """
    horas = 3
    minutos = 8
    segundos = 45
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance (resultado, int), "El resultado debe ser 11325"
    assert resultado == 11325, "El resultado es el esperado"

def test_decimal_a_sexadecimal():
    """
    test para convertir 11325 a 3 horas, 8 minutos y 45 segundos
    """
    seg_a_conv = 11325
    resultado = decimal_a_sexadecimal(seg_a_conv)
    assert isinstance (resultado, int), "El resultado debe ser 3;8;45"
    assert resultado == 3;8;45, "El resultado es el esperado"
    