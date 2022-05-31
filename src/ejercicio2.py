################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
# Precondicion: Ingresar un numero
# Postcondicion: determina si el numero es negativo, positivo o igual a cero
################

"""
2. Números positivos y negativos
"""
#Escribir una función que reciba un número e indique si el mismo es:
#positivo, negativo o cero utilizando sumas y restas.
def principal():
    """
    Programa
    """
    numero = int(input("Ingrese un número: "))
    return signo(numero)
def signo(numero):
    """
    Ingresar numero, determinar si es positivo, negativo o cero
    """
    if numero==0:
        sgn = print("Cero")
        return 0
    elif numero + abs(numero)==0:
        sgn = print("Negativo")
        return -1
    else:
        sgn = print("Positivo.")
        return 1

if __name__=="__main__":
    principal()
