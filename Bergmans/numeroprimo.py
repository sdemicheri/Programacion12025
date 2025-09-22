N = int(input("Ingrese un número: "))

divisores = 0

if N <= 1:
    divisores = 1 

else:
    for i in range(2, N):
        if (N % i) == 0:
            divisores = divisores + 1 


if divisores == 0:
    print(f"El número {N} es primo.")
else:
    print(f"El número {N} no es primo.")