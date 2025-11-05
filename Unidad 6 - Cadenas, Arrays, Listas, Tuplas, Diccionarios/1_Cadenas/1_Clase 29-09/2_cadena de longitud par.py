"""
Pedir 5 cadenas y contar cuantas cadenas tienen longitud par
"""
contador_par = 0
for i in range(5):
    cadena_1 = input("Ingrese la cadena: ")
    if len(cadena_1) % 2 == 0:
        contador_par += 1
print ("Cantidad de cadenas con longitud par:",contador_par)