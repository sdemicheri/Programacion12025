import os
palabra=input().lower()
os.system('cls')
incognita="_"*len(palabra)
incognitaAuxiliar=""
intentosMax=7
intento=1
letrasUsadas=''
win=False

while intento<intentosMax and win==False:
    print("este sera su intento numero ", intento, "/", intentosMax)
    if intento!=1:
        print("Usaste: ", letrasUsadas, ". las repetidas se contaran igual, estate atento")
    letra=input("ingrese una letra: ").lower()
    letrasUsadas+=letra
    for i in range (len(palabra)):
        if letra==palabra[i] and incognita[i]=="_":
            incognitaAuxiliar+=palabra[i]
        else:
            incognitaAuxiliar+=incognita[i]
    incognita=incognitaAuxiliar
    incognitaAuxiliar=""
    print(incognita)
    if incognita==palabra:
        win=True
    intento+=1
    input("Aprete enter para continuar...")
if win==True:
    print("Ganaste!!")
else:
    print("Perdiste :(")