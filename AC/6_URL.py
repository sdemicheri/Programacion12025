url = input("Ingresa la url: ").lower()
nueva_url = ""
contador_barra = 0
posicion_barra = 0

for j in range(len(url)):
    if url[0] == "h":
        for i in range(8,len(url)):
            if url[i] == "/":
                posicion_barra = i
        for i in range (8,posicion_barra+1):
            nueva_url += url[i]
    elif url[0] == "f":
        for i in range(6,len(url)):
            if url[i] == "/":
                posicion_barra = i
        for i in range (6,posicion_barra+1):
            nueva_url += url[i]

print(nueva_url)