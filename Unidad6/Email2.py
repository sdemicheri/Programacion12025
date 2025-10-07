email = input().lower()
contador = 0
posicionArroba = 0
correoValido = True

for i in range(len(email)):
    if email[i] == "@":
        contador += 1
        posicionArroba = i      
if contador != 1:
    correoValido = False

if posicionArroba == 0:
    correoValido = False
else:
    tieneCaracterAntes = False
    for i in range(posicionArroba):
        if email[i] != " " and email[i] != ".":
            tieneCaracterAntes = True
    if tieneCaracterAntes == False:
        correoValido = False

punto = False
for i in range(posicionArroba + 1, len(email)):
    if email[i] == ".":
        punto = True
if punto == False:
    correoValido = False

if correoValido == True:
    print("mail válido")
else:
    print("mail inválido")