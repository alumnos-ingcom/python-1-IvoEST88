################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
# Precondicion: Ingresar numero y multiplo
# Postcondicion: Indica con True si el numero es multiplo del segundo número ingresado.
################
"""
11. Multiplos de
"""
#Escribir una función que indique con True si un número entero es
#multiplo de otro, utilizando sumas y restas.
def es_multiplo(numero, multiplo):
    """
    Esta funcion indica si un numero es multiplo de otro.
    """
    if multiplo == 0:
        resultado = "0 es multiplo de todos los números"
    else:
        if multiplo <0 or numero <0:
            multiplo = abs(multiplo)
            numero = abs(numero)
        else:
            pass
        while numero > 0:
            numero -= multiplo
            if numero == 0:
                resultado = True
            else:
                resultado = False
    return resultado
def principal():
    """
    Programa
    """
    numero = (int(input("Ingrese un número: ")))
    multiplo = (int(input("Ingrese el numero a determinar si es multiplo: ")))
    resultado_es_multiplo = es_multiplo(numero, multiplo)
    print (resultado_es_multiplo)
if __name__=="__main__":
    principal()
