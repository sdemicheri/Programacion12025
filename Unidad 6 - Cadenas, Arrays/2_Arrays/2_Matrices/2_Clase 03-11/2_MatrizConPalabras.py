palabra = input()
longitud = len(palabra)
print()
print(palabra)

for i in range(1, longitud - 1):
    print(palabra[i], end="")
    print(" " * (longitud-2), end="")
    print(palabra[-(i + 1)])


for i in range(len(palabra)-1,-1,-1):
    print(palabra[i], end="")

print()