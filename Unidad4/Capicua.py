try:
    numero = int(input("Ingrese un número de tres cifras: "))

    if numero < 0:
        print("El número que ingrese debe ser mayor a 0")
    elif numero < 100 or numero > 999:
        print("El número debe ser de tres cifras")
    else:
        primer_numero = numero // 100
        segundo_numero = numero % 10

        if primer_numero == segundo_numero:
            print("Es capicúa")
        else:
            print("No es capicúa")

except ValueError:
    print("Ingreso un dato no válido")