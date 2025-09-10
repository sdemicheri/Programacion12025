"""
Simular un piedra papel o tijera
"""
print ("¡JUGUEMOS PIEDRA PAPEL O TIJERA!")

#DATOS DEL jUGADOR 1
print("Jugador 1, ingrese su nombre: ")
nombre_1 = input ()
print (f"{nombre_1} Escriba su jugada de la siguiente forma: piedra, papel tijera")
jugada_1 = input()

#DATOS DEL JUGADOR 2
print("Jugador 2, ingrese su nombre: ")
nombre_2 = input ()
print (f"{nombre_2} Escriba su jugada de la siguiente forma: piedra, papel tijera")
jugada_2 = input()

#COMPROBAR QUE EL NOMBRE NO ESTE VACÍO
if nombre_1 == "" or nombre_2 == "":
  print("El nombre no puede estar vacío")

else: #COMPROBAR QUE LA JUGADA SEA VALIDA
  if (jugada_1 == "piedra" or jugada_1 == "papel" or jugada_1 == "tijera") \
    and (jugada_2 == "piedra" or jugada_2 == "papel" or jugada_2 == "tijera"):
      
      if jugada_1 == jugada_2: #EN CASO DE UN EMPATE
        print(f"EMPATE, ambos eligieron {jugada_1}")

          #EN CASO DE QUE EL JUGADOR 1 GANE
      elif (jugada_1 == "piedra" and jugada_2 == "tijera") or \
        (jugada_1 == "papel" and jugada_2 == "piedra") or \
          (jugada_1 == "tijera" and jugada_2 == "papel"):
        print(f"GANA {nombre_1} con {jugada_1} contra {nombre_2} con {jugada_2}")

        #SI NO GANA EL JUGADOR 1 Y TAMPOCO HUBO EMPATE EL ÚNICO RESULTADO VALIDO ES QUE GANE EL JUGADOR 2
      else:
        print(f"GANA {nombre_2} con {jugada_2} contra {nombre_1} con {jugada_1}")
  else:
    print("Los datos ingresados en las jugadas no son validos")
    # POR SI LA COMPROBACIÓN DE JUGADA VALIDA RESULTA NEGATIVA