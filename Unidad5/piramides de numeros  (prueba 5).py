n = int(input("ingrese un numero:"))
a = 0
for i in range (n):
    a = a + 1
    b = a + 1
    print(a, b)
    if( a == n or b == n):
        break