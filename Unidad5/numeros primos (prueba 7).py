N = int(input("ingrese un numero:"))
acu = 2
if( N % acu != 0):
    while(N > acu):
        acu += 1
        div = N / acu
        if( div == 0):
            print("su numero no es primo")
else:
    print("su numero es primo")