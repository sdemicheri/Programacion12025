#Solicitar al usuario que ingrese su AÑO,MES Y DÍA de nacimiento
anio_nacido = int(input("Ingrese el año de nacimiento:"))
mes_nacido = int(input("Ingrese el mes de nacimiento"))
dia_nacido = int(int("Ingrese el día de nacimiento"))

#Solicitar al usuario que ingrese su AÑO,MES Y DÍA acutual
anio_actual = int(input("Inggrese el año actual: "))
mes_actual = int(input("Ingrese el mes actual: "))
dia_actual = int(input("Ingrese el día actual: "))

if (anio_actual > anio_nacido):
    if (mes_actual < mes_nacido):
        edad = (dia_nacido - dia_actual)
        print("Los días restante son: ", edad, "Días")
    if (mes_actual > mes_nacido):
        edad = (dia_nacido - dia_actual) - 360
        print("Los días restante son: ", edad, "Días")
    if (mes_actual == mes_nacido):
        if (dia_actual < dia_nacido):
            edad = ()

else:
    print("ERROR. El año de nacido no puede ser mayor al año actual")