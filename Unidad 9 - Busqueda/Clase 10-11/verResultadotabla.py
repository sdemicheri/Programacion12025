archivoTabla = open("C:\\Users\\Rodo\\Documents\\Python\\2025\\2 - Programación I\\Repositorio\\Programacion12025\\Unidad 9 - Busqueda\\EJERCICIO\\tablaMultiplicar.txt","r")

try:
    entrada1 = int(input())   # se ingresan los 2 nros del usuario como enteros, si no es int, se ejecuta el try except
    entrada2 = int(input())  
    nro1 = str(entrada1)  # se convierten en caracteres para compararlos con los de la tabla
    nro2 = str(entrada2)

    contenido = archivoTabla.readlines()  # guardo todo el contenido del txt

    for i in range(100):
        cadena = contenido[i].strip() # guardo cada 1 linea x iteracion( sin el \n)
        subcadena = cadena.split() # quito los espacios
        if (subcadena[0] == nro1 and subcadena[1] == nro2): # comparo los caracteres q ingreso usuario con los de la tabla
            print(f"El resultado de {subcadena[0]}x{subcadena[1]} es: {subcadena[2]}")

except ValueError:
    print("ERROR: Debe ingresar un número")  # si no ingresa un número entero imprimo el error
 
finally:
    archivoTabla.close()