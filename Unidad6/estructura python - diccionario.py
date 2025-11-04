diccionario = {}

try:
    for i in range(3):
        cadena = input()
        espaniol,ingles = input().split()
        diccionario[espaniol] = ingles
    busqueda = input()
    print(diccionario[busqueda])
except KeyError:
    print("Palabra no encontrada")