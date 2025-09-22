import random
fin=False
numeroInicial=829
puntos=0
while fin==False:
    numeroNuevo=696
    relacion = input(f"El siguiente número al azar será <<MAYOR!>> o <<MENOR!>> a {numeroInicial}? ")
    if relacion=="MAYOR!":
        if numeroNuevo>=numeroInicial:
            puntos+=100
            print("Correcto! se ha generado el numero", numeroNuevo)
        else:
            fin=True
            print("Incorrecto! se ha generado el numero", numeroNuevo, ". Ha perdido ;(")
    else:
        if numeroNuevo<=numeroInicial:
            puntos+=100
            print("Correcto! se ha generado el numero", numeroNuevo)
        else:
            fin=True
            print("Incorrecto! se ha generado el numero", numeroNuevo, ". Ha perdido ;(")
    numeroInicial=numeroNuevo
print("Ha conseguido", puntos, (" puntos!"))