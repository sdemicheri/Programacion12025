x = int(input("Ingrese primer numero amigo: "))
a = 0
for i in range (1,x):
    resto=x%i
    if resto == 0:
        print (i)
a += i
a = a+n

y = int(input("Ingrese segundo numero amigo: "))
b = 0
for i in range (1,y):
    resto=y%i
    if resto == 0:
        print (i)
b += i
b = b+n

if a == y and b == x:
    print("Son amiguis")
else:
    print("No son amiguis")