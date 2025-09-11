edad = int(input())

nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

promedio = (nota1 + nota2 + nota3) / 3


estado_edad = "mayor de edad" if edad >= 18 else "menor de edad"

if promedio >= 9:
    rendimiento = "Excelente"
elif promedio >= 8:
    rendimiento = "Muy Bueno"
elif promedio >= 7:
    rendimiento = "Bueno"
elif promedio >= 6:
    rendimiento = "Regular"
else:
    rendimiento = "Insuficiente"

beneficio = ""
if edad >= 18 and promedio >= 9:
    beneficio = "Reconocimiento al mérito"
elif edad < 18 and promedio >= 8:
    beneficio = "Beca de excelencia juvenil"
elif promedio < 6:
    beneficio = "Requiere apoyo académico"


print(f"Promedio : {promedio:.2f}")
print("Es", estado_edad)
print("Rendimiento:", rendimiento)
print(beneficio)