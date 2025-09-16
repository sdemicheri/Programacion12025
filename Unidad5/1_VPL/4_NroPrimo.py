"""
Identifique si un número N ingresado es primo o no
"""
numero = int(input("Ingrese un numero o '0' para finalizar: "))

while numero != 0 and numero > 0:
    numero = int(input("Ingrese un numero o '0' para finalizar: "))
    for i in range(2,numero):
        if (numero % i+1 != 0):
            print("Es primo")
        else:
            print("No es primo")
















"""
numero = int(input("Ingrese un número: "))
if numero == 2 or numero == 3:
    
elif numero == 0 or numero == 1:
    print ("No es primo")
else:
    if ((numero%2)!= 0) and ((numero%3)!= 0) and ((numero%4)!= 0):
        print("Es primo")
    else:
        print("No es primo")
"""