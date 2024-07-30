from suma import suma
from resta import resta
from suma_avanzada import suma_avanzada
from multiplicacion import multiplicacion
from division import division

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Suma avanzada")
    print("0. Salir")

def pedir_numeros():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    return a, b

def main():
    print("Bienvenido a la calculadora Open Source")
    menu()
    opcion = int(input("Por favor seleccione una opcion: "))
    while opcion < 0 or opcion > 5:
        opcion = int(input("Por favor ingrese una opcion valida: "))

    while opcion != 0:
        if opcion == 1:
            a, b = pedir_numeros()
            print(f'La suma de {a} y {b} es igual a:',suma(a, b))

        elif opcion == 2:
            a, b = pedir_numeros()
            print(f'La resta de {a} y {b} es igual a:',resta(a, b))

        elif opcion == 3:
            a, b = pedir_numeros()
            print(f'La multiplicacion de {a} y {b} es igual a:', multiplicacion(a, b))

        elif opcion == 4:
            a, b = pedir_numeros()
            print(f'La division de {a} y {b} es igual a:',division(a, b))

        elif opcion == 5:
            suma = suma_avanzada()
            print(f'La suma de los numeros ingresados es igual a:', suma)

        continuar = input("Desea realizar otra operacion (s/n): ")
        if continuar == 'n':
            break
        elif continuar == 's':
            menu()
            opcion = int(input("Por favor seleccione una opcion: "))

    print("Gracias por usar la calculadora Open Source")

main()