try:
   año = int(input("ponga el año en que nacio:"))
   mes = int(input("ponga el numero del mes en que nacio:"))
   dia = int(input("ponga el numero de el dia en que nacio:"))
   año2 = int(input("ponga el numero de este año:"))
   mes2 = int(input("ponga el numero de el mes de este año:"))
   dia2 = int(input("ponga el numero del dia de hoy:"))
   if( año == 0 and mes == 0):
       dia3 = dia2 - dia
       print(f"Su infante tiene {dia3} dias")
   elif( año == 0):
       mes3 = mes2 - mes
       print(f"su infante tiene {mes3} mese")
   elif(año2 < año):
        print("no me esperaba conocer un viajero del tiempo, vuelva a poner su fecha de nacimiento")
   elif( mes > mes2):
       edad1 = año2  - año - 1
       print("tu edad es:", edad1)
   elif( mes == mes2 and dia > dia2):
       edad3 = año2  - año - 1
       print("tu edad es:", edad3)
   else:
       edad2 = año2 - año
       print("tu edad es:", edad2)    
except ValueError:
    print("no has puesto bien alguno de los datos, intentelo de nuevo")