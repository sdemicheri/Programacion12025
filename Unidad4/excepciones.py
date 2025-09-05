#Al probar el código que hice, no me deja dividir el numero 100.
#try:
    #numero = int(input("Ingrese un número: "))
    #if numero % 2 == 0:
    #    print("El número que ingresó se puede dividir")
   # else:
  #      print("El número que ingresó no se puede dividir")
#except ValueError:
 #   print("El dato que ingresó no es válido para el sistema")
try:
    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        print("Es divisible")
    else:
        print("No es divisible")

except ValueError:
    print("Los datos ingresados no son correctos")