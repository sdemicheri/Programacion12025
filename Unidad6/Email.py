email = input().lower()
contador = 0
posicionArroba = 0

for i in range(len(email)):
    if email[i] == "@":
        posicionArroba = i
        contador += 1
        if contador > 1 and contador == 0:
            correoValido = False

for i in range(posicionArroba):
    if email[i] != " " and email[i] != "." and email[i] != "":
        correoValido = True

for i in range(posicionArroba, len(email)):
    if email[i] == ".":
        correoValido = True

if correoValido == True:
    print("mail válido")
elif correoValido == False: 
    print("mail inválido")