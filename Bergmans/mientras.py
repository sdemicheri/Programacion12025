contador = 0
numero = 0

while numero >= 0:
    
    numero = int(input("Ingresa un número (ingresa uno negativo para terminar): "))
    
   
   
    if numero >= 0:
        contador = contador + 1

print("Se ingresaron", contador, "números no negativos.")