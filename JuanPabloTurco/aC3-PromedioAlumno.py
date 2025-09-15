edad=int(input())
nota1=int(input())
nota2=int(input())
nota3=int(input())
promedio=(nota1+nota2+nota3)/3
print(f"Promedio: {promedio:.2f}")
if edad>=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
if promedio<6:
    print("Rendimiento: Insuficiente")
    print("Requiere apoyo académico")
elif promedio>=9:
    print("Rendimiento: Excelente")
    if edad>=18:
        print("Reconocimiento al mérito")
    else:
        print("Beca de excelencia juvenil")
elif promedio>=8:
    print("Rendimiento: Muy Bueno")
    if edad<18:
        print("Beca de excelencia juvenil")
elif promedio>=7:
    print ("Rendimiento: Bueno")
elif promedio>=6:
    print("Rendimiento: Regular")