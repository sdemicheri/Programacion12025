#Entrada: diaNacimiento - MesNacimiento - DiaActual - MesActual
#Proceso: Definir meses con sus dias pertinentes, Pedir datos, 
# restar  
#Salida: DiasFaltantesParaCumplirAnios
print ("Introduzca los datos que se le pide para obtener cuantos dias aproximados faltan para su cumpleanios")
diaN=int(input("Dia de nacimiento"))
mesN=int(input("Mes de nacimiento"))
diaA=int(input("Dia actual"))
mesA=int(input("Mes actual"))
i=mesA
dias=0
if mesA ==mesN and diaA>=diaN:
    dias=365-(diaA-diaN)
else:
    while i!=mesN:      #Tiene cilclo MAAAAAAAAL
        dias+=30
        i+=1
        if i>12:
            i=1
    dias+=30-diaA+(diaN-30)
print ("Faltan aproximadamente: ", dias, "Dias para tu cumpleanios")
