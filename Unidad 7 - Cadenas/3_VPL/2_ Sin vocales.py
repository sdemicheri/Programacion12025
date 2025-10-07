cadena = input("Ingrese una cadena: ").lower()
cadena_sin_vocal = ""

for i in range(len(cadena)):
    if cadena[i] != 'a' and cadena[i] != 'e' and cadena[i] != 'i' and cadena[i] != 'o' and cadena[i] != "u":
        cadena_sin_vocal += cadena[i]

print(cadena_sin_vocal)