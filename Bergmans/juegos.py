# La variable de control principal para el bucle del menú se inicializa
menu_principal = "continuar" 

# El bucle principal del programa comienza aquí
# Continuará ejecutándose mientras la variable menu_principal sea igual a "continuar"
while menu_principal == "continuar":
    # Imprime un encabezado para el menú en la consola
    print("--- MENU DE JUEGOS ---")
    # Imprime la primera opción de juego
    print("1. Adivina el número (una sola oportunidad)")
    # Imprime la segunda opción de juego
    print("2. Piedra, Papel o Tijera (una sola ronda)")
    # Imprime la tercera opción de salir
    print("3. Salir")
    
    # Solicita al usuario que seleccione una opción y almacena su entrada en la variable 'opcion'
    opcion = input("Selecciona una opción (1-3): ")

    # Si el usuario eligió '1', el juego "Adivina el número" comienza.
    if opcion == '1':
        print("--- Adivina el número ---")
        # Establece el número secreto a adivinar.
        numero_a_adivinar = 5 
        print("Estoy pensando en un número entre 1 y 10.")
        intento_usuario = input("¿Qué número estoy pensando? ")
        
        # Se utiliza un bloque 'try, except' para manejar posibles errores si el usuario no ingresa un número válido.
        try:
            # Intenta convertir la cadena de entrada del usuario a un número entero.
            intento_numerico = int(intento_usuario)
            # Comprueba si la suposición del usuario es correcta.
            if intento_numerico == numero_a_adivinar:
                # Si es correcta, se imprime este mensaje.
                print("¡Correcto! Adivinaste el número 5.")
            # Si es demasiado baja, se ejecuta este bloque.
            elif intento_numerico < numero_a_adivinar:
                # Imprime un mensaje de "demasiado bajo".
                print("Incorrecto. Demasiado bajo.")
            # Si es demasiado alta (la única otra posibilidad), se ejecuta este bloque.
            else:
                # Imprime un mensaje de "demasiado alto".
                print("Incorrecto. Demasiado alto.")
        # Si la conversión 'int()' falla (por ejemplo, el usuario escribió "abc"), este bloque captura el 'ValueError'.
        except ValueError:
            # Imprime un mensaje de error para una entrada no válida.
            print("Entrada no válida. Por favor, ingresa un número.")

    # Si el usuario eligió '2', el juego "Piedra, Papel o Tijera" comienza.
    elif opcion == '2':
        print("¡JUGUEMOS PIEDRA PAPEL O TIJERA!")

        
       
        jugada_1 = input(" escriba su jugada (piedra, papel, tijera): ")

        
       
        jugada_2 = input( "escriba su jugada (piedra, papel, tijera): ")
            
        if (jugada_1 in ["piedra", "papel", "tijera"]) and (jugada_2 in ["piedra", "papel", "tijera"]):
                if jugada_1 == jugada_2: 
                    print(f"EMPATE, ambos eligieron {jugada_1}")
               
                elif (jugada_1 == "piedra" and jugada_2 == "tijera") or \
                    (jugada_1 == "papel" and jugada_2 == "piedra") or \
                    (jugada_1 == "tijera" and jugada_2 == "papel"):
                    print(f" {jugada_1} contra {jugada_2}.")
                
                else:
                    print(f"GANA  con {jugada_2} contra {jugada_1}.")
        else:
                print("Los datos ingresados en las jugadas no son válidos.")

    # Si el usuario eligió '3', el programa saldrá.
    elif opcion == '3':
        #mensaje de despedida.
        print("¡Hasta la próxima!")
        # Cambia la variable de control a "salir", lo que hará que el bucle 'while' principal termine.
        menu_principal = "salir"
    
    # Maneja opciones no válidas.
    else:
        # Imprime un mensaje de error para una elección no válida.
        print("Opción no reconocida. Por favor, elige 1, 2 o 3.")

    # Este bloque se ejecuta si el usuario no eligió salir.
    if menu_principal == "continuar":
        # Informa al usuario que la ronda del juego ha terminado.
        print("--- Fin de ronda. Presiona Enter para volver al menú principal... ---")
        # Pausa el programa, esperando que el usuario presione la tecla Enter antes de que el bucle principal comience de nuevo.
        input()