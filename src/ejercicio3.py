################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
# Precondicion: Ingresar dos números
# Postcondicion: retorna un valor dependiendo si el primer numero es mayor, menor o igual al segundo numero ingresado
################

"""
3. Comparación de números
"""

#Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:
###Retornar -1 si el primero es menor que el segundo
###Retornar 0 si son iguales
###Retornar 1 si el primero es mayor que el segundo
def compara(num1, num2):
    """
    Comparar ambos valores, indicar cual es mayor, menor o si son iguales
    """
    if num1 == num2:
        return 0
    elif num1 - num2 >= 0:
        return 1
    else:
        return -1

def principal():
    """
    Programa
    """
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    print(f"El resultado es: {compara(num1, num2)}")

if __name__=="__main__":
    principal()
