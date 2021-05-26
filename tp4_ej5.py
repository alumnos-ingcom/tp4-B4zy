################
# Tomás Gadea - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def signo(numero):
    if numero < 0:
        return -1
    elif numero == 0:
        return 0
    else:
        return 1    
    
def prueba():
    while True:
        numero = input("Ingrese un numero: ")
        try:
            numero = int(numero)
            break
        except ValueError:
            print("Oops eso no era un numero.")
            
    mostrar = signo(numero)
    
    if mostrar < 0:
        print("El numero es negativo")
    elif numero == 0:
        print("El numero es cero")
    else:
        print("El numero es positivo")
        
prueba()