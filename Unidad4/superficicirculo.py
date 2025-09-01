pi = 3.1416
try:
    radio = int(input("ingresee el radio:"))
    area = pi*(radio*radio)
    print("la superficie del circulo es: ", round(area, 2))
except ValueError:
    print("Error en el ingreso de numeros")