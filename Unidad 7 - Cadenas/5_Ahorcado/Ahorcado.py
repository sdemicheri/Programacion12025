"""
Juego del "ahorcado"

Dos adolescentes, A y B, quieren jugar "al ahorcado" usando su computadora: 
el problema consiste en escribir un programa que les permita hacerlo. 
El juego consiste en lo siguiente: 
A escribe en el teclado una palabra de N letras (N <30). 
La palabra desaparece de la pantalla y B trata de encontrarla en, a lo sumo, 
K intentos. Al principio, una sucesión de N guiones ("--...-") aparece en pantalla. 
Cada vez que B escribe una letra que figura en la palabra elegida por A, 
la letra aparece en pantalla en su lugar correcto reemplazando los correspondientes guiones. 
Cada vez que B escribe una letra equivocada, la letra aparece en pantalla junto con todas las letras equivocadas 
que haya ingresado B hasta ese momento. 
Al cabo de cada intento, debe aparecer también en pantalla la cantidad de intentos hechos y las chances que aún le quedan a B. 
El juego termina si la palabra es encontrada o bien si se han hecho ya los K intentos permitidos. 
Para evitar la picardía de alguno de los jugadores es conveniente que el programa valide que A ha elegido una palabra usando sólo las letras que aparecen en el teclado 
(evitando, por ejemplo, los símbolos *, $, +, los números, el espacio en blanco) 
y que, al final del juego, muestre la palabra elegida por A, si es que B no ha logrado encontrarla.
"""
import os

palabra_real = input("\nIngrese una palabra: ").lower()
os.system(('cls'))

if palabra_real != "*" and palabra_real != "," and palabra_real != "$" and palabra_real != "+" and palabra_real != " " and palabra_real != "":
    print("-"*len(palabra_real))
    auxiliar = "-" * len(palabra_real)
    letra = ""
    intentos = 0
    letras = ""
    ganaste = False

    while palabra_real != 0 and letra != 0 and intentos < 7 and palabra_real != auxiliar:
        cadena_nueva = ""
        letra = input("\nIngrese una letra: ").lower()
        acerto = False

        for i in range(len(palabra_real)):

            if letra == palabra_real[i]:
                cadena_nueva += letra
                acerto = True   
            else:
                cadena_nueva += auxiliar[i]

        auxiliar = cadena_nueva

        if palabra_real == auxiliar:
            ganaste = True
        else:
            ganaste = False

        if acerto == False:
            intentos += 1
            print(f"\n{intentos} intentos hechos, te quedan {7-intentos} intentos")
            letras += letra
            print(f"\nletras erroneas hasta el momento: {letras}")
        
        else:
            if ganaste == True:
                print(f"GANASTE, la palabra es: {palabra_real}")
            else:
                print(f"\nPalabra formada hasta ahora: {cadena_nueva}")

    if intentos == 7:
        print("\nPERDISTE, SE TERMINARON LOS INTENTOS")
else:
    print("ERROR, ingrese una palabra")