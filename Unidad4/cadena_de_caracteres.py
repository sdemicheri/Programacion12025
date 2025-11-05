def contar_vocales():
    frase = input ("Ingrese una frase: ")
    vocales = ""
    for i in range(len(frase)):
        if frase[i].lower() == "a" or frase[i].lower() == "e" or frase[i].lower() == "i" or frase[i].lower() == "o" or frase[i].lower() == "u":
            vocales = vocales + frase[i]
    print(len(vocales))


def sin_vocales():
    cadena = input("Ingrese una frase: ")
    consonantes = ""
    for i in range(len(cadena)):
        if cadena[i].lower() != "a" and cadena[i].lower() != "e" and cadena[i].lower() != "i" and cadena[i].lower() != "o" and cadena[i].lower() != "u":
            consonantes = consonantes + cadena[i]
    print(consonantes)

def ultima_letra_repetida():
    palabra = input("Ingrese una frase: ")
    ultima = palabra[-1]
    letra_repetida = 0
    for i in range(len(palabra)):
        if palabra [i].lower() == ultima.lower():
            letra_repetida += 1
    print(letra_repetida)

def contar_letras():
    palabra = input("Ingrese una frase: ")
    palabra_sin_espacio = 0
    for i in range(len(palabra)):
        if palabra[i] != " ":
            palabra_sin_espacio += 1
    print(palabra_sin_espacio)

def contar_palabras():
    frase = input("Ingrse una frase: ")
    palabras = 1
    for i in range(len(frase)):
        if frase[i] == " ":
            palabras += 1
    print(palabras)

def url():
    url = input("Ingrese la URL: ")
    posicion = 0

    for i in range(len(url)):
        if url[i] == "/":
            posicion = i + 1

    for i in range(len(url)-1):
        if url[i] == "/" and url[i+1] == "/": 
            posicion1 = i
    print(url[posicion1 + 2:posicion])

def palabra_mas_larga():
    frase1 = input("Ingrese la primer frase ")
    frase2 = input("Ingrese la segunda frase ")
    if len(frase1) ==  len(frase2):
        print(frase1) and print(frase2)
    elif len(frase1) > len(frase2):
        print(frase1)
    else:
        print(frase2)

def encriptar():
    cadena = input("Ingrese una frase: ")
    posicion = ""

    for i in range (0,len(cadena),2):
        if len(cadena) > i + 1:
            posicion += cadena[i + 1]
        posicion += cadena[i]
        
    print(posicion)

def mensaje():
    original = input()
    oculto = ""
    for i in range(len(original)):
        if i == 0: 
            oculto = oculto + original[i]  
        if original[i] == " ":          #Primer letra
            oculto = oculto + original[i+1]
    print(oculto)

def formato_numerico():
    total = input()
    sin_coma = ""
    for i in range(len(total)):
        if total[i] == " ":
            sin_coma += "."
        else:
            sin_coma += total[i]
    print(sin_coma)

def risas_digitales():
    risa = input("Ingrese la risa: ")
    vocales = ""
    for i in range(len(risa)):
        if risa[i] == "a" or risa[i] == "e" or risa[i] == "i" or risa[i] == "o" or risa[i] == "u":
            vocales += risa[i]
    invertida = ""
    for i in range(len(vocales)-1,-1,-1):
        invertida += vocales[i]
        if invertida == vocales:
            print("S")
        else:
            print("N")

def oracion_danzante():
    oracion = input("Ingrese la oración: ")
    danzante = " "
    mayuscula = True
    for i in range(len(oracion)):
        if oracion[i] == " ":
            danzante += " "
        else:
            if mayuscula == True:
                danzante += oracion[i].upper()
                mayuscula = False
            else:
                danzante += oracion[i].lower()
                mayuscula = True
    print(danzante,end="")

#AC 9 Palabra mas larga
def palabra_mas_larga():
    frase = input("")

    palabra = ""
    mas_larga = ""

    for i in range(len(frase)):
        if frase[i] != " ":
            palabra += frase[i]
        else:
            if len(palabra) > len(mas_larga):
                mas_larga = palabra
            palabra = ""

    if len(palabra) > len(mas_larga):
        mas_larga = palabra

    print(mas_larga)

def main():
    print("---EJERCICIOS---")
    print("1. Contar vocales")
    print("2. Sin vocales")
    print("3. Última letra repetida")
    print("4. Contar letras")
    print("5. Contar palabras")
    print("6. URL")
    print("7. Palabra más larga")
    print("8. Encriptar")
    print("9. Mensaje")
    print("10. Formato numérico")
    print("11. Risas digitales")
    print("12. Oración danzante")
    print("13. Palabra más larga (AC)")
    opcion = int(input("Opción: "))
    match opcion:
        case 1:
            contar_vocales()
        case 2:
            sin_vocales()
        case 3:
            ultima_letra_repetida()
        case 4:
            contar_letras()
        case 5:
            contar_palabras()
        case 6:
            url()
        case 7:
            palabra_mas_larga()
        case 8:
            encriptar()
        case 9:
            mensaje()
        case 10:
            formato_numerico()
        case 11:
            risas_digitales()
        case 12:
            oracion_danzante()
        case 13:
            palabra_mas_larga()
main()