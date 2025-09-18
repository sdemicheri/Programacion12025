try:
 print("**********BIENVENIDO AL MENU**********")
 print(":")
 print(":")
 print(":")
 print("-Opciones:")
 print("1 - piedra papel o tijera (2 jugadores)")
 print("2 - preguntados")
 print("3 - adivina la palabra")
 J = int(input("ingrese un numero para poner un juego:"))
 if( J == 1 ):
   print("+Bienvenido a piedra papel o tijera+")
   print(":")
   print("-Reglas: usted tiene que selccionar entre 3 movimientos: PIEDRA, PAPEL o TIJERA")
   print("y ganarle a al jugador 2 en 3 turnos y viceversa")
   print(":")
   cont_1 = 0
   cont_2 = 0
   for i in range (3):
     jugada_1 = input("Jugador numero 1 ingrese su jugada: ")
     jugada_2 = input("jugador numero 2 ingrese su jugada: ")
     print(":")
     if( jugada_1 == "PIEDRA"  and jugada_2 == "PAPEL"):
       print("✊ vs ✋")
       print("Punto para el jugador 2")
       print(":")
       cont_2 += 1
     elif( jugada_1 == "PAPEL"  and jugada_2 == "PIEDRA"):
       print("✋ vs ✊")
       print("Punto para el jugador 1")
       print(":")
       cont_1 += 1
     elif( jugada_1 == "TIJERA" and jugada_2 == "PIEDRA"):
       print("✌️ vs ✊")
       cont_2 += 1
       print("Punto para el jugador 2")
       print(":")
     elif( jugada_1 == "PIEDRA" and jugada_2 == "TIJERA"):
       print("✊ vs ✌️")
       cont_1 += 1
       print("Punto para el jugador 1")
       print(":")
     elif( jugada_1 == "TIJERA" and jugada_2 == "PAPEL"):
       print("✌️ vs ✋")
       cont_1 += 1
       print("Punto para el jugador 1")
       print(":")
     elif( jugada_1 == "PAPEL" and jugada_2 == "TIJERA"):
       print("✋ vs ✌️")
       print("Punto para el jugador 2")
       print(":")
       cont_2 += 1
     elif( jugada_1 == "PAPEL" and jugada_2 == "PAPEL"):
       print("✋ vs ✋")
       print("Empate")
     elif( jugada_1 == "PIEDRA" and jugada_2 == "PIEDRA"):
       print("✊ vs ✊")
       print("Empate")
     elif( jugada_1 == "TIJERA" and jugada_2 == "TIJERA"):
       print("✌️ vs ✌️")
       print("empate")
   if(cont_1 > cont_2):
      print("Ganador jugador 1")
   elif( cont_2 > cont_1):
      print("Ganador: jugador 2")
   else:
      print("Empate entre los dos jugadores")
   
 elif( J == 2):
   print("**Bienvenidos a preguntados**")
   print(":")
   print("-Reglas: Elige una de las categorias y responde correctamente las preguntas")
   print(":")
   print("categorias: HISTORIA, GEOGRAFIA, CINE, DEPORTES, MUSICA")
   print(":")
   puntos = 0
   categoria = input("Elige una de las categoria: ")
   if( categoria == "HISTORIA"):
     print("En que año se acabo la segunda guerra mundia ")
     print("A) 1945")
     print("B) 1978")
     print("C) 1991")
     print("D) 1914")
     r1 = input("Respuesta seleccionada:")
     if( r1 == "A"):
      print(":")
      print("correcto")
      puntos += 1
     else: 
       print(":")
       print("incorrecto")

     print("")
except ValueError:
  print("lol")