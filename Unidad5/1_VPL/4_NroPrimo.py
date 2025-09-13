"""
Programa que determina si un número ingresado es primo o no.
"""
numero = int(input("Ingrese un número: "))
if numero == 2 or numero == 3:
    print ("Es primo")
elif numero == 0 or numero == 1:
    print ("No es primo")
else:
    if ((numero%2)!= 0) and ((numero%3)!= 0) and ((numero%4)!= 0):
        print("Es primo")
    else:
        print("No es primo")