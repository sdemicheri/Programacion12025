PI = 3.1415
try:
   radio = float(input("Ingrese el radio: "))
except ValueError:
   print("Error en el ingreso de números")
else:
    area = PI* (radio)**2
    print(f"la superficie del circulo es: {area:.2f}")
finally:
    print("Gracias por usar el programa")