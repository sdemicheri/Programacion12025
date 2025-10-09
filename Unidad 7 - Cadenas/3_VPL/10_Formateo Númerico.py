cadena = input()        #  33,916,828.12 SE INGRESA ASI
                        #  33.916.828,12 DEBE SALIR ASI
nueva_salida = ""
for i in range(len(cadena)):
    if cadena[i] != "," and cadena[i] != ".":
        nueva_salida += cadena[i]
    elif cadena[i] == ",":
        nueva_salida += "."
    if cadena[i] == ".":
        nueva_salida += ","
    
print(nueva_salida)