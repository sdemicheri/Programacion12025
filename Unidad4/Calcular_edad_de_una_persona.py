

#Solicitar al usuario el año de nacimiento como número entero.
anio_nacido = int(input("Ingrese su año de nacimiento: "))
mes_nacido = int(input("Ingrese su mes de nacimiento: "))
dia_nacido = int(input("Ingrese el día de nacimiento: "))

#Solicitar al usuario el año actual como número entero.
anio_actual = int(input("Ingrese el año actual: "))
mes_actual = int(input("Ingrese el mes actual: "))
dia_actual = int(input("Ingrese el día actual: "))



if  (anio_actual > anio_nacido): # Calcular la edad de una persona que supera el año de vida
    if (mes_actual < mes_nacido): # La persona no llego a cumplir la edad
        edad = (anio_actual - anio_nacido - 1)
        print("Tu edad es: ", edad, "años" )
    if (mes_actual > mes_nacido): #La persona ya cumplió la edad
        edad = (anio_actual - anio_nacido)
        print("Tu edad es: ", edad, "años" )
    if (mes_actual == mes_nacido): # Si el mes actual es igual al mes de nacido la edad exacta se calcula con los días
        if (dia_actual >= dia_nacido):
            edad = (anio_actual - anio_nacido) # Cumpliria o ya cumplió los años
            print("Tu edad es: ", edad, "años" )
        if (dia_actual < dia_nacido): # Esta en el mes donde cumpliria la edad pero todavia no llegó el día
            edad = (anio_actual - anio_nacido - 1)
            print("Tu edad es: ", edad, "años" )
elif (anio_actual == anio_nacido): # calcula la edad de una persona que no supera el año de vida. Ejemplo: un bebé
    if (mes_actual > mes_nacido): # Se calcula la edad de alguien que tiene unos cuantos meses de vidad
     edad = (mes_actual - mes_nacido)
     print("Tu edad es: ", edad, "meses de nacido")
    elif (mes_actual == mes_nacido): # Se calcula la edad de alguien que todavia no supera el mes de vida
        if (dia_actual > dia_nacido):
         edad = (dia_actual - dia_nacido)
         print("Tu edad es:", edad, "días de nacido")
        else:
            print("ERROR. El día actual no puede ser menor al día de nacimiento ")
    else: 
        print("ERROR. El mes actual no puede ser menor al mes de nacido")
else:
    print("ERROR. El año de nacimiento no puede ser mayor al año actual")





    
    

    
    




  