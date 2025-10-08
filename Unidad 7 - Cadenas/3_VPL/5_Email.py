"""
En una empresa de servicios en línea, se necesita un programa que verifique si el correo electrónico 
ingresado por el usuarios es válido.
Un correo electrónico válido debe contener al menos un carácter antes del símbolo '@', un '@', 
y al menos un punto ('.') que separa el dominio de nivel superior (TLD, por sus siglas en inglés) 
del dominio de nivel inferior (SLD, por sus siglas en inglés). 
Además, se permite que haya un subdominio opcional, que también se separa por un punto.
"""
correo = input().lower()
contador_arroba = 0
posicion_arroba = 0
contador_puntos = 0
letras_antes_arroba = False
for i in range(0,len(correo)):
    if correo[i] == "@":
        contador_arroba += 1
        posicion_arroba = i
        for i in range (0,posicion_arroba): # COMPROBAR CARACTERES ANTES DE LA ARROBA (AL MENOS UNA LETRA DEBE HABER)
            if correo[i] != " " or correo[i] != ".":
                letras_antes_arroba = True
            else:
                letras_antes_arroba = False
    if correo[i] == ".":
        contador_puntos += 1
if contador_arroba == 1 and letras_antes_arroba == True and contador_puntos != 0 and correo[0] != " ":
    print("mail válido")
else:
    print("mail inválido")