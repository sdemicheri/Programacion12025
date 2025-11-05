cadena_1 = "Nos vemos el viernes"
cadena_2 = ""

for i in range(len(cadena_1)-1,-1,-1):   # invertir cadena
    cadena_2 += cadena_1[i]

print(cadena_2)