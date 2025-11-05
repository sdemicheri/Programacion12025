
def ejemplo1():

    edad = [0] * 10
    acu = 0
    for i in range(10):
        edad[i] = int(input())
        acu = acu + edad[i]
    prom = acu / 10
    print("Promedio General: ", prom)
    print("Edades mayores al promedio:")
    for i in range(10):
        if edad[i] > prom:
            print(f'{edad[i]}')
            
#EJEMPLO 2
def ejemplo2():

    vectorpalabra = [''] * 5
    conta = 0
    for i in range(len(vectorpalabra)):
        vectorpalabra[i] = input("Ingrese una palabra: ")
        if len(vectorpalabra[i]) > 5:
            conta += 1

#EJEMPLO 3
def ejemplo3():

    vector = [0] * 10
    asiento = int(input("Ingrese un numero de asiento "))
    while asiento != 0:
        vector[asiento -1] = 1
        asiento = int(input("Ingrese un numero de asiento "))
    print(vector)

#EJEMPLO 4
def ejemplo4():
    try:
        vector = [0] * 5
        posicion = 0
        numero = int(input("Ingrese un numero de asiento "))
        while numero != 0:
            vector[posicion] = numero
            posicion = posicion + 1
            numero = int(input("Ingrese un numero de asiento "))
        print(vector)
        for i in range(posicion):
            print(vector[i], end=" ")
    except IndexError:
        print("No hay mas espacios")
    except ValueError:
        print("Error, ingrese un numero valido")


#Cantidad de edades mayor que el promedio
def mayores_promedio():
    edad = [0] * 10
    acu = 0
    for i in range(10):
        edad[i] = int(input("Ingrese edad:"))
        acu = acu + edad[i]
    prom = acu / 10
    mayores = 0
    for i in range(10):
        if edad[i] > prom:
            mayores += 1
    print("Promedio General: ", prom)
    print("Cantidad de Edades mayores al promedio: ", mayores)

def numeros_pares():
    numeros = [0] * 10
    acu = 0
    for i in range(10):
        numeros[i] = int(input("Ingrese un número:"))
        if numeros[i] % 2 == 0:
            acu += 1
    print("Cantidad de números pares:", acu)
    print("Numeros: ", )
    for i in range(10):
        if numeros[i] % 2 == 0:
            print(i)

def mayoritario():
    n = int(input())
    vector = [0] * n
    for i in range(n):
        vector[i] = int(input("Ingrese un numero:"))
    mayoritario = 0
    rep = 0
    for i in range(n):
        contador = 0
        for j in range(n):
            if vector[i] == vector[j]:
                contador += 1
        if contador > rep:
            rep = contador
            mayoritario = vector[i]
    if rep > n // 2:
        print("No hay mayoritario")

def main():
    print("--Ejercicios de vectores---")
    print("1. Ejemplo 1")
    print("2. Ejemplo 2")
    print("3. Ejemplo 3")
    print("4. Ejemplo 4")
    print("5. Mayores al promedio")
    print("6. Números pares")
    print("7. Mayoritario")
    opcion = int(input("Opción: "))
    match opcion:
        case 1:
            ejemplo1()
        case 2:
            ejemplo2()
        case 3:
            ejemplo3()
        case 4:
            ejemplo4()
        case 5:
            mayores_promedio()
        case 6:
            numeros_pares()
        case 7:
            mayoritario()
main()
