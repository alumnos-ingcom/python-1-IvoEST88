################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
# Precondicion: Ingresar un número
# Postcondicion: Determina los factores primos del numero ingresado
################
"""
9. Factores Primos
"""
#Escribir una función que retorne una tuple con factores primos de un numero entero positivo.

lista=[]
def factores_primos(numero):
    """
    Funcion que retorna una tuple con los factores primos de un numero positivo.
    """
    divisor = 2
    if numero < 0:
        numero = abs(numero)
        signo = -1
    else:
        signo = 1
    
    while numero>1:
        if numero%divisor == 0:
            numero=numero//divisor
            lista.append(divisor*signo)
        else:
            divisor +=1
    tuple(lista)
    return tuple(lista)
def principal():
    """
    Programa
    """
    numero = int(input("Ingrese un valor: "))
    print (factores_primos(numero))
if __name__=="__main__":
    principal()
    