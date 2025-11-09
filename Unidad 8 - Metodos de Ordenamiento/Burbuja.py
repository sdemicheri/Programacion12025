vector = [80,10,50,5,1,13,77]

contarCiclos = 0
for i in range(len(vector)-1):
    for j in range(len(vector)-1):
        contarCiclos += 1
        if vector[j] > vector[j+1]:
            auxiliar = vector[j]
            vector[j] = vector[j+1]
            vector[j+1] = auxiliar

print(vector)
print("Cantidad de ciclos: ",contarCiclos)
