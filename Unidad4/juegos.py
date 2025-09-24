#MENÚ DE JUEGOS
salir = False
while salir == False:
    print("------------------------")
    print("Bienvenido al menú principal")
    print("1) Piedra, papel o tijeras")
    print("2) Preguntas y respuestas")
    print("3) Adivina el número")
    print("4) Salir")
    print("------------------------")
    opcion = int(input("Elige una opcion del 1 al 4: "))
    if opcion == 1:
# PIEDRA, PAPEL O TIJERA
      try:
       print("------------------------")
       print("Bienvenidos a Piedra, Papel o Tijera ")
       print("Opciones: ")
       print("1 Piedra")
       print("2 Papel")
       print("3 Tijera")
       print("------------------------")
       ganador = False
       while ganador == False:
         jugador1= int(input("Jugador 1, elige tu opción (1-3): "))
         jugador2= int(input("Jugador 2, elige tu opción (1-3): "))
         if jugador1 < 1 or jugador1 > 3 and jugador2 < 1 or jugador2 > 3:
            print("Ingresó una opción incorrecta. Vuelva a intentarlo ")
         elif jugador1 == jugador2:
            print("Empate, jueguen de nuevo ")
         elif jugador1 == 1 and jugador2 == 3 or jugador1 == 2 and jugador2 == 1 or jugador1 == 3 and jugador2 == 2:
            print("Jugador 1 gana ")
            ganador = True
         else:
               print("Jugador 2 gana ")
               ganador = True
      except ValueError:
       print("Ingresó un dato no válido. Por favor, intente de nuevo ")
    elif opcion == 2:

   #PREGUNTAS Y RESPUESTAS
      try:
         print("------------------------")
         print("Pongamos a prueba tu conocimiento")
         print("------------------------")
         puntaje = 0
         print("Pregunta 1: ¿Cuál es la isla mas grande del planeta?")
         print("1) Islandia")
         print("2) Japón")
         print("3) Australia")
         print("4) Groenlandia")
         respuesta = int(input("Seleccione una opción "))
         if respuesta < 1 or respuesta > 4:
            print("Ingreso una respuesta incorrecta ")
            break
         elif respuesta == 4:
            print("Correcto")
            puntaje += 1
         else:
            print("Respuesta incorrecta, la correcta era: Groenlandia")
         print("Pregunta 2: ¿Quién ganó el mundial 2002?")
         print("1) Brasil")
         print("2) Inglaterra")
         print("3) Francia")
         print("4) Alemania")
         respuesta = int(input("Seleccione una opción "))
         if respuesta == 1:
            print("Correcto")
            puntaje += 1
         else:
            print("Respuesta incorrecta, la correcta era: Brasil")
         print("Pregunta 3: ¿Cuando llegó Cristóbal Colón a América?")
         print("1) 1492")
         print("2) 1453")
         print("3) 1500")
         print("4) 1473")
         respuesta = int(input("Seleccione una opción "))
         if respuesta == 1:
            print("Correcto")
            puntaje += 1
         else:
            print("Respuesta incorrecta, la correcta era: 1492")
         print("Pregunta 3: ¿Cuál es el río mas largo del mundo?")
         print("1) Missisippi")
         print("2) Amazonas")
         print("3) Nilo")
         print("4) Calamuchita")
         respuesta = int(input("Seleccione una opción "))
         if respuesta == 2:
            print("Correcto")
            puntaje += 1
         else:
            print("Respuesta incorrecta, la correcta era: Amazonas") 
         print("Pregunta 4: ¿Cuál es el planeta mas grande del sistema solar?")
         print("1) Neptuno")
         print("2) Saturno")
         print("3) Júpiter")
         print("4) Marte")
         respuesta = int(input("Seleccione una opción "))
         if respuesta == 3:
            print("Correcto")
            puntaje += 1
         else:
            print("Respuesta incorrecta, la correcta era: Júpiter")
         print("Pregunta 5: ¿Qué elemento de la tabla periódica es este: Au?")
         print("1) Plata")
         print("2) Cobre")
         print("3) Aluminio")
         print("4) Oro")
         respuesta = int(input("Seleccione una opción "))
         if respuesta == 4:
            print("Correcto")
            puntaje += 1
         else:
            print("Respuesta incorrecta, la correcta era: Oro")
         if puntaje == 6:
            print("Respondiste correctamente a todas las preguntas. Excelente")
         elif puntaje >= 3 and puntaje <= 5:
            print("Respondiste casi todas. Muy bien")
         elif puntaje <= 1 and puntaje <= 3:
            print("Estuviste medio flojo, pero se puede mejorar. ¡Ánimo!")
         else:
            print("Biennn, solo te faltó acertar todas las preguntas...Casi.")
      except ValueError:
         print("Ingresaste un dato no válido")
   #ADIVINA EL NÚMERO
    elif opcion == 3:
      import random
      try:
         print("------------------------")
         print("Bienvenido a Adivina el número")
         print("La consola, tu archienemiga en este juego pensó un número del 1 al 20...¿te atreves a retarla?")
         print("------------------------")
         numero_secreto = random.randint(1,20)
         intentos = 0 
         adivinado = False
         while adivinado == False:
            intento= int(input("Ingresa el número que pensaste: "))
            if intento < 0:
               print("Ingreso un dato no válido. Intente de nuevo")
            intentos += 1
            if intento == numero_secreto:
               print("¡Correcto! El número era ", numero_secreto)
               print("Lo conseguiste en", intentos,"intentos")
               adivinado = True
            elif intento < numero_secreto:
               print("El número secreto es mayor ")
            else:
               print("El número secreto es menor ")
      except ValueError:
         print("Dato no válido")
    elif opcion == 4:
      print("Gracias por jugar")
      salir = True