"""
Tests de los ejercicios en la carpeta src
"""
from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados

def test_convertir_a_fahrenheit():
    """
    Test de centigrados a fahrenheit ambos positivos
    """
    centigrados = 20
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser 68.0"
    assert resultado ==68.0, "No se obtuvo el resultado esperado"

def test_convertir_a_centigrados():
    """
    Test de fahrenheit a centigrados ambos positivos
    """
    fahrenheit = 70
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser 21.11"
    assert resultado ==21.11, "No se obtuvo el resultado esperado"

def test_convertir_a_centigrados_negativos():
    """
    Test de centigrados a fahrenheit ambos negativos
    """
    fahrenheit = -70
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser -56.67"
    assert resultado ==-56.67, "No se obtuvo el resultado esperado"

def test_converitr_a_fahrenheit_negativos():
    """
    Test de fahrenheit a centigrados ambos negativos
    """
    centigrados = -20
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser -4.0"
    assert resultado ==-4.0, "No se obtuvo el resultado esperado"
    