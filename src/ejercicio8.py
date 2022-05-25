################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
8. Números primos
"""
#Escribir una función que indique con True si un numero indicado es Primo.

def es_primo(numero):
    """
    Indicar con true si un numero indicado es primo.
    """
    div = 2
    primo = 0
    while primo == 0 and div<numero:
        if numero%div==0:
            primo = 1
        else:
            div += 1
    if primo == 1:
        resultado = "False"
    else:
        resultado = "True"
    return resultado
def principal():
    """
    Programa
    """
    numero = int(input("Ingrese un valor: "))
    print (es_primo(numero))
if __name__=="__main__":
    principal()
