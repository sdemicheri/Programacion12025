#EJEPLO N°1

#Solicitar al usuario el año de nacimiento como número entero.
anio_nacimiento = int(input("Ingre su año de nacimiento: "))

#Solicitar al usuario el año actual como número entero.
anio_actual = int(input("Ingrese el año actual: "))

#Se verifica que el año de nacimiento no sea mayor que el año actual. Si esto ocurre, se muestra un mensaje de error
if anio_nacimiento < anio_actual:
    edad = anio_actual - anio_nacimiento
else:
    print("ERROR.El año de nacimiento no puede ser mayor que el año actual")


#Calcular la edad
edad = anio_actual - anio_nacimiento

#Imprimir la edad
print("La edad de la persona es:", edad)



#EJEMPLO N°2

# Solicitar años
anio_nacimiento = int(input("Año de nacimiento: "))
anio_actual = int(input("Año actual: "))

# Calcular edad
edad = anio_actual - anio_nacimiento

# Mostrar resultado
print("Edad:", edad)  
  