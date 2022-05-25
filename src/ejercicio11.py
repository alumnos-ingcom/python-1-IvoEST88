################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
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
        print ("0 es multiplo de todos los números")
    else:
        while numero > 0:
            numero -= multiplo
            if numero == 0:
                resultado = "True"
            else:
                resultado = "False"
    return resultado
def principal():
    """
    Programa
    """
    numero = abs(int(input("Ingrese un número: ")))
    multiplo = abs(int(input("Ingrese el numero a determinar si es multiplo: ")))
    print(es_multiplo(numero, multiplo))
if __name__=="__main__":
    principal()
