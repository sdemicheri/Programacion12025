frase = input().lower()
contador = 0
for i in range(len(frase)):
    if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        contador += 1
print(contador)