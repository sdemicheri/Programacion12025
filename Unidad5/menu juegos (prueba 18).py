try:
 print("**********BIENVENIDO AL MENU**********")
 print("")
 print("")
 print("")
 print("-Opciones:")
 print("1 - piedra papel o tijera (2 jugadores)")
 print("2 - preguntados")
 print("3 - adivina el numero")
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
   if( categoria != "HISTORIA" or categoria != "CINE" or categoria != "DEPORTES" or categoria != "MUSICA"):
     print("no ha puesto bien la categoria, porfavor vuelva a ejecutar el programa")
   elif( categoria == "HISTORIA"):
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
 elif( J == 3):
   print("---Bienvenidos a adivina el numero---")
   print("")
   print("Reglas: Debes advinar un numero cada ronda y la maquina te dira si lo adivinaste o no")
   print("")
   print("Ronda 1")
   Numero = 13
   usuario_advinando1 = 0
   intentos_maximos = 5
   puntos = 0
   while( usuario_advinando1 < intentos_maximos):
     print("")
     ad = int(input("ponga un numero:"))
     usuario_advinando1 += 1
     if( ad < Numero):
       print("el numero es mayor")
     elif( ad > Numero):
       print("el numero es menor")
     elif( ad == Numero):
       print("felicidades ganaste")
       puntos += 1
       break
   else:
     print("Perdiste la ronda 1")
      
   print(puntos)
     
   print("")
   print("Ronda 2")
   Numero2 = 122
   usuario_advinando2 = 0
   intentos_maximos = 5
   while( usuario_advinando2 < intentos_maximos):
     print("")
     ad = int(input("ponga un numero:"))
     usuario_advinando2 += 1
     if( ad < Numero2):
       print("el numero es mayor")
     elif( ad > Numero2):
       print("el numero es menor")
     elif( ad == Numero2):
       print("felicidades ganaste")
       puntos += 1
       break
   else:
     print("Perdiste la ronda 2")
 
   print(puntos)

   print("")
   print("Ronda 3")
   Numero3 = 57
   usuario_advinando3 = 0
   intentos_maximos = 5
   while( usuario_advinando3 < intentos_maximos):
     print("")
     ad = int(input("ponga un numero:"))
     usuario_advinando3 += 1
     if( ad < Numero3):
       print("el numero es mayor")
     elif( ad > Numero3):
       print("el numero es menor")
     elif( ad == Numero3):
       print("felicidades ganaste")
       puntos += 1
       break
   else:
     print("Perdiste la ronda 3")
   
   print(puntos)
   tres = 3
   dos = 2 
   uno = 1

   if(puntos == 3 and usuario_advinando1 <= 2 and usuario_advinando2 <= 2 and usuario_advinando3 <= 2):
     print("")
     print("Rondas completadas: 3/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Vaya!, tienes un talento sobrenatural en esto")
   elif( puntos == 3 and usuario_advinando1 == 3 and usuario_advinando2 <= 2 and usuario_advinando3 <= 2 or usuario_advinando1 <= 2 and usuario_advinando2 == 3 and usuario_advinando3 <= 2 or usuario_advinando1 <= 2 and usuario_advinando2 <= 2 and usuario_advinando3 == 3):
     print("")
     print("Rondas completadas: 3/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Bastante bien, pero no te conformes si crees poder mejorar")
   elif( puntos == 3 and usuario_advinando1 == 3 and usuario_advinando2 == 3 and usuario_advinando3 <= 2 or usuario_advinando1 <= 2 and usuario_advinando2 == 3 and usuario_advinando3 == 3 or usuario_advinando1 == 3 and usuario_advinando2 <= 2 and usuario_advinando3 == 3):
     print("")
     print("Rondas completadas: 3/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Nada mal, pero puedes hacerlo mejor")
   elif( puntos == 3 and usuario_advinando1 == 3 and usuario_advinando2 == 3 and usuario_advinando3 == 3):
     print("")
     print("Rondas completadas: 3/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Bien ahi, lo hiciste bien")
   elif( puntos == 3 and usuario_advinando1 >= 3 and usuario_advinando2 <= 2 and usuario_advinando3 <= 2 or usuario_advinando1 <= 2 and usuario_advinando2 >= 3 and usuario_advinando3 <= 2 or usuario_advinando1 <= 2 and usuario_advinando2 <= 2 and usuario_advinando3 >= 3):
     print("")
     print("Rondas completadas: 3/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Buen trabajo, pero aun te falta practica")
   elif( puntos == 3 and usuario_advinando1 >= 3 and usuario_advinando2 >= 3 and usuario_advinando3 <= 2 or usuario_advinando1 <= 2 and usuario_advinando2 >= 3 and usuario_advinando3 >= 3 or usuario_advinando1 >= 3 and usuario_advinando2 <= 2 and usuario_advinando3 >= 3):
     print("")
     print("Rondas completadas: 3/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Que un par de intentos extra en unas ronda no te desanimen, sigue intentando")
   elif( puntos == 3 and usuario_advinando1 > 3 and usuario_advinando2 > 3 and usuario_advinando3 > 3):
     print("")
     print("Rondas completadas: 3/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Bueno... almenos completaste todas las rondas")


   if(puntos == 2 and usuario_advinando1 <= 2 and usuario_advinando2 <= 2 or usuario_advinando2 <= 2 and usuario_advinando3 <= 2 or usuario_advinando1 <= 2 and usuario_advinando3 <= 2 ):
     print("")
     print("Rondas completadas: 2/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Eres bueno adivinando, lastima que hayas fallado una ronda")
   elif( puntos == 2 and usuario_advinando1 == 3 and usuario_advinando2 <= 2 or usuario_advinando2 == 3 and usuario_advinando1 <= 2 or usuario_advinando3 == 3 and usuario_advinando2 <= 2 or usuario_advinando3 <= 2 and usuario_advinando2 == 3 or usuario_advinando3 == 3 and usuario_advinando1 <= 2 or usuario_advinando3 <= 2 and usuario_advinando1 == 3):
     print("")
     print("Rondas completadas: 2/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Curioso resultado, pero hey, almenos tienes un gran mergen de mejor, no te rindas!")
   elif( puntos == 2 and usuario_advinando1 == 3 and usuario_advinando2 == 3 or usuario_advinando1 == 3 and usuario_advinando3 == 3 or usuario_advinando2 == 3 and usuario_advinando3 == 3):
     print("")
     print("Rondas completadas: 2/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Oh hola señor promedio, ¿seguis igual de tibio que siempre?")
   elif( puntos == 2 and usuario_advinando1 >= 3 and usuario_advinando2 <= 2 or usuario_advinando1 <= 2 and usuario_advinando2 >= 3 or  usuario_advinando2 <= 2 and usuario_advinando3 >= 3 or usuario_advinando2 >= 3 and usuario_advinando3 <= 2 or usuario_advinando1 <= 2 and usuario_advinando3 >= 3 or usuario_advinando1 >= 3 and usuario_advinando3 <= 3):
     print("")
     print("Rondas completadas: 2/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Esta bien, todos tenemos tropezones, sigue intentando")
   elif( puntos == dos and usuario_advinando1 >= 3 and usuario_advinando2 >= 3 or puntos == 2 and usuario_advinando1 >= 3 and usuario_advinando3 >= 3 or puntos == 2 and usuario_advinando2 >= 3 and usuario_advinando3 >= 3):
     print("")
     print("Rondas completadas: 2/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Ibas bien y te caiste Horriblemente, aun asi puedes volverlo a intenar")


   if(puntos == 1 and usuario_advinando1 <= 2 or usuario_advinando2 <= 2 or usuario_advinando3 <= 2):
     print("")
     print("Rondas completadas: 1/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Porfavor, vuelve a intentarlo, puedes mas que esto")
   elif( puntos == 1 and usuario_advinando1 == 3 or usuario_advinando2 == 3 or usuario_advinando3 == 3):
     print("")
     print("Rondas completadas: 1/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Loco, recapasita, no es tan dificil")
   elif( puntos == 1 and usuario_advinando1 > 3 or usuario_advinando2 > 3 or usuario_advinando3 > 3):
     print("")
     print("Rondas completadas: 1/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("No se como hiciste pero lograste ser horriblente desastroso en este juego")
     print("porfavor reconsidera estudiar mas y enderezar tu vida porque no puede ser que")
     print("alguien normal pierda en un juego tan facil")
   else:
     print("")
     print("Rondas completadas: 0/3")
     print("Numero de intentos en la ronda 1:", usuario_advinando1)
     print("Numero de intentos en la ronda 2:", usuario_advinando2)
     print("Numero de intentos en la ronda 3:", usuario_advinando3)
     print("Se sincero conmigo, ¿le diste este programa a tu hermanito pequeño?")
     print("¿Jugaste a esto con los ojos cerrados? o fallaste proposito para demostrar algo")
     print("porque sino no entiendo la razon de tal fracaso rotundo, no se suponia que perdieras")
     print("pero lo hiciste y estoy impactado, porfavor elige otro juego ya que es obvio que este")
     print("no es para ti")
except ValueError:
  print("No has puesto bien los valores en el menu o jugando algunos de los juegos.")
  print("porfavor vuelva a ejecutar el programa y asegurese de poner bien los valores esta vez")