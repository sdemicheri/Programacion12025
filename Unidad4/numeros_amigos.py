a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
suma_a = 0
for i in range (1,a,1):
    if a % i == 0:
        suma_a += i
suma_b = 0
for k in range (1,b,1):
    if b % k == 0:
        suma_b += k
if suma_a == b and suma_b == a:
    print("Los números ingresados son amigos")
else:
    print("Los números ingresados no son amigos")
