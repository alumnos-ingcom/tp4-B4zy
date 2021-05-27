################
# Tomás Gadea - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def convertir_a_fahrrenheit(centigrados):
    return (centigrados * 1.8) + 32

def convertir_a_centigrados(fahrrenheit):
    return (fahrrenheit - 32) / 1.8
    
def prueba():
    print("""
(1) Convertir de centigrados a fahrenheit
(2) Convertir de fahrenheit a centigrados
          """)
    while True:
        respuesta = input("Ingresa (1) o (2) ")
        try:
            respuesta = int(respuesta)
        except ValueError:
            print("Oops, eso no era un numero")
        if respuesta == 1 or respuesta == 2:
            break

    if respuesta == 1:
        while True:
            centigrados = input("Ingrese centigrados para convertir a fahrrenheit: ")
            try:
                centigrados = float(centigrados)
                break
            except ValueError:
                print("Oops, eso no era un numero")
                
        conversion = convertir_a_fahrrenheit(centigrados)
        print(f"La conversion a fahrrenheit da {conversion} grados")
    
    else:
        while True:
            fahrrenheit = input("Ingrese fahrrenheit para convertir a centigrados: ")
            try:
                fahrrenheit = float(fahrrenheit)
                break
            except ValueError:
                print("Oops, eso no era un numero")
                
        conversion = convertir_a_centigrados(fahrrenheit)
        print(f"La conversion a centigrados da {conversion} grados")
    
prueba()
