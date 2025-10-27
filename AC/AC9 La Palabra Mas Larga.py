frase = input("Ingrese la frase: ").lower()
palabra = ""
cantidadLetras = 0

for i in range(len(frase)):
    if frase[i] == " ":
        espacio = i
        for i in range(espacio, len(frase)):
            palabra += frase[i]
        print(palabra)