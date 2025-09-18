acu = 0
cont = 0
acu2 = 0
for i in range (2):
    digito_A = int(input("poner un digito:"))
    cont += 1
    acu = cont * digito_A
    acu2 += acu

print(cont)
print(acu2)
L = acu2 % 2
D = acu2 / 2
print(D)
print(L)
s = 198 % 11
print(s)