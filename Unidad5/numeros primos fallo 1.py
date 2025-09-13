N = int(input("ingrese un numero:"))
acu = 1
for i in range (9):
    acu += 1
    div = N / acu
    if ( N % acu == 0):
        print("lo lograste")