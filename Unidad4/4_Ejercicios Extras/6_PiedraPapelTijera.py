"""
Simular un piedra papel o tijera
"""
print ("¡JUGUEMOS piedra papel O tijera!")

print("Jugador 1, ingrese su nombre: ")
nombre_1 = input ()
print (f"{nombre_1} Escriba su jugada: -piedra -papel -tijera")
jugada_1 = input()

print("Jugador 2, ingrese su nombre: ")
nombre_2 = input ()
print (f"{nombre_2} Escriba su jugada: -piedra -papel -tijera")
jugada_2 = input()

if (jugada_1 == "piedra" or jugada_1 == "papel" or jugada_1 == "tijera") and (jugada_2 == "piedra" or jugada_2 == "papel" or jugada_2 == "tijera"):

     if jugada_1 == jugada_2:
      print(f"EMPATE, ambos eligieron {jugada_1}")
     elif (jugada_1 == "piedra" and jugada_2 == "tijera") or (jugada_1 == "papel" and jugada_2 == "piedra") or (jugada_1 == "tijera" and jugada_2 == "papel"):
      print(f"Gana {nombre_1} con {jugada_1} contra {nombre_2} con {jugada_2}")
     else:
      print(f"Gana {nombre_2} con {jugada_2} contra {nombre_1} con {jugada_1}")

else:
  print("Los datos ingresados en las jugadas no son validos")