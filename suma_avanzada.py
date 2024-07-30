# Description: Función que recibe una cantidad variable de argumentos y devuelve la suma de los mismos.
def suma_avanzada():
    n = 1
    suma = 0
    print("Ingrese los numeros que desea sumar")
    print("0 para terminar la suma")
    while n != 0:
        n = int(input("--> "))
        suma += n
    return suma
