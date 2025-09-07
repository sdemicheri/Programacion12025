#Utilizando las excepciones para resolver el siguiente enunciado. Realice un algoritmo que ingresando un número, muestre un mensaje indicando si el número es divisible por 2 o no. En caso de ingresar un valor no numérico, mostrar el error "Los datos ingresados no son correctos"
#Entrada: un número.
#Salida: "Es divisible", "No es divisible", ó "Los datos ingresados no son correctos"

try:
    numero=int(input("Ingrese un número:"))
    if numero%2==0:
        print("Es divisible")
    else:
        print("No es divisible")
except ValueError:
    print("Los datos ingresados no son correctos")
