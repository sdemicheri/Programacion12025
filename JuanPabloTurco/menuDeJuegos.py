import random
fin=False
reiniciar=False
puntosTotales=0
juegosInit=0
try:
    while fin==False:
        print("Bienvenido al menu, escribe un numero para elegir:")
        print("1 - Mayor/o/Menor")
        print("2 - Resuelve la Incognita")
        print("3 - Adivinanza")
        print("0 - Cerrar el menu")
        juego=int(input())
        if juego==1:                    #MAYOR O MENOR
            juegosInit+=1
            fin=False
            numeroInicial=random.randint(0,1000)
            puntos=0
            print("El programa tomara numeros entre el 1 y el 1000")
            while fin==False:
                numeroNuevo=random.randint(0,1000)
                relacion = input(f"El siguiente número al azar será 'MAYOR!' o 'MENOR!' a {numeroInicial}? ")
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
            puntosTotales+=puntos
            input("Presiona enter para volver al menu...")
            fin=False


        elif juego==2:             #RESOLVER INCOGNITA
            juegosInit+=1
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
            puntosTotales+=puntos
            input("Presiona enter para volver al menu...")
            fin=False


        elif juego==3:             #ADIVINANZA
            juegosInit+=1
            print("Bienvenido al juego: Adivinanza!")
            print("Se ha generado un numero del 1 al 100. Podes adivinar cual es?")

            numeroSecreto = random.randint(1, 100)
            intentos = 0
            adivinado = False
            puntos=500
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
                        puntos=puntos-(intentos*50)
                        if puntos<0:
                            puntos=0
                        print("Ha conseguido", puntos, (" puntos!"))
                        puntosTotales+=puntos
                except ValueError:
                    print("Solo podes ingresar numeros.")

            input("Presiona enter para volver al menu...")


        elif juego==0:       #SALIR DEL MENU
            fin=True
        else:
            print("No hay una opcion con ese numero")
except ValueError:
    print("Ingrese solo numeros enteros. Porfavor reinicie el codigo")
    reiniciar=True
if  reiniciar==False:
    print("Ha conseguido", puntosTotales, " puntos jugando ", juegosInit, "partidas!")
    print("Gracias por jugar, volveremos a vernos!")
