#Cada estudiante debe implementar UNA de las siguientes funciones:

#Función: aplicarDescuento()

#Responsable: Estudiante G
#Descripción: Aplica un descuento si el grupo es numeroso.

#Entrada: Monto total, cantidad de personas
#Salida: Retorna el monto con descuento aplicado
#Lógica: Usar condicionales:
#Si son 5 o más personas: 10% de descuento
#Si son 3 o 4 personas: 5% de descuento
#Si son menos de 3: sin descuento


#FUNCIONES
def Aplicar_descuento(monto_total, cantidad_personas):
    if cantidad_personas >=5: 
        descuento = monto_total*10/100
    elif cantidad_personas == 3 or cantidad_personas == 4: 
        descuento = monto_total*5/100
    elif cantidad_personas < 3:
        print("No hay descuento para esa cantidad de personas. Gracias por utilizarnos.")


cantidad_personas = int(input("Ingrese la cantidad de personas: "))
monto_total = float(input("Ingrese el monto total de lo gastado: "))
