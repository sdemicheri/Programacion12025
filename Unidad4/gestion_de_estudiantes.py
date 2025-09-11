# ENTRADA
edad=int(input("ingrese edad:"))
nota1=float(input("ingrese nota1:" ))
nota2=float(input("ingrese nota2:" ))
nota3=float(input("ingrese nota3:" ))

#PROCESO
promedio=(nota1+nota2+nota3)/3
print(f"promedio:{promedio:.2f}")

if edad >= 18:
    print("Es mayor de edad")
elif  edad <=18:
    print("Es menor que")


# clasificacion
if promedio >= 9:
    print("Excelente")
if promedio >= 8:
    print("Muy_Bueno")
elif promedio >=7:
    print("Bueno")
if promedio <= 6:
    print("Insuficiente")

# Beneficios especiales
if edad >=18 and promedio >= 8: 
    print("Beca de excelencia juvenil")
if edad >=18 and promedio >= 9: 
    print("Reconocimiento al mérito")
if promedio <=6: 
    print("Requiere apoyo académico")