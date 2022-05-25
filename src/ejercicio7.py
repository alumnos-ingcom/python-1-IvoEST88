################
# Nombre - @IvoEST88
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
7. Transformación de un número
"""
#Escribir un programa que :
#permita convertir un número solicitado expresado en grados, minutos y segundos.
#Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    convercion sexadecimal a decimal
    """
    total = (horas) * 3600 + (minutos) * 60 + (segundos)
    return total
def decimal_a_sexadecimal(seg_a_conv):
    """
    convercion decimal a sexadecimal
    """
    horas = int(seg_a_conv / 3600)
    segundos = seg_a_conv % 3600
    minutos = int(segundos / 60)
    segundos = segundos % 60
    return horas,minutos,segundos

def principal():
    """
    Programa
    """
    print ("1. Ingresar horas, minutos y segundos para convertirlo a segundos.")
    print ("2. Ingresar segundos y pasar a horas, minutos y segundos.")
    eleccion = int(input("Ingrese: "))
    if eleccion == 1:
        horas = int(input("Ingrese hora/s: "))
        minutos = int(input("Ingrese minuto/s: "))
        segundos = int(input("Ingrese segundo/s: "))
        print (sexadecimal_a_decimal(horas, minutos, segundos))
    else:
        seg_a_conv = int(input("Ingrese segundos: "))
        print (decimal_a_sexadecimal(seg_a_conv))
if __name__=="__main__":
    principal()
    