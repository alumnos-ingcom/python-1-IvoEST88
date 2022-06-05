################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
# Precondicion: Ingresar dos numeros
# Postcondicion: Devuelve la suma lenta de ambos numeros
################

"""
4. Suma lenta
"""
#Escribir una función que haga la suma entre dos números enteros sin operacion de manera directa.
#La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.


def suma_lenta(num1, num2):
    """
    Ingresar dos numeros, y realizar una suma lenta.
    """
    while num2>0 or num2<0:
        if num1 >= 0 and num2 >= 0:
            suma = num1 + 1
            num2 -= 1
            print (f"{num1} + 1 = {suma}")
            num1 += 1
        elif num1 <= 0 and num2 <= 0:
            suma= num1 - 1
            num2 += 1
            print (f"{num1} - 1 = {suma}")
            num1 -= 1
        elif num1 >= 0:
            suma= num1 - 1
            num2 += 1
            print (f"{num1} - 1 = {suma}")
            num1 -= 1
        else:
            suma= num1 + 1
            num2 -= 1
            print (f"{num1} + 1 = {suma}")
            num1 += 1
    return num1


def principal():
    """
    Programa
    """
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    resultado_suma_lenta = suma_lenta(num1, num2)
    print(f"El resultado de la suma lenta es: {resultado_suma_lenta}")
if __name__=="__main__":
    principal()
