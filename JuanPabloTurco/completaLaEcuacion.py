import random
puntos=0
fin=False
while fin==False:
    numero1=random.randint(1,10)
    numero2Secreto=random.randint(1,10)
    producto=numero1*numero2Secreto
    print("Que numero multiplicado por ", numero1, " da como producto: ", producto)
    numeroElegido=int(input("Responde con un entero: "))
    if numero2Secreto==numeroElegido:
        print("Correcto!")
        puntos+=100
        input("presione enter para seguir completando incognitas")
    else:
        print("Incorrecto!")
        fin=True
print("Ha conseguido", puntos, (" puntos!"))
input("Presiona enter para volver al menu...")
