try:
   año = int(input("Ponga el año en que nacio:"))
   mes = int(input("Ponga el numero del mes en que nacio:"))
   dia = int(input("Ponga el numero de el dia en que nacio:"))
   año2 = int(input("Ponga el numero de este año:"))
   mes2 = int(input("Ponga el numero de el mes de este año:"))
   dia2 = int(input("Ponga el numero del dia de hoy:"))
    
   if( año < 0 or dia <= 0 or mes < 0):
       print("Usted no ha nacido porfavor pase el condigo a alguien que si nacio")
   elif( año2 <= 0 or mes2 <= 0 or dia2 <= 0):
       print("No puede haber un dia mes año con ese numero, porfavor vuelva a poner los datos")
   elif( mes > 12 or mes2 > 12):
       print("No hay mes 13 o derivados porfavor vuelva a poner los datos")
   elif( dia > 31 or dia2 > 31):
       print("Los dias del mes no puede tener mas de 31 dias, porfavor vuelva a poner los datos")
   elif( año == 0 and mes == 0):
       dia3 = dia2 - dia
       print(f"Su bebe tiene {dia3} dias")
   elif( año == 0):
       mes3 = mes2 - mes
       print(f"Su bebe tiene {mes3} mes")
   elif(año2 < año):
        print("No me esperaba conocer un viajero del tiempo, vuelva a poner su fecha de nacimiento")
   elif( mes > mes2):
       edad1 = año2  - año - 1
       print("Tu edad es:", edad1)
   elif( mes == mes2 and dia > dia2):
       edad3 = año2  - año - 1
       print("Tu edad es:", edad3)
   else:
       edad2 = año2 - año
       print("Tu edad es:", edad2)    
except ValueError:
    print("No has puesto bien alguno de los datos, intentelo de nuevo")