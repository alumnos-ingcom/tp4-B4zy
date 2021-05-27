################
# Tomás - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
        else:
            return True





def prueba():
    
    while True:
        numero_ingresado = input("Ingrese un numero: ")
        try:
            numero_ingresado = int(numero_ingresado)
            break
        except ValueError:
            print("Oops, eso no era un numero")
            
    numero_es_primo = es_primo(numero_ingresado)
    
    if numero_es_primo == False:
        print(f"El numero {numero_ingresado} es primo")
    else:
        print(f"El numero {numero_ingresado} no es primo")
        
prueba()