vector = [80,10,50,5,1,13,77]

contarCiclos = 0

i = 1
for i in range(0,len(vector)-1):
    contarCiclos += 1
    auxiliar = vector[i]
    k = i
    for j in range(i+1,len(vector)):
        if vector[j] < auxiliar:
            auxiliar = vector[j]
            k = j
    vector[k] = vector[i]
    vector[i] = auxiliar

print(vector)
print("Cantidad de ciclos: ",contarCiclos)