edad=int(input())
nota1=int(input())
nota2=int(input())
nota3=int(input())
sumanota=nota1+nota2+nota3
promedio=sumanota/3
print("Promedio:",int(promedio))
if edad >= 18:
    print("Es mayor de edad")
else :
    print("Es menor de edad")
if promedio >= 9:
    print("Rendimiento: Excelente")
elif promedio >= 8:
    print("Rendimiento: Muy Bueno")
elif promedio >= 7:
    print("Rendimiento: Bueno")
elif promedio >= 6:
    print("Rendimiento: Regular")
elif promedio < 6:
    print("Rendimiento: Insuficiente")
if edad < 18 and promedio >= 8:
    print("Beca de excelencia juvenil")
elif edad >= 18 and promedio >= 9:
    print("Reconocimiento al mérito")
elif promedio < 6:
    print("Requiere apoyo académico")