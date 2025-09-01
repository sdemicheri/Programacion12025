PI = 3.1415
try:
   radio = int(input("Ingrese el radio: "))
except ValueError:
   print("Error en el ingreso de números")
else:
    area = PI(radio*radio)
    print("la superficie del circulo es: ", round, 2)
finally:
    print("Gracias por usar el programa")