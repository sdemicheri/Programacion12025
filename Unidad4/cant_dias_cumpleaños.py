a_actual=int(input("ingrese el año actual: "))
mes_actual=int(input("ingrese mes actual: "))
dia_actual=int(input("ingrese dia actual: "))

a_nacimiento=int(input("ingrese el año de nacimiento: "))
mes_nacimiento=int(input("ingrese mes de nacimiento: "))
dia_nacimiento=int(input("ingrese el dia de nacimiento: "))
if (a_actual > a_nacimiento):
    if (mes_actual ==  mes_nacimiento):
        if dia_nacimiento > dia_actual:
            dias_restantes = (dia_nacimiento - dia_actual)
            print("Los dias restantes son: ", dias_restantes)
        else:
            dias_restantes = 365 - (dia_actual - dia_nacimiento)
            print("Los dias restantes son: ", dias_restantes)
    else:
        if mes_nacimiento > mes_actual:
            mes_restante = mes_nacimiento - mes_actual 
            print("Los meses restantes son: ", mes_restante)
            dias = mes_restante * 30
            if dia_nacimiento > dia_actual:
                dias_restantes = dia_nacimiento - dia_actual
                print("Los dias para mi cumpleaños son: ", dias + dias_restantes)
            else:
                dias_restantes = dia_actual - dia_nacimiento
                print("Los dias para mi cumpleaños son: ", dias - dias_restantes)
           
        else:
            mes_restantes = 12 - (mes_actual - mes_nacimiento)
            print("Los meses restantes son: ", mes_restantes)
