try:
    numero=int(input("Ingrese un número: "))
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
except ValueError:
    print("Ingresó un dato no válido")
