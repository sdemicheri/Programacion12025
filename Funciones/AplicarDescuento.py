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
def aplicarDescuento(monto_total, cantidad_personas):
    montoConDescuento = 0
    if cantidad_personas >=5: 
        descuento = monto_total*10/100
        montoConDescuento = monto_total - descuento
    elif cantidad_personas == 3 or cantidad_personas == 4: 
        descuento = monto_total*5/100
        montoConDescuento = monto_total - descuento
    elif cantidad_personas < 3:
        montoConDescuento = monto_total
    return montoConDescuento

cantidad_personas = int(input("Ingrese la cantidad de personas: "))
monto_total = float(input("Ingrese el monto total de lo gastado: "))
resultado = aplicarDescuento (monto_total, cantidad_personas)
print(resultado)