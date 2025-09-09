alumno = int(input("ponga la edad de el estudiante:"))
nota1 = int(input("ponga la primera nota:"))
nota2 = int(input("ponga la segunda nota:"))
not3 = int(input("ponga la tercera nota:"))
nota_final = (nota1 + nota2 + not3)/ 3
print("promedio:", nota_final)
if( alumno >= 18 ):
    print("el alumno es mayor de edad")
else:
    print("es menor de edad")

if( nota_final >= 9):
    print("Rendimiento: excelente")
elif( nota_final >= 8):
    print("Rendimiento: muy bueno")
elif( nota_final >= 7):
    print("Rendimiento: bueno")
elif( nota_final >= 6):
    print("Rendimiento: regular")
elif( nota_final < 6):
    print("Rendimiento: insuficiente")

if( nota_final >= 8 and alumno < 18):
    print("Beca de excelencia juvenil")
elif( nota_final >= 9 and alumno >= 18):
    print("Reconocimiento al mérito")
elif( nota_final <= 6):
    print("Requiere apoyo académico")