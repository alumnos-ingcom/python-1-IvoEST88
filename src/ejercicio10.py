################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
# Precondicion: Ingresar palabra o frase.
# Postcondicion: Determinar si la palabra/frase es palindromo.
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
    texto = texto.lower() #poner todas las letras en minuscula
    texto = "".join(texto.split()) #quitar espacios
    if str(texto) == str(texto)[::-1]:
        return True
    else:
        return False
def principal():
    """
    Programa
    """
    texto = input("Ingrese una palabra o frase Palindromo: ")
    print (es_palindromo(texto))
if __name__=="__main__":
    principal()
