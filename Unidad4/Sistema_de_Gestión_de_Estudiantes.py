#Crear un programa que:
#Pida edad y tres notas de un estudiante
# Calcule el promedio
#Determine si es mayor o menor de edad
#Clasifique según rendimiento académico:
#Excelente: >= 9
#Muy Bueno: >= 8
#Bueno: >= 7
#Regular: >= 6
#Insuficiente: < 6
#Otorgue beneficios especiales:
#Si es menor de edad y tiene promedio >= 8: "Beca de excelencia juvenil"
#Si es mayor de edad y tiene promedio >= 9: "Reconocimiento al mérito"
#Si tiene promedio < 6: "Requiere apoyo académico"

#Ejemplo:

#Entrada:

#18 #edad
#10 #nota1
#9 #nota1
#8 #nota1

#Salida:

#Promedio: 9
#Es mayor de edad
#Rendimiento: Excelente
#Reconocimiento al mérito

edad = int(input())
nota1 = int(input()) 
nota2 = int(input())
nota3 = int(input())
promedio = (nota1 + nota2 + nota3) / 3
print(f"Promedio:{promedio:.2f}")
if  edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
if promedio >= 9:
    print("Rendimiento: Excelente")
elif promedio >= 8:
    print("Rendimiento: Muy bueno")
elif promedio >= 7:
    print("Rendimiento: Bueno")
elif promedio >= 6:
    print("Rendimiento: Regular")
elif promedio < 6:
    print("Rendimiento: Insuficiente")
if (edad< 18) and (promedio >=8):
    print("Beca de excelencia juvenil")
elif (edad>= 18) and (promedio >=9):
    print("Reconocimiento al mérito")
elif (promedio < 6):
    print("Requiere apoyo académico")
    