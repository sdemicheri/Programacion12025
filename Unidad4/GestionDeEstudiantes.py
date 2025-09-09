try:    
    edad = int(input())
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())

    promedio = (nota1 + nota2 + nota3)/3

    print (f"Promedio: {promedio:.2f}")

    if edad >= 18:
        print ("Es mayor de edad")
    else:
        print ("Es menor de edad")

    if promedio >= 9:
        rendimiento = "Excelente"
        print("Rendimiento:",rendimiento)
    elif promedio >= 8:
        rendimiento = "Muy Bueno"
        print("Rendimiento:",rendimiento)
    elif promedio >= 7:
        rendimiento = "Bueno"
        print("Rendimiento:",rendimiento)
    elif promedio >= 6:
        rendimiento = "Regular"
        print("Rendimiento:",rendimiento)
    elif promedio <6:
        rendimiento = "Insuficiente"
        print("Rendimiento:",rendimiento)

    if edad < 18 and promedio >= 8:
        print("Beca de excelencia juvenil")

    if edad >= 18 and promedio >= 9:
        print("Reconocimiento al mérito")

    if promedio <6:
        print("Requiere apoyo académico")

except ValueError: 
    ("Las notas no son validas")