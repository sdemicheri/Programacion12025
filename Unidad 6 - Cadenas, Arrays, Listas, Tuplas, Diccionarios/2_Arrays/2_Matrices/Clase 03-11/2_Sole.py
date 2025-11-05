palabra = input()

for i in range(len(palabra)):
    print(palabra[i],end=" ")

cantidad_espacios = (len(palabra)) - 2

for i in range(1,len(palabra)-1):
    print(palabra[i]," "*(cantidad_espacios),palabra[len(palabra)-1])

for i in range(len(palabra)-1,-1,-1):
    print(palabra[i],end=" ")