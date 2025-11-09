vector = [80,10,50,5,1,13,77]

contarCiclos = 0

for i in range(len(vector)):
    auxiliar = vector[i]
    k = i - 1
    sw = False
    while not sw and (k >= 0):
        contarCiclos += 1
        if auxiliar < vector[k]:
            vector[k+1] = vector[k]
            contarCiclos += 1
            k -= 1
        else:
            sw = True
    vector[k+1] = auxiliar

print(vector)
print("Cantidad de ciclos: ",contarCiclos)