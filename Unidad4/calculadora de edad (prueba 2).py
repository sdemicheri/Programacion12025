año = int(input("ponga el año en que nacio:"))
mes = int(input("ponga el numero del mes en que nacio:"))
dia = int(input("ponga el numero de el dia en que nacio:"))
año2 = int(input("ponga el numero de este año:"))
mes2 = int(input("ponga el numero de el mes de este año:"))
dia1 = int(input("ponga el numero del dia de hoy:"))
try:
    if(año2 < año):
        print("no sabia que teniamos un viajero del tiempo, vuelva a poner su fecha de nacimiento")
except ValueError:
    print("error")