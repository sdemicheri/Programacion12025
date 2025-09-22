numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
divisoresNumero1 = 0
divisoresNumero2 = 0

for divisor in range(1, numero1):
    if numero1 % divisor == 0:
        divisoresNumero1 += divisor
for divisor in range(1, numero2):
    if numero2 % divisor == 0:
        divisoresNumero2 += divisor
if divisoresNumero1 == numero2 and divisoresNumero2 == numero1:
    print("Son amigos!!")
else:
    print("No son amigos :(")