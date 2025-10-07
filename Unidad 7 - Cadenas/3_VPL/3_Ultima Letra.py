cadena = input("Ingrese una cadena: ").lower()
contador = 0
for i in range(len(cadena)):
    if cadena [i] == cadena[-1]:
        contador += 1
print(contador)