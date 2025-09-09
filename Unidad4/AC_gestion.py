edad = int(input("Ingrese su edad: "))
nota_uno = int(input("Ingrese su primera nota: "))
nota_dos = int(input("Ingrese su segunda nota: "))
nota_tres = int(input("Ingrese su tercer nota: "))
promedio = (nota_uno + nota_dos + nota_tres) / 3
print(f"Promedio, {promedio:.2f}")
if edad == 18:
    print("Es mayor de edad ")
elif edad < 18:
    print("Es menor de edad ")
if promedio >= 9:
    print("El rendimiento es excelente ")
elif promedio >= 8:
    print("El rendimiento es muy bueno ")
elif promedio >= 7:
    print("El rendimiento es bueno ")
elif promedio >= 6:
    print("El rendimiento es regular ")
elif promedio < 6:
    print("El rendimiento es insuficiente")
if promedio >= 9 and edad == 18:
    print("Reconocimiento al mérito ")
elif promedio >= 8 and edad < 18:
    print("Beca de excelencia juvenil ")
elif promedio < 6:
    print("Requiere apoyo académico ")
