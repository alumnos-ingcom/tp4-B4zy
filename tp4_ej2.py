################
# Tomás Gadea - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    resultado = numero + otro_numero
    if (resultado < 0) or (numero > 0 and otro_numero < 0):
        if (numero < 0 and otro_numero > 0):
            while numero != resultado:
                numero = numero + 1
        else:
            while numero > resultado:
                numero = numero - 1
    elif (resultado > 0) or (numero < 0 and otro_numero > 0):
        while numero < resultado:
            numero = numero + 1
            
    return numero
    
def prueba():
    primer_numero = (int(input("Ingrese un numero: ")))
    segundo_numero = (int(input("Ingrese otro numero: ")))
    resultado = suma_lenta(primer_numero, segundo_numero)
    print (f"El resultado es {resultado}")

prueba()
