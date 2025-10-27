frase = input("Ingrese la frase: ").lower()
frase = frase+" "
palabra = ""
longitudPalabraMayor = 0
palabraMayor = ""

for i in range(len(frase)):
    if frase[i] == " ":
        if len(palabra) > longitudPalabraMayor:
            palabraMayor = palabra
            longitudPalabraMayor = len(palabra)
        palabra = ""
    else:
        palabra = palabra + frase[i]
print(palabraMayor)