try:
    numero = input("ingrese un numero:")
    if( numero <= 0):
        print("su numero debe ser mayor a 0")
    elif( numero <= 100 or numero >= 1000):
        print("su numero debe ser de 3 cifras")
    elif( numero == numero [::-1] ):
        print("capicua")
    else:
        print("no es capicua")
except TypeError:
    print("error al ingresar los datos")