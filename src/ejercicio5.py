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
    signo2=1
    cociente = 0
    if dividendo <0 and divisor >0:
        dividendo *= -1
        signo = -1
    elif dividendo >0 and divisor >0:
        signo = 1
    elif divisor <0 and dividendo >0:
        divisor *= -1
        signo2 = -1
    elif divisor <0 and dividendo <0:
        signo = -1
        signo2 = -1
        dividendo *= -1
        divisor *= -1
    elif dividendo < divisor:
        return print("El dividendo no puede ser menor al divisor")
    else:
        return print("El divisor no puede ser 0!")
    while dividendo >= divisor:
        cociente += 1
        print(f"{dividendo} - {divisor}")
        dividendo -= divisor
        print(f"Resto : {signo}{dividendo}")
        print("--------------")
    dividendo *= signo
    divisor *= signo2
    cociente *= signo
    cociente *= signo2
    resto = dividendo
    return print(f"Cociente: {cociente}\nResto: {resto}")
def principal():
    """
    Programa
    """
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    return division_lenta(dividendo, divisor)
if __name__=="__main__":
    principal()
    