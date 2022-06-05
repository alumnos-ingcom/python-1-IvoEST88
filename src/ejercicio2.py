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
def signo(numero):
    """
    Funcion que determina si un numero es Positivo, Negativo o igual a Cero
    """
    if numero==0:
        sgn = 0
        print ("Cero")
    else:
        if numero + abs(numero)==0:
            sgn = -1
            print ("Negativo")
        else:
            print ("Positivo")
            sgn = 1
    return sgn
def principal():
    """
    Programa
    """
    numero = int(input("Ingrese un número: "))
    resultado_signo = signo(numero)
    print (resultado_signo)
if __name__=="__main__":
    principal()
