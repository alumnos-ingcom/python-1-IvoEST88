################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
# Precondicion: Ingresar grado centigrado y grado fahrenheit
# Postcondicion: Imprime cuantos grados fahrenheit equivalen "X" grados celsius y viceversa
################
"""
1. Conversión de temperaturas
"""
#Se quiere transformar temperaturas en fahrenheit a centígrados y viceversa.
#Escribir la funcion para convertir la temperatura en grados centigrados en fahrenheit como decimal

def principal():
    """
    Programa
    """
    centigrados = int(input("Ingrese °C a convertir: "))
    fahrenheit = int(input("Ingrese °F a convertir: "))
    print (f"{centigrados}ºC equivalen a: {convertir_a_fahrenheit(centigrados)} ºF")
    print (f"{fahrenheit}ºF equivalen a: {convertir_a_centigrados(fahrenheit)} ºC")
def convertir_a_fahrenheit(centigrados):
    """
    Convierte centigrados a fahrenheit
    """
    return float((centigrados* 1.8) + 32)
def convertir_a_centigrados(fahrenheit):
    """
    Convierte fahrenheit a centigrados
    """
    return round(((fahrenheit-32) / 1.8),2)

if __name__=="__main__":
    principal()
