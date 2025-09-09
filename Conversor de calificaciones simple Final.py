try:
    import math

    nota = float(input("Ingrese la calificación: "))
    calificacion = math.ceil(nota)
    if calificacion > 0 and calificacion <= 100:
        if calificacion < 60:
            print("Reprobado")
        elif calificacion >= 60 and calificacion < 80:
            print("Aprobado")
        elif calificacion >= 80 and calificacion < 100:
            print("Promocionado")
        elif calificacion == 100:
            print("Calificación Perfecta \nFelicitaciones!!")
    else:
        print("Ingrese los valores correctos.")

except ValueError:
    print("Vuelva a ingresar la calificación.")