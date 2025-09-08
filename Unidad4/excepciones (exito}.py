try:
    numero = int(input("ingrese en un numero:"))
    if( numero % 2 == 0):
        print("es divisible")
    else:
        print("no es divisble")
except ValueError:
    print("los datos ingresados no son correctos")