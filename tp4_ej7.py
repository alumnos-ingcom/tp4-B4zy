################
# Tomás Gadea - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def division_lenta(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        cociente = cociente + 1
        dividendo = dividendo - divisor
    resto = dividendo
    mostrar = [resto, cociente]
    return mostrar
        
    
    
def prueba():
    while True:
        primer_numero = input("Ingrese un numero: ")
        try:
            primer_numero = int(primer_numero)
            break
        except ValueError:
            print("Oops, eso no era un numero")
            
    while True:     
        segundo_numero = input("Ingrese otro numero: ")
        try:
            segundo_numero = int(segundo_numero)
            break
        except ValueError:
            print("Oops, eso no era un numero")
            
    mostrar = division_lenta(primer_numero, segundo_numero)
    cociente = mostrar.pop(1)
    resto = mostrar.pop(0)
    print(f"El cociente es: {cociente} y el resto es: {resto}")
            
prueba()