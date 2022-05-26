################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
"""
#Escribir una función que mediante restas sucesivas
#obtenga el valor del cociente y resto de dos números enteros.
def division_lenta(dividendo, divisor):
    """
    Division mediante una resta sucesiva
    """
    signo=1
    cociente = 0
    if dividendo <0:
        dividendo = abs(dividendo)
        signo = -1
    elif dividendo < divisor:
        return print("El dividendo no puede ser menor al divisor")
    elif dividendo >0 and divisor >0:
        signo = 1
    elif divisor <0:
        return print("No se puede utilizar un divisor igual o menor a 0")
    else:
        return print("No se puede utilizar un dividendo igual o menor a 0")
    while dividendo > divisor:
        cociente += 1
        print(f"{dividendo} - {divisor}")
        dividendo -= divisor
        dividendo *= signo
        print(f"Resto : {dividendo}")
        print("--------------")
    resto = dividendo
    return cociente, resto
def principal():
    """
    Programa
    """
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    return division_lenta(dividendo, divisor)
if __name__=="__main__":
    principal()
    