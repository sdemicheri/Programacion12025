import random
fin=False
numeroInicial=random.randint(0,1000)
puntos=0
while fin==False:
    numeroNuevo=random.randint(0,1000)
    relacion = input(f"El siguiente número al azar será <<MAYOR!>> o <<MENOR!>> a {numeroInicial}? ")
    if relacion=="MAYOR!":
        if numeroNuevo>=numeroInicial:
            puntos+=100
            print("Correcto! se ha generado el numero", numeroNuevo)
            numeroInicial=numeroNuevo
        else:
            fin=True
            print("Incorrecto! se ha generado el numero", numeroNuevo, ". Ha perdido ;(")
    elif relacion=="MENOR!":
        if numeroNuevo<=numeroInicial:
            puntos+=100
            print("Correcto! se ha generado el numero", numeroNuevo)
            numeroInicial=numeroNuevo
        else:
            fin=True
            print("Incorrecto! se ha generado el numero", numeroNuevo, ". Ha perdido ;(")
    else:
        print("Ha introducido incorrectamente la relacion, probemos de nuevo.")
print("Ha conseguido", puntos, (" puntos!"))
input("Presiona enter para volver al menu...")