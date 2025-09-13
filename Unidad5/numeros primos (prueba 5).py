N = int(input("ingrese un numero:"))
divisores = (2, 3, 4, 5, 6, 7, 8, 9, 10)
D = float(divisores)
if( N % D == 0):
    print("su numero no es primo")
else:
    print("su numero es primo")