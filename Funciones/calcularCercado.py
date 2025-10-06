"""
Función 11: calcularCercado(largo, ancho)
Descripción: Calcula el perímetro del terreno para saber cuántos metros lineales de cerco se necesitan para proteger la huerta.
Entrada:
largo: número decimal con el largo del terreno en metros
ancho: número decimal con el ancho del terreno en metros
Salida:
Retorna un número decimal con el perímetro en metros
Lógica requerida:
Calcular perímetro: 2 × (largo + ancho)
"""
def calcularCercado():
    try:
        largo = float(input("Ingrese el largo del terreno en metros: "))
        ancho = float(input("Ingrese el ancho del terreno en metros: "))
        perimetro_cercar = 2 * (largo + ancho)
        print("El perímetro del terreno es: ", perimetro_cercar)
        return perimetro_cercar
    except ValueError:
        print("Ingresó un dato no válido.")
