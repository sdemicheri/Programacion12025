import os
try:
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
except:
    print("NO SE PERMITEN NUMEROS")