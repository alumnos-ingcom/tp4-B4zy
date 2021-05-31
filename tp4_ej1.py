################
# Tomás Gadea - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 
    
def ingreso_entero(mensaje):
    """ Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
        de un número entero. """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto(f"[{ingreso}] No era un número'") from err
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    while cantidad_reintentos != 0:
        try:
            entero = ingreso_entero(mensaje)
            entero = int(entero)
            break
        except IngresoIncorrecto:
            cantidad_reintentos = cantidad_reintentos - 1
            print(f"Oops, eso no era un numero quedan: [{cantidad_reintentos}] intentos")
        if cantidad_reintentos == 0:
            raise IngresoIncorrecto("Ya no hay mas reintentos")

def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    entero= ingreso_entero(mensaje)
    if (entero < valor_minimo) or (entero > valor_maximo):
        raise IngresoIncorrecto("El numero ingresado no pertenece al rango")
         
def prueba():
    print(ingreso_entero("Ingrese un numero: "))
    print(ingreso_entero_reintento("Ingrese un numero nuevamente:"))
    print(ingreso_entero_restringido("Ingrese un numero entre 2 valores [0 - 10]"))
 
prueba()