frase = input().lower()
acumulador = 0

for i in range(len(frase)):
    if frase[i] == " ":
        separacion = i
        acumulador += 1
if acumulador < len(frase):
    print(acumulador+1)
    