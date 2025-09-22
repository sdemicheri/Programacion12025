edad = int(input())
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

sumaNotas = nota1 + nota2 + nota3
promedio = sumaNotas / 3
print(f"Promedio: {promedio:.2f}")

if edad < 18:
 print("Es menor de edad")
elif edad >= 18:
 print("Es mayor de edad")

if promedio >= 9:
 print("Rendimiento: Excelente")
elif promedio >= 8:
 print("Rendimiento: Muy bueno")
elif promedio >= 7:
 print("Rendimiento: Bueno")
elif promedio >= 6:
 print("Rendimiento: Regular")
elif promedio <= 6:
 print("Rendimiento: Insuficiente")

if edad < 18 and promedio >= 8:
 print("Beca de excelencia juvenil")
elif edad >= 18 and promedio >= 9:
 print("Reconocimiento al mérito")
elif promedio < 6:
 print("Requiere apoyo académico")