try:
    numero=int(input())
    numerodivisible=numero%2
    if numerodivisible == 0:
        print("Es divisible")
    else :
        print("No es divisible")
except ValueError:
    print("Los datos ingresados no son correctos")
