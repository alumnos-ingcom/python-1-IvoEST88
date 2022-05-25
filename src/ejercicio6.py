################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
6. Ordenar 3 valores
"""
#Escribir una función que a partir de tres variables de tipo entero retorne
#una tupla con dichos valores ordenados de menor a mayor. Y Viceversa

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Ordenar de mayor a menor
    """
    if dos<uno>tres:
        if dos>tres:
            tupla=(uno,dos,tres)
        else:
            tupla=(uno,tres,dos)
    elif uno<dos>tres:
        if uno>tres:
            tupla=(dos,uno,tres)
        else:
            tupla=(dos,tres,uno)
    else:
        if dos>uno:
            tupla=(tres,dos,uno)
        else:
            tupla=(tres,uno,dos)
    return tupla
def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Ordenar de menor a mayor
    """
    if uno<dos<tres:
        if dos<tres:
            tupla=(uno,dos,tres)
        else:
            tupla=(uno,tres,dos)
    elif uno>dos<tres:
        if uno<tres:
            tupla=(dos,uno,tres)
        else:
            tupla=(dos,tres,uno)
    elif uno>tres<dos:
        if dos<uno:
            tupla=(tres,dos,uno)
        else:
            tupla=(tres,uno,dos)
    return tupla

def principal():
    """
    Programa
    """
    uno = int(input("Ingrese un número: "))
    dos = int(input("Ingrese un número: "))
    tres = int(input("Ingrese un número: "))
    print(ordenar_mayor_a_menor(uno, dos, tres))
    print (ordenar_menor_a_mayor(uno, dos, tres))
if __name__=="__main__":
    principal()
              