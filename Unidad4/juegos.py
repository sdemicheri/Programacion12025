
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
    while not ganador:
        jugador1= int(input("Jugador 1, elige tu opción (1-3): "))
        jugador2= int(input("Jugador 2, elige tu opción (1-3): "))
        if jugador1 == jugador2:
         print("Empate, jueguen de nuevo ")
        elif jugador1 == 1 and jugador2 == 3 or jugador1 == 2 and jugador2 == 1 or jugador1 == 3 and jugador2 == 2:
         print("Jugador 1 gana ")
         ganador = True
        else:
            print("Jugador 2 gana ")
            ganador = True
except ValueError:
    print("Ingresó un dato no válido. Por favor, intente de nuevo ")

#PREGUNTAS Y RESPUESTAS
try:
   print("Pongamos a prueba tu conocimiento")
   puntaje = 0
   print("Pregunta 1: ¿Cuál es la isla mas grande del planeta?")
   print("1) Islandia")
   print("2) Japón")
   print("3) Australia")
   print("4) Groenlandia")
   respuesta = int(input("Seleccione una opción "))
   if respuesta == 4:
      print("Correcto")
      puntaje += 1
   else:
      print("Respuesta incorrecta, la correcta era: Groenlandia")
   print("Pregunta 2: ¿Quién ganó el mundial 2002?")
   print("1) Brasil")
   print("2) Inglaterra")
   print("3) Francia")
   print("4) Alemania")
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
   if respuesta == 4:
      print("Correcto")
      puntaje += 1
   else:
      print("Respuesta incorrecta, la correcta era: Oro")
   if puntaje == 5:
      print("Respondiste correctamente a todas las preguntas. Excelente")
   elif puntaje >= 3 and puntaje <= 4:
      print("Respondiste casi todas. Muy bien")
   elif puntaje <= 1 and puntaje <= 3:
      print("Estuviste medio flojo, pero se puede mejorar. ¡Ánimo!")
   else:
      print("Biennn, solo te faltó acertar todas las preguntas...Casi.")
except ValueError:
   print("Ingresaste un dato no válido")
#ADIVINA EL NÚMERO
import random
try:
   print("Bienvenido a Adivina el número")
   print("La consola, tu archienemiga en este juego pensó un número del 1 al 20...¿te atreves a retarla?")
   numero_secreto = random.randint(1,20)
   intentos = 0
   adivinado = False
   while not adivinado:
      intento= int(input("Ingresa el número que pensaste: "))
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