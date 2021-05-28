################
# Tomás - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def factores_primos(numero):
    factor_primo = []
    i = 2
    while numero != 1:
        if numero % i == 0:
            numero = numero / i
            factor_primo.append(i)   
        elif numero % i != 0:
            i = i + 1
    return tuple(factor_primo)    
        




def prueba():
    
    while True:
        numero_ingresado = input("Ingrese un numero: ")
        try:
            numero_ingresado = int(numero_ingresado)
            break
        except ValueError:
            print("Oops, eso no era un numero")
            
    mostrar = factores_primos(numero_ingresado)
    print(f"Los factores primos de {numero_ingresado} son: {mostrar}")
    
prueba()