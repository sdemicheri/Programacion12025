def ejemplo():
    col = 5
    fil = 3
    matriz = [[0]*col for i in range(fil)]
    matriz[1][1] = 99
    for f in range(fil):
        for c in range(col):
            print(matriz[f][c], end=" ")
        print()

# tabla pitagórica

def tabla_pitagorica():
    tabla = [[0]*11 for i in range(11)]
    for f in range(11):
        for c in range(11):
            tabla [f][c] = f*c
    for f in range(11):
        for c in range(11):
            if tabla[f][c] < 10:
                print(" ", end="")
            print(tabla[f][c], end=" ")
        print()

# Matriz ejercicio simple

def mes():
    matriz = [[0]*3 for i in range(3)]
    suma = 0
    for f in range(3):
        for c in range(3):
            matriz[f][c] = int(input("Ingrese un dato: "))
            suma += matriz[f][c]
    promedio = suma / 9

    mayores = 0
    for f in range(3):
        for c in range(3):
            if matriz[f][c] > promedio:
                mayores += 1
    print(mayores)

# Matriz de identidad.

def matriz_identidad():
    matriz = [[0]*10 for i in range(10)]
    n = int(input())
    for f in range(n):
        matriz[f][f] = 1
    for f in range(n):
        for c in range(n):
            print(matriz[f][c], end=" ")
        print()

# Anillo. Escribir un programa  que daba una matriz de numeros enteros y dimension mxn, permita sumar los elementos de todos los anillos y mostrarlos.
# Se deberán mostrar las sumas de los anillos desde afuera hacia adentro.
def cargar_matriz():
    matriz = [[0]*10 for i in range(10)]
    m = int(input("Filas: "))
    n = int(input("Columnas: "))

    for f in range(m):
        for c in range(n):
            matriz[f][c] = int(input("Ingrese un dato: "))
    return matriz, m, n
def sumar_anillos(matriz,m,n):
    if m < n:
        menor = m
    else:
        menor = n

    anillos = (menor + 1) // 2

    for a in range(anillos):
        suma = 0
        for c in range(a, n-a):
            suma += matriz[a][c]
            
        for f in range(a+1, m-a):
            suma += matriz[f][n-a-1]
        if m - a - 1 != a:
            for c in range(n - a - 2, a - 1, -1):
                suma += matriz[m - a - 1][c]
        if n - a - 1 != a:
            for f in range(m - a - 2, a, -1):
                suma += matriz[f][a]    
        print(suma)
def anillos_ac():
    matriz, m, n = cargar_matriz()
    sumar_anillos(matriz,m,n)


#Anillo ejemplo con la profesora
# SI ES IMPAR SE LE SUMA +1 AL NUMERO ENTERO AL DIVIDIRLO ENTRE 2

def ejemplo_anillo():

    d = int(input("Dimension de la matriz: "))
    m = [["0"]* d for i in range(d)]

    fila = 0
    columna = 0


    for i in range(d):
        m[fila][i] = 1
    fila = d - 1

    for i in range(d):
        m[fila][i] = 1


    for i in range(d):
        m[i][columna] = 1
    columna = d - 1

    for i in range(d):
        m[i][columna] = 1
    #Si es par

    if d % 2 == 0:
        anillo = d // 2 
        m[anillo][anillo] = 1
        m[anillo][anillo -1] = 1
        m[anillo - 1][anillo] = 1
        m[anillo -1][anillo -1] = 1
    else:
        anillo = d // 2
        m[anillo][anillo] = 1 


    for i in range(fila + 1):
        for j in range(columna + 1):
            print(m[i][j], end=" ")
        print()


# Matriz con palabras

def matriz_palabras():
    palabra = input("Ingrese una palabra: ").upper()

    invertida = ""

    for i in range(len(palabra)-1,-1,-1):   
        invertida += palabra[i]

    lon = len(palabra)
    matriz = [[" "]*lon for i in range(lon)]

    for i in range(lon):    #primera flia
        matriz[0][i] = palabra[i]

    for i in range(1, lon):   #primera columna
        matriz[i][0] = palabra[i]

    for i in range(lon):                #ultima flia
        matriz[lon-1][i] = invertida[i]

    for i in range(1, lon-1):       #ultima columna
        matriz[i][lon-1] = invertida[i]

    for i in range(lon):
        for j in range(lon):
            print(matriz[i][j], end=" ")
        print()

# ESTRELLA

def estrella():

    estrella = int(input("Dimension de la matriz: "))

    if estrella % 2 != 0:
        matriz = [[" "]*estrella for i in range(estrella)]
        centro = estrella // 2

        for i in range(estrella):
            matriz[centro][i] = "*"
            matriz[i][centro] = "*"
            matriz[i][i] = "*"
            matriz[i][estrella - i - 1] = "*"

        for i in range(estrella):
            for j in range(estrella):
                print(matriz[i][j], end=" ")
            print()
    else:
        print("El número debe ser impar.")

def main():
    print("---EJERCICIOS DE MATRICES---")
    print("1. Ejemplo")
    print("2. Tabla pitagórica")
    print("3. Matriz ejercicio simple")
    print("4. Matriz de identidad")
    print("5. Anillos (AC)")
    print("6. Ejemplo anillo")
    print("7. Matriz con palabras")
    print("8. Estrella")
    opcion = int(input("Opción: "))
    match opcion:
        case 1:
            ejemplo()
        case 2:
            tabla_pitagorica()
        case 3:
            mes()
        case 4:
            matriz_identidad()
        case 5:
            anillos_ac()
        case 6:
            ejemplo_anillo()
        case 7:
            matriz_palabras()
        case 8:
            estrella()
main()
