#Set

def ejemplo_set():
    lista = input("Ingrese una lista de números ingresados: ").split()
    s= set(lista)
    print(len(s))

def diccionario():

    diccionario={}
    for i in range(3):
        cadena = input()
        espaniol, ingles = cadena.split()
        diccionario[espaniol] = ingles
    print(diccionario)
    try:
        busqueda=input()
        print(diccionario[busqueda])
    except KeyError:
        print("La palabra no se encuentra en el diccionario.")
def main():
    print("Ejercicios con listas, tuplas, sets y diccionarios")
    print("1. Ejemplo con set")
    print("2. Ejemplo con diccionario")
    opcion = int(input("Opcion: "))
    match opcion: 
        case 1:
            ejemplo_set()
        case 2:
            diccionario()
main()