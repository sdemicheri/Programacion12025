cadena = input("Ingrese una cadena: ")
contador_letras = 0

for i in range(len(cadena)):
    if cadena [i] != " " and cadena != ".":
        contador_letras += 1
    
print(contador_letras)