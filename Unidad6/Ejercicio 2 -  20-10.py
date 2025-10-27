try:

    vector = [0]*100
    posicion = 0
    numero = int(input("Ingrese el numero hasta 0: "))
    while numero !=0:
        vector[posicion] = numero
        posicion = posicion + 1
        numero = int(input("Ingrese el numero hasta 0: "))

    for i in range(posicion):
        print(vector[i], end=" ")

except IndexError:
    print("No hay más espacio loquillo.")
except ValueError:
    print("Ingrese un valor.")
    
#----------
numero = [0]*10
contador = 0
for i in range(10):
    numero = int(input())
    if numero[i] % 2 == 0:
        contador += 1
        numero[contador-1] = i
print(f"Cantidad: {contador}")
print("Numeros")
print(contador[i])