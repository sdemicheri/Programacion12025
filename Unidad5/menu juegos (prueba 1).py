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
   print("-Regñas: usted tiene que selccionar entre 3 movimientos: PIEDRA, PAPEL o TIJERA")
   print("y ganarle a al jugador 2 en 3 turnos y viceversa")
   jugada_1 = input("Jugador numero 1 ingrese su jugada:")
   jugada_2 = input("jugador numero 2 ingrese su jugada:")
   cont_1 = 0
   cont_2 = 0
   for i in range (3):
     if( jugada_1 == "PIEDRA"  and jugada_2 == "PAPEL"):
       print("✊ vs ✋")
       print("Punto para el jugador 2")
       cont_2 += 1
     elif( jugada_1 == "PAPEL"  and jugada_2 == "PIEDRA"):
       print("✋ vs ✊")
       print("Punto para el jugador 1")
       cont_1 += 1
     elif( jugada_1 == "TIJERA" and jugada_2 == "PIEDRA"):
       print("✌️ vs ✊")
       cont_2 += 1
       print("Punto para el jugador 2")
     elif( jugada_1 == "PIEDRA" and jugada_2 == "TIJERA"):
       print("✊ vs ✌️")
       cont_1 += 1
       print("Punto para el jugador 1")
     elif( jugada_1 == "TIJERA" and jugada_2 == "PAPEL"):
       print("✌️ vs ✋")
       cont_1 += 1
       print("Punto para el jugador 1")
     elif( jugada_1 == "PAPEL" and jugada_2 == "TIJERA"):
       print("✋ vs ✌️")
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
    
except ValueError:
  print("lol")