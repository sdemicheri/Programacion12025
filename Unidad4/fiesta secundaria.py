"""
ENTRADA:
TOTAL $ COMIDA
TOTAL $ BEBIDA SIN ALCOHOL
TOTAL $ BEBIDA CON ALCOHOL
CANTIDAD DE INVITADOS
CANTIDAD DE INVITADOS QUE BEBEN ALCOHOL

PROCESO:

PEDIR TOTAL DE LA COMIDA 
PEDIR TOTAL DE LA BEBIDA SIN ALCOHOL
PEDIR TOTAL DE LA BEBIDA CON ALCOHOL
PEDIR CANTIDAD DE INVITADOS
PEDIR CANTIDAD DE INVITADOS QUE BEBEN ALCOHOL
DIVIDIR TOTAL DE LA COMIDA POR CANTIDAD DE INVITADOS Y SUMARLE A ESO LA DIVISION TOTAL 
DE LA BEBIDA SIN ALCOHOL POR CANTIDAD DE INVITADOS



SALIDA:
MOSTRAR IMPORTE QUE DEBE ABONAR CADA INVITADO
MOSTRAR IMPORTE EXTRA POR EL CONSUMO DE ALCOHOL

"""

comida = int(input("Ingrese el total de la comida: "))
bebida_sin_alcohol = int(input("Ingrese el total de la bebida sin alcohol: "))
bebida_con_alcohol = int(input("Ingrese el total de la bebida con alcohol: "))
invitados = int(input("Ingrese el total de invitados: "))
invitados_beben_alcohol = int(input("Ingrese el total de invitados que beben alcohol: "))

importe = comida/invitados + bebida_sin_alcohol/invitados
try :
   extra = bebida_con_alcohol/invitados_beben_alcohol
except ZeroDivisionError:
   extra = 0
   print("No hay invitados que beban alcohol, por lo tanto no hay importe extra.")
else:
 print("El importe extra por el consumo de alcohol: ", extra)
 
print("El importe que debe abonar cada invitado es de : ", importe)

