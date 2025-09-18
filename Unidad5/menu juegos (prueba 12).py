try:
 print("**********BIENVENIDO AL MENU**********")
 print("")
 print("")
 print("")
 print("-Opciones:")
 print("1 - piedra papel o tijera (2 jugadores)")
 print("2 - preguntados")
 print("3 - adivina la palabra")
 J = int(input("ingrese un numero para poner un juego:"))
 if( J == 1 ):
   print("+Bienvenido a piedra papel o tijera+")
   print("")
   print("-Reglas: usted tiene que selccionar entre 3 movimientos: PIEDRA, PAPEL o TIJERA")
   print("y ganarle a al jugador 2 en 3 turnos y viceversa")
   print("")
   cont_1 = 0
   cont_2 = 0
   for i in range (3):
     jugada_1 = input("Jugador numero 1 ingrese su jugada: ")
     jugada_2 = input("jugador numero 2 ingrese su jugada: ")
     print("")
     if( jugada_1 != "PIEDRA" or jugada_1 != "PAPEL" or jugada_1 != "TIJERA" or jugada_2 != "PIEDRA" or jugada_2 != "PAPEL" or jugada_2 != "TIJERA"):
       print("no han puesto la jugada en mayuscula, por ello a ambos se les quitara un punto en este turno")
       print("")
     elif( jugada_1 == "PIEDRA"  and jugada_2 == "PAPEL"):
       print("✊ vs ✋")
       print("Punto para el jugador 2")
       print("")
       cont_2 += 1
     elif( jugada_1 == "PAPEL"  and jugada_2 == "PIEDRA"):
       print("✋ vs ✊")
       print("Punto para el jugador 1")
       print("")
       cont_1 += 1
     elif( jugada_1 == "TIJERA" and jugada_2 == "PIEDRA"):
       print("✌️ vs ✊")
       cont_2 += 1
       print("Punto para el jugador 2")
       print("")
     elif( jugada_1 == "PIEDRA" and jugada_2 == "TIJERA"):
       print("✊ vs ✌️")
       cont_1 += 1
       print("Punto para el jugador 1")
       print("")
     elif( jugada_1 == "TIJERA" and jugada_2 == "PAPEL"):
       print("✌️ vs ✋")
       cont_1 += 1
       print("Punto para el jugador 1")
       print("")
     elif( jugada_1 == "PAPEL" and jugada_2 == "TIJERA"):
       print("✋ vs ✌️")
       print("Punto para el jugador 2")
       print("")
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
   print("")
   print("-Reglas: Elige una de las categorias y responde correctamente las preguntas")
   print("(Las reglas deben seleccionarse si o si en mayuscula)")
   print("")
   print("categorias: HISTORIA, CINE, DEPORTES, MUSICA")
   print("")
   puntos = 0
   categoria = input("Elige una de las categoria: ")
   if( categoria == "HISTORIA"):
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("En que año se acabo la segunda guerra mundia ")
     print("A) 1945")
     print("B) 1978")
     print("C) 1991")
     print("D) 1914")
     r1 = input("Respuesta seleccionada:")
     if( r1 == "A"):
      print("")
      print("correcto")
      puntos += 1
     else: 
       print("")
       print("incorrecto")

     print("")
     print("     ????? ")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")
     print("¿Cómo se llamó y dónde se firmó la declaración de independencia de Argentina?")
     print("A) Declaración de independencia del Virreinato del Río de La Plata, firmada el 19 de abril de 1810 en Buenos Aires")
     print("B) Solemne independencia de la República Argentina, firmada el 18 de septiembre de 1810 en Santiago del Estero")
     print("C) Acta de independencia de las Provincias Unidas en Sudamérica, firmada el 9 de julio de 1816 en San Miguel de Tucumán")
     print("D) Declaración independentista de las Provincias del Cono Sur, firmada el 25 de agosto de 1825 en Santa Fe")
     r2 = input("Respuesta seleccionada:")
     if( r2 == "C"):
       print("")
       print("Correcto")
       puntos += 1
     else:
       print("incorrecto")
 
     print("")
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("¿Quien fue prócer de la independencia, importante líder de la Guerra Gaucha y Gobernador de Salta desde 1815 a 1821?")
     print("A) Bartolomé Mitre")
     print("B)Domingo Faustino Sarmiento")
     print("C) Juan José Castelli")
     print("D) Martín Miguel de Güemes")
     r3 = input("Respuesta seleccionada:")
     if( r3 == "D"):
       print("")
       print("Correcto")
       puntos += 1
     else:
       print("")
       print("incorrecto")

     if( puntos == 3):
       print("")
       print("Resultado")
       print("3/3")
       print("Puntuacion perfecta")
     elif( puntos == 2):
       print("")
       print("Resultado:")
       print("2/3")
       print("Muy bien")
     elif( puntos == 1):
       print("")
       print("Resultado:")
       print("1/3")
       print("Mejor suerte la proxima")
     else:
       print("")
       print("Resultado:")
       print("0/3")
       print("Falta estudiar, vuelva a la secundaria")
   elif( categoria == "CINE"):
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("¿Quién fue el director de la trilogía original de El Señor de los Anillos?")
     print("A) James Cameron")
     print("B) George Lucas")
     print("C) Peter Jackson")
     print("D) Ridley Scott")
     r4 = input("Respuesta seleccionada:")
     if( r4 == "C"):
       print("")
       print("Correcto")
       puntos += 1
     else:
       print("")
       print("Incorrecto")
    
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("¿En qué año se estrenó la primera película de Harry Potter Harry Potter y la piedra filosofal")
     print("A) 2005")
     print("B) 2001")
     print("C) 1999")
     print("D) 2003")
     r5 = input("Respuesta seleccionada:")
     if( r5 == "B"):
       print("")
       print("Correcto")
       puntos += 1
     else:
       print("")
       print("Incorrecto")

     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("¿Qué película ganó el Óscar a Mejor Película en 1994?")
     print("A) Titanic")
     print("B) Forrest Gump")
     print("C) Gladiador")
     print("D) El silencio de los inocentes")
     r6 = input("Respuesta seleccionada:")
     if( r6 == "B"):
       print("")
       print("Correcto")
       puntos += 1
     else:
       print("")
       print("Incorrecto")
       
     if( puntos == 3):
       print("")
       print("Resultado:")
       print("3/3")
       print("Puntuacion perfecta")
     elif( puntos == 2):
       print("")
       print("Resultado:")
       print("2/3")
       print("Mucho cine")
     elif( puntos == 1):
       print("")
       print("Resultado:")
       print("1/3")
       print("Mejor suerte la proxima")
     else:
       print("")
       print("Resultado:")
       print("0/3")
       print("Usted no es un cinefilo para nada")
   elif( categoria == "DEPORTES"):
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("¿Qué país ganó el primer Mundial de Fútbol en 1930?")
     print("A) Brasil")
     print("B) Alemania")
     print("C) Uruguay")
     print("D) Argentina")
     r7 = input("Respuesta seleccionada:")
     if ( r7 == "C"):
       print("")
       print("Correcto")
       puntos +=1
     else:
       print("")
       print("Incorrecto")

     print("")
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("¿Quién tiene el récord de más títulos de Grand Slam en tenis masculino (hasta 2023)?")
     print("A) Roger Federer")
     print("B) Novak Djokovic")
     print("C) Rafael Nadal")
     print("D) Pete Sampras")
     r8 = input("Respuesta seleccionada:")
     if( r8 == "B"):
       print("")
       print("Correcto")
       puntos += 1
     else:
       print("")
       print("Incorrect")

     print("")
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("¿En qué ciudad se celebraron los Juegos Olímpicos de 1992?")
     print("A) Los Ángeles")
     print("B) Seúl")
     print("C) Barcelona")
     print("D) Atenas")
     r9 = input("Respuesta seleccionada:")
     if( r9 == "C"):
       print("")
       print("correcto")
       puntos += 1
     else:
       print("")
       print("Incorrecto")

     if( puntos == 3):
       print("")
       print("Resultado:")
       print("3/3")
       print("Puntuacion perfecta")
     elif( puntos == 2):
       print("")
       print("Resultado:")
       print("2/3")
       print("Que buen deportista")
     elif( puntos == 1):
       print("")
       print("Resultado:")
       print("1/3")
       print("Mejor suerte la proxima")
     else:
       print("")
       print("Resultado:")
       print("0/3")
       print("Usted nunca ha practido ningun deporte ¿verdad?")
   elif( categoria == "MUSICA"):
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("¿Qué banda británica lanzó el álbum The Dark Side of the Moon en 1973?")
     print("A) The Beatles")
     print("B) Pink Floyd")
     print("C) Led Zeppelin")
     print("D) The Rolling Stones")
     r10 = input("Respuesta seleccionada:")
     if( r10 == "B"):
       print("")
       print("Correcto")
       puntos += 1
     else:
       print("")
       print("Incorrecto")

     print("")
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")  
     print("¿Quién es conocida como la “Reina del Soul”?")
     print("A) Tina Turner")
     print("B) Diana Ross")
     print("C) Aretha Franklin")
     print("D) Whitney Houston")
     r11 = input("Respuesta seleccionada:")
     if( r11 == "C"):
       print("")
       print("Correcto")
       puntos += 1
     else:
       print("")
       print("Incorrecto")

     print("")
     print("     ?????")
     print("   ?       ? ")  
     print("  ?   ^_^   ?")  
     print("   ?       ?")   
     print("    ??????")
     print("¿Cuál fue el primer videoclip emitido en MTV en 1981?")
     print("A) “Billie Jean” – Michael Jackson")
     print("B) “Like a Virgin” – Madonna")
     print("C) “Radio Ga Ga” – Queen")
     print("D) “Video Killed the Radio Star” – The Buggles")
     r12 = input("Respuesta seleccionada:")
     if( r12 == "D"):
       print("")
       print("Correcto")
       puntos += 1
     else:
       print("")
       print("Incorrecto")
        
     if( puntos == 3):
       print("")
       print("Resultado:")
       print("3/3")
       print("Puntuacion perfecta")
     elif( puntos == 2):
       print("")
       print("Resultado:")
       print("2/3")
       print("Le sabes a la musico")
     elif( puntos == 1):
       print("")
       print("Resultado:")
       print("1/3")
       print("Mejor suerte la proxima")
     else:
       print("")
       print("Resultado:")
       print("0/3")
       print("No tenes oido capo, haceptalo")
except ValueError:
  print("lol")