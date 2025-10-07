url = input().lower()
barra = 0
acumulador = 0

for i in range(8, len(url)):
    if url[i] == "/":
        barra = i
        acumulador += 1

for i in range(8, barra+1):
    print(url[i], end="")