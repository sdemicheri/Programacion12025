N = int(input("ingrese un numero:"))
acu = 2
while( N > acu):
    acu += 1
    if( N // acu == N and N % 1 == 0):
        print("su numero es primo")
    else:
        print("su numero no es primo")