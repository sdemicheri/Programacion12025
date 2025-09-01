#ejercicio de prueba
comida = int(input("ingrese el total de la comida:; "))
bebida_ca = int(input("ingrese el total de la bebida con alcohol: "))
bebida_sa = int(input("ingrese el total de la bebida sin alcohol: "))
invitados = int(input("ingrese la cantidad de envitados: "))
invitados_ca = int(input("ingrese la cantidad de invitados: "))
importe = comida/invitados+bebida_sa/invitados
extra =bebida_ca/invitados_ca 
print("El importe debe abonar cada invitado es de: ", importe)
print("El import extra por el consumo de alcohol:", extra)