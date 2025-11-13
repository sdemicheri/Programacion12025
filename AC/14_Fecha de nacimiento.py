try:
    cadena = input()
    if cadena == " " or cadena == "" or cadena == "-":
        print("Debe ingresar algun dato")
    else:
        if len(cadena) != 10 or cadena[2] != "/" or cadena[5] != "/":
            print("Formato Incorrecto")
        else:
            dia = ""
            mes = ""
            año = ""
            for i in range(0,2):
                dia += cadena[i]
            for i in range(3,5):
                mes += cadena[i]
            for i in range(6,len(cadena)):
                año += cadena[i]
            meses = {'01': "Enero", '02': "Febrero", '03': "Marzo", '04': "Abril", 
                    '05': "Mayo", '06': "Junio", '07': "Julio", '08': "Agosto", '09': "Septiembre",
                    '10': "Octubre", '11': "Noviembre", '12': "Diciembre"}
            print(f"Día: {dia}")
            print(f"Mes: {meses[mes]}")
            print(f"Año: {año}")
except KeyError:
    print("No existe el mes")