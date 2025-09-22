import random
numero_secreto = random.randint(1, 10)
intentos = 0

print("Hola vamos a jugar! yo elijo un numero y vos adivinas cual es!")
print("Estoy pensando en un número del 1 al 10. ¿Crees saber cual?")

while True:
    try:
        # Pedir número al jugador
        adivinanza = int(input("Ingresa tu número: "))
        intentos += 1
        
        if adivinanza < 1 or adivinanza > 10:
            print("Por favor, ingresa un número entre 1 y 10.")
            continue

        if adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta otra vez.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Intenta otra vez.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos")
            break
    except ValueError:
        print("Entrada inválida. Ingresa un número del 1 al 10.")
