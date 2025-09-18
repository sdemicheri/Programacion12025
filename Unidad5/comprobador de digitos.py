acu = 0
cont = 0
acu2 = 0
for i in range (9):
    digito_A = int(input("poner un digito (no poner el ultimo digito):"))
    cont += 1
    acu = cont * digito_A
    acu2 += acu

if( acu2 % 11 == 2):
    print("Verficado")
else:
    print("No verificado")