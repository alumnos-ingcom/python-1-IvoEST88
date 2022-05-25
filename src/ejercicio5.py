################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
"""
#Escribir una función que mediante restas sucesivas
#obtenga el valor del cociente y resto de dos números enteros.

def signos(dividendo, divisor):
    """
    Funcion que saca el signo
    """
    if dividendo < 0 and divisor < 0:
        dividendo = dividendo * -1
        divisor = divisor * -1
        signo = 1
        print ("Ambos numeros cambiaron de signo.")
    elif dividendo < 0:
        dividendo = dividendo * -1
        signo = -1
        print ("Dividendo cambio a signo positivo.")
    elif divisor < 0:
        divisor = divisor * - 1
        signo = -1
        print ("Divisor cambio a signo positivo.")
    else:
        signo = 1
    return dividendo, divisor, signo
def division_lenta(dividendo, divisor):
    """
    Division mediante una resta sucesiva
    """
    divisor_original= divisor
    dividendo_original= dividendo
    cociente = 0
    if divisor == 0:
        print("No se puede dividir por 0.")
    else:
        while dividendo >=divisor:
            cociente += 1
            print(f"{dividendo} - {divisor}")
            dividendo -= divisor
            print(f"Resto : {dividendo}")
            print("--------------")
    print (f"{dividendo_original} / {divisor_original}: {cociente}.")
    print (f"Resto: {dividendo}")
    return cociente, dividendo
def principal():
    """
    programa
    """
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    print (division_lenta(dividendo, divisor))
if __name__=="__main__":
    principal()
