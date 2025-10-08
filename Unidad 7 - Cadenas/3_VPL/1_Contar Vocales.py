cadena = input("Ingrese una cadena: ").lower()

contador_vocales = 0

for i in range(len(cadena)):
    if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u":
        contador_vocales += 1
print(contador_vocales)