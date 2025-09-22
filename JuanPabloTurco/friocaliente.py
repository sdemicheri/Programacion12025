import random
print("Bienvenido al juego: ¡Adivina el numero!")
print("Se ha generado un numero del 1 al 100. Podes adivinar cual es?")

numeroSecreto = random.randint(1, 100)
intentos = 0
adivinado = False

while adivinado==False:
    try:
        intento = int(input("Ingresa tu numero: "))
        intentos += 1

        if intento < 1 or intento > 100:
            print("Por favor, elige un número entre 1 y 100.")
        elif intento < numeroSecreto:
            print("Demasiado bajo. ")
        elif intento > numeroSecreto:
            print("Demasiado alto.")
        else:
            print(f"Correcto! El numero era {numeroSecreto}.")
            print(f"Lo adivinaste en {intentos} intentos.")
            adivinado = True
    except ValueError:
        print("Solo podes ingresar numeros.")

input("Presiona enter para volver al menu...")