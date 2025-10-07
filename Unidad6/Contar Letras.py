frase = input().lower()
contador = 0

for i in range(len(frase)):
    if frase[i] != " ":
        contador += 1
print(contador)