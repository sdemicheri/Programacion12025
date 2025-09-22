eleccion1=input("(Piedra, Papel o Tijera)")
eleccion2=input("(Piedra, Papel o Tijera)")
if eleccion1 == "piedra" and eleccion2 == "papel":
    print("Ganador: Papel")
elif eleccion1 == "tijera" and eleccion2 == "papel":
    print("Ganador: Tijera")
elif eleccion1 == "piedra" and eleccion2 == "tijera":
    print("Ganador: Piedra")
elif eleccion1 == "papel" and eleccion2 == "piedra":
    print("Ganador: Papel")
elif eleccion1 == "papel" and eleccion2 == "tijera":
    print("Ganador: Tijera")
elif eleccion1 == "tijera" and eleccion2 == "piedra":
    print("Ganador: Piedra")
elif eleccion1 == "tijera" and eleccion2 == "tijera":
    print("Empate")
elif eleccion1 == "piedra" and eleccion2 == "piedra":
    print("Empate")
elif eleccion1 == "papel" and eleccion2 == "papel":
    print("Empate")
else :
    print("Dato ingresado no valido")
