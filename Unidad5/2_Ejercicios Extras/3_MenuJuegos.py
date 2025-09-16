#--- Código para mostrar el menú ---
print("-" * 20)
print("  MENÚ DE JUEGOS  ")
print("-" * 20)
print("\n")
print("1. Verdadero o Falso")
print("2. Adivina el Número")
print("3. [Nombre del tercer juego]")
print("\n")

opcion_elegida = input("Elige un juego (ingresa el número) o '0' para salir: ")

if opcion_elegida == "1":
    print(f"¡Elegiste Verdadero o Falso!")
elif opcion_elegida == "2":
    print(f"!Elegiste Adivina el número!")
elif opcion_elegida == "3":
    print(f"¡Elegiste ...!")
elif opcion_elegida == "0":
    print(f"Fin del programa")
else:
    print(f"Opcion no valida, por favor ingrese un numero del 1 al 3 o 0 para finalizar el programa")