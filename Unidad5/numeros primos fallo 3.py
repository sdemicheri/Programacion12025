N = int(input("ingrese un numero:"))
acu = 1
for i in range (N):
    acu += 1
    if ( acu == N and N % acu == 0 ):
        print("su numero es primo")
    elif( N % acu == 0):
        print("su numero no es primo")
        break