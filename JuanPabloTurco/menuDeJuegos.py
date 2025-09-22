import random
fin=False
while fin==False:
    print("Bienvenido al menu, escribe un numero para elegir:")
    print("1 - Mayor/o/Menor")
    print("2 - Piedra, Papel o Tijera")
    print("3 - Adivinanza")
    print("0 - Cerrar el menu")
    juego=int(input())
    if juego==1:
        fin=False
        numeroInicial=random.randint(0,1000)
        puntos=0
        while fin==False:
            numeroNuevo=random.randint(0,1000)
            relacion = input(f"El siguiente número al azar será <<MAYOR!>> o <<MENOR!>> a {numeroInicial}? ")
            if relacion=="MAYOR!":
                if numeroNuevo>=numeroInicial:
                    puntos+=100
                    print("Correcto! se ha generado el numero", numeroNuevo)
                    numeroInicial=numeroNuevo
                else:
                    fin=True
                    print("Incorrecto! se ha generado el numero", numeroNuevo, ". Ha perdido ;(")
            elif relacion=="MENOR!":
                if numeroNuevo<=numeroInicial:
                    puntos+=100
                    print("Correcto! se ha generado el numero", numeroNuevo)
                    numeroInicial=numeroNuevo
                else:
                    fin=True
                    print("Incorrecto! se ha generado el numero", numeroNuevo, ". Ha perdido ;(")
            else:
                print("Ha introducido incorrectamente la relacion, probemos de nuevo.")
        print("Ha conseguido", puntos, (" puntos!"))
        input("Presiona enter para volver al menu...")
        fin=False


    elif juego==2:
        print(("Lamento comunicarle que este juego esta en construccion"))
        input("Presiona enter para volver al menu...")


    elif juego==3:
        print("Bienvenido al juego: ¡Adivina el numero!")
        print("Se ha generado un numero del 1 al 100. Podes adivinar cual es?")

        numeroSecreto = random.randint(1, 100)
        intentos = 0
        adivinado = False

        while adivinado==False:
            try:
                intento = int(input("Ingresa tu numero: "))
                intentos += 1

                if intento < 1 or intento > 100:
                    print("Por favor, elige un número entre 1 y 100.")
                elif intento < numeroSecreto:
                    print("Demasiado bajo. ")
                elif intento > numeroSecreto:
                    print("Demasiado alto.")
                else:
                    print(f"Correcto! El numero era {numeroSecreto}.")
                    print(f"Lo adivinaste en {intentos} intentos.")
                    adivinado = True
            except ValueError:
                print("Solo podes ingresar numeros.")

        input("Presiona enter para volver al menu...")


    elif juego==0:
        fin=True
    else:
        print("No hay una opcion con ese numero")
print("Gracias por jugar, volveremos a vernos!")
