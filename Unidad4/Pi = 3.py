Pi = 3.1415
try:
 radio = int(input("ingrese el radio:"))
except ValueError:
 print("error en el ingreso de numeros")
else: 
 area = Pi*(radio*radio)
 print("la suoerficie del circulo es: ", round(area, 2))
finally:
 print ("Gracias por utilizar el programa")