################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
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
        sgn = "Cero"
    elif numero + abs(numero)==0:
        sgn = "Negativo"
    else:
        sgn = "Positivo."
    return sgn

print (principal())

if __name__=="__main__":
    principal()
