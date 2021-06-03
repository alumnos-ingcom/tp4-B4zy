################
# Tomás Gadea - @B4zy
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_palindromo(texto):
    palindromo = list(texto)
    palindromo_reverse = list(reversed(palindromo))
    if palindromo == palindromo_reverse:
        return True
    else:
        return False

def prueba():
    
    mostrar = es_palindromo(input("Ingresa algo: "))
    if mostrar == True:
        print(f"[{mostrar}] Es palíndromo")
    else:
        print(f"[{mostrar}] No es palíndromo")
        
if __name__ == "__main__":
    prueba()
