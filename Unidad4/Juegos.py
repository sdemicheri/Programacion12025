eleccion="1"
while eleccion < "5" and eleccion >="1" :
    try :
        print("Bienvenido")
        print("1 (Menu Pricipal)")
        print("2 (Piedra,Papel o Tijeras)")
        print("3 (Preguntas)")
        print("4 (Par o Impar)")
        print("5 (Salir)")
        eleccion=input("Elija una opcion: ")
        while eleccion == "2":
            eleccion1=input("(Piedra, Papel o Tijera)")
            eleccion2=input("(Piedra, Papel o Tijera)")
            if eleccion1 == "Piedra" and eleccion2 == "Papel":
                print("Ganador: Papel")
            elif eleccion1 == "Tijera" and eleccion2 == "Papel":
                print("Ganador: Tijera")
            elif eleccion1 == "Piedra" and eleccion2 == "Tijera":
                print("Ganador: Piedra")
            elif eleccion1 == "Papel" and eleccion2 == "Piedra":
                print("Ganador: Papel")
            elif eleccion1 == "Papel" and eleccion2 == "Tijera":
                print("Ganador: Tijera")
            elif eleccion1 == "Tijera" and eleccion2 == "Piedra":
                print("Ganador: Piedra")
            elif eleccion1 == "Tijera" and eleccion2 == "Tijera":
                print("Empate")
            elif eleccion1 == "Piedra" and eleccion2 == "Piedra":
                print("Empate")
            elif eleccion1 == "Papel" and eleccion2 == "Papel":
                print("Empate")
            else :
                print("Dato ingresado no valido") 
            print("2 (Para seguir)")
            print("1 (Menu principal)")
            eleccion=input("Elija una opcion: ")
        while eleccion == "3":
            print("Bienvenido al Juego de Preguntas")
            puntos = 0
            print("¿Cuánto es 2 + 2?")
            print("1: 4")
            print("2: 6")
            print("3: 10")
            respuesta = input("Tu respuesta: ")
            if respuesta == "1":
                print("Correcto")
                puntos += 1
            else:
                print("Incorrecto, la respuesta era (1: 4).")
            print("¿De qué color es el cielo en un día despejado?")
            print("1: rojo")
            print("2: azul")
            print("3: blanco")
            respuesta = input("Tu respuesta: ")
            if respuesta == "2":
                print("Correcto")
                puntos += 1
            else:
                print("Incorrecto, era (2: azul).")
            print("¿Cuál es la capital de Argentina?")
            print("1: Buenos Aires")
            print("2: Cordoba")
            print("3: Mendoza")
            respuesta = input("Tu respuesta: ")
            if respuesta == "1":
                print("Correcto")
                puntos += 1
            else:
                print("Incorrecto, es (1: Buenos Aires).")
            print("¿Cuántos días tiene una semana?")
            print("1: 19")
            print("2: 1")
            print("3: 7")
            respuesta = input("Tu respuesta: ")
            if respuesta == "3":
                print("Correcto")
                puntos += 1
            else:
                print("Incorrecto, es (3: 7).")
            print("¿Qué planeta está más cerca del sol?")
            print("1: Mercurio")
            print("2: Venus")
            print("3: Jupiter")
            respuesta = input("Tu respuesta: ")
            if respuesta == "1":
                print("Correcto")
                puntos += 1
            else:
                print("Incorrecto, es (1: Mercurio).")
           
            print("Juego terminado")
            print(f"Tu puntaje final es: {puntos}/5")
            print("3 (Para seguir)")
            print("1 (Menu principal)")
            eleccion=input("Elija una opcion: ")
        while eleccion == "4":
            n = int(input("Ingresa un número: "))
            if n % 2 == 0:
                print("Es par")
            else:
                print("Es impar")
            print("4 (Para seguir)")
            print("1 (Menu principal)")
            eleccion=input("Elija una opcion: ")
        while eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5":
            print("DATO INGRESADO NO VALIDO")
            print("Bienvenido")
            print("1 (Menu Pricipal)")
            print("2 (Piedra,Papel o Tijeras)")
            print("3 (Preguntas)")
            print("4 (Par o Impar)")
            print("5 (Salir)")
            eleccion=input("Elija una opcion: ")
    except ValueError:
        print("Dato ingresado no valido")
print("Gracias")    