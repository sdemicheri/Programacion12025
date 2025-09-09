try:
   año = int(input("ponga el año en que nacio:"))
   mes = int(input("ponga el numero del mes en que nacio:"))
   dia = int(input("ponga el numero de el dia en que nacio:"))
   año2 = int(input("ponga el numero de este año:"))
   mes2 = int(input("ponga el numero de el mes de este año:"))
   dia2 = int(input("ponga el numero del dia de hoy:"))
   if(año2 < año):
        print("no me esperaba conocer un viajero del tiempo, vuelva a poner su fecha de nacimiento")
   elif( mes > mes2 or dia > dia2):
       edad1 = año2  - año - 1
       print("tu edad es:", edad1)
   else:
       edad2 = año2 - año
       print("tu edad es:", edad2)    
except ValueError:
    print("error")