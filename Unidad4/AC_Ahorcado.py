intentos = 0
palabra = "casa".upper()
oculta = "-"
for i in range(len(palabra)):
        oculta += "-"
        
while intentos < 6 and oculta != palabra:
    
        
    letra = input("Ingrese una letra: ").upper()
    nueva = ""
    
    for i in range(len(palabra)):
        if palabra[i] == letra:
            nueva += letra
        else:
            nueva += oculta[i]
    if nueva == oculta:
        intentos += 1
        
    oculta = nueva
    print("Palabra: ", oculta)
    print("Intentos: ", intentos, "/6")
if nueva == palabra:
    print("Adivinaste en: ",intentos,"intentos, la palabra completa es: ",nueva)
else:
    print("Te quedaste sin intentos, la palabra era: ",palabra)
