N = int(input("ingrese un numero:"))
acu = 0
for i in range (N):
    acu += 1
    print(acu)
    while( acu < N):
        acu += 1
        print(acu)