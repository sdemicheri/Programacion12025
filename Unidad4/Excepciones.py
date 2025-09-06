try:
    
    numero = int(input())
    if numero % 2 == 0:
        print("Es divisible")
    else:
        print("No es divisible")

except ValueError:
    print("Los datos ingresados no son correctos")