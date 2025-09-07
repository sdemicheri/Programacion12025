#Utilizando la estructura condicional multiple. Realice un algoritmo que ingresando un número del 0 al 5, muestre un mensaje indicando el mismo numero escrito en letras.
#Entrada: 1
#Salida: "uno"


numero=int(input("Ingrese un numero:"))
if numero==0:
    print("cero")
elif numero == 1:
    print("uno")
elif numero == 2:
    print("dos")
elif numero == 3:
    print("tres")
elif numero == 4:
    print("cuatro")
elif numero == 5:
    print("cinco")
else:
    print("Número fuera de rango")