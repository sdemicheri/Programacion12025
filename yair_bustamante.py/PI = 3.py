PI = 3.1415
try:

    radio = int(input("Ingrese el radio: "))
    area = PI *(radio*radio)
    print("La superficie es: ", round(area, 2))
except ValueError:
    print("Error en el ingreso de datos")
