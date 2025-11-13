"""
Identifique si un número N ingresado es primo o no
"""
numero = int(input("Ingrese un numero o '0' para finalizar: "))
es_primo = True

if numero < 2:
    es_primo = False
elif numero == 2:
    es_primo = True
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
if es_primo == True:
    print("Es primo")
else:
    print("No es primo")