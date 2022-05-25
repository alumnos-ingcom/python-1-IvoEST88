################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
10. Palíndromo
"""
#Escribir una función que indique con True si una palabra ingresada se trata de un palindromo.
#Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.

def es_palindromo(texto):
    """
    funcion que retorna true si la palabra ingresada es palindromo.
    """
    if str(texto) == str(texto)[::-1]:
        valor = "True"
    else:
        valor = "False"
    return valor
def principal():
    """
    Programa
    """
    texto = input("Ingrese una palabra o frase Palindromo: ")
    texto = texto.lower() #poner todas las letras en minuscula
    texto = "".join(texto.split()) #quitar espacios
    print (es_palindromo(texto))
if __name__=="__main__":
    principal()
