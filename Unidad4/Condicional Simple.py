try:
    numero = int(input())
    if numero > 0:
        print("Es positivo")
except ValueError:
    print("Ingrese el valor correcto")