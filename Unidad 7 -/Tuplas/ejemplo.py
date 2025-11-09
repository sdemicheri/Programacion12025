mi_tupla = (1, "dos", [3.33, "cuatro"], (5,0,6))

print(mi_tupla[3][0]) # imprime 5.0

# CASTING
lista_1 = list(mi_tupla)
print(lista_1) # ahora es con corchetes y es modificable (menos la tupla)

a, b, c, d  = mi_tupla
print(c) # imprime el tercer elemento que es: [3.33, "cuatro"]