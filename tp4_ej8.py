################
# Tomás - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def ordenar_mayor_a_menor(uno, dos, tres):
    mayor_menor = (uno, dos, tres)
    return sorted(mayor_menor, reverse = True)
def ordenar_menor_a_mayor(uno, dos, tres):
    menor_mayor = (uno, dos, tres)
    return sorted(menor_mayor)


def prueba():
    
    tupla = []
    while True: 
        numero_ingresado = input("Ingrese un numero para su tupla: ")
        try:
            numero_ingresado = int(numero_ingresado)
            tupla.append(numero_ingresado)
            if len(tupla) == 3:
                tupla = tuple(tupla)
                print("Su tupla original es: ", tupla)
                break
        except ValueError:
            print("Oops, eso no era un numero")
            
    mostrar_mayor_menor = ordenar_mayor_a_menor(tupla[0], tupla[1], tupla[2])
    mostrar_menor_mayor = ordenar_menor_a_mayor(tupla[0], tupla[1], tupla[2])
    mostrar_mayor_menor = tuple(mostrar_mayor_menor)
    mostrar_menor_mayor = tuple(mostrar_menor_mayor)
    print(f"Su tupla de mayor a menor: {mostrar_mayor_menor} y de menor a mayor: {mostrar_menor_mayor}")
    
    
prueba()