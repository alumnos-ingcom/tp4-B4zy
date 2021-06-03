################
# Tomás Gadea - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def compara(numero, otro_numero):
    if numero < otro_numero:
        return -1
    elif numero == otro_numero:
        return 0
    else:
        return 1
    
def prueba():
    while True:
        primer_numero = input("Ingrese un numero: ")
        try:
            primer_numero = int(primer_numero)
            break
        except ValueError:
            print("Oops, eso no era un numero.")
            
    while True:
        segundo_numero = input("Ingrese otro numero: ")
        try:
            segundo_numero = int(segundo_numero)
            break
        except ValueError:
            print("Oops, eso no era un numero.")
            
    mostrar = compara(primer_numero, segundo_numero)
    print(mostrar)
    
if __name__ == "__main__":
    prueba()           
            
            
            
            
            
