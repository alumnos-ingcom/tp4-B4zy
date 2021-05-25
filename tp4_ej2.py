################
# Tomás Gadea - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    resultado = numero + otro_numero
    if resultado < 0 or (numero > 0 and otro_numero < 0):
        while numero >= resultado:
            numero = numero - 1
            mostrar = numero + 1
            return numero + otro_numero
    elif resultado > 0 or (numero < 0 and otro_numero > 0):
        while numero <= resultado:
            numero = numero + 1
            mostrar = numero - 1
            return numero + otro_numero
    
def prueba():
    primer_numero = int(input("Ingrese un entero: "))
    segundo_numero = int(input("Ingrese otro entero: "))
    suma_lenta(primer_numero, segundo_numero)
prueba()
