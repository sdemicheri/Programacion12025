try:
    numero = int(input())
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
except ValueError:
    print("Ingrese un numero")