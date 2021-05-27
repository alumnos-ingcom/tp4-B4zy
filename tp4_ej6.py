################
# Tomás Gadea - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def minimo(lista):
    minimo = min(lista)
    return minimo
def maximo(lista):
    maximo = max(lista)
    return maximo
    
    
def prueba():
    import random
    while True:
        cantidad_elementos = input("Ingrese la cantidad de elementos de su lista: ")
        try:
            cantidad_elementos = int(cantidad_elementos)
            break
        except ValueError:
            print("Oops, eso no es un numero")
            
    lista = list(range(cantidad_elementos))
    cantidad_elementos_lista = len(lista)
    lista_random = [lista[random.randint(0, cantidad_elementos_lista - 1)] for i in range(len(lista))]
    print("Su lista generada aleatoriamente es:", lista_random)
    mostrar_minimo = minimo(lista_random)
    mostrar_maximo = maximo(lista_random)
    print(f"El valor minimo de tu lista es {mostrar_minimo} y el maximo es {mostrar_maximo}")
    
prueba()