try:
    numero = float(input("Ingresa un número del 0 al 10: "))

    if 0 <= numero <= 10:
        entero = numero // 1 
        decimal = (numero * 10) % 10
        if entero == 0:
            letras = "cero"
        elif entero == 1:
            letras = "uno"
        elif entero == 2:
            letras = "dos"
        elif entero == 3:
            letras = "tres"
        elif entero == 4:
            letras = "cuatro"
        elif entero == 5:
            letras = "cinco"
        elif entero == 6:
            letras = "seis"
        elif entero == 7:
            letras = "siete"
        elif entero == 8:
            letras = "ocho"
        elif entero == 9:
            letras = "nueve"
        elif entero == 10:
            letras = "diez"
        else:
            print("no esta definido")
        if decimal == 0:
            d = "cero"
        elif decimal == 1:
            d  = "uno"
        elif decimal == 2:
            d  = "dos"
        elif decimal == 3:
            d  = "tres"
        elif decimal == 4:
            d = "cuatro"
        elif decimal == 5:
            d = "cinco"
        elif decimal == 6:
           d = "seis"
        elif decimal == 7:
            d = "siete"
        elif decimal == 8:
            d = "ocho"
        elif decimal == 9:
            d = "nueve"
        elif decimal == 10:
            d = "diez"
        else:
            print("No esta definido")
        print(f"El número {numero} en letras es: {letras} coma {d}")
    else:
        print("El número no es válido, por favor ingresa un número entre 0 y 10.")

except ValueError:
    print("Error: El valor ingresado no es un número entero. Por favor, intenta de nuevo.")