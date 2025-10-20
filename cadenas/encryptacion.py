frase= input()
fraseEncriptada=""

for i in range (len(frase)):
    if i%2==0 and i!=len(frase)-1:
        fraseEncriptada+=frase[i+1]
        fraseEncriptada+=frase[i]
    elif i%2==0 and i==len(frase)-1:
        fraseEncriptada+=frase[i]

print(fraseEncriptada)