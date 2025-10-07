frase = input().lower()
fraseSinVocal = ""

for i in range(len(frase)):
    if frase[i] != 'a' and frase[i] != 'e' and frase[i] != 'i' and frase[i] != 'o' and frase[i] != 'u':
        fraseSinVocal += frase[i]

print(fraseSinVocal)