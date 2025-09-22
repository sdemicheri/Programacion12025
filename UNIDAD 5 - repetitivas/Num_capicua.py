#ERROR NUMEROS IGUALES DE 3 CIFRAS

# Solicitar ingreso de número
entrada = input("Ingresa un número entero de tres cifras: ")

# no se ingresa ningún valor
if entrada == "":
    print("Error al ingresar los datos")
else:
    try:
        numero = int(entrada)

# Caso 2: número negativo
        if numero < 0:
            print("El numero debe ser mayor a 0")
        
# Caso 3: número con más o menos de tres cifras
        elif numero < 100 or numero > 999:
            print("El numero debe ser de 3 cifras")
        
# Caso 4: número válido, verificar si es capicúa
        else:
# Convertimos a string para poder invertirlo
            num_str = str(numero)
            if num_str == num_str[::-1]:
                print("Es capicua")
            else:
                print("No es capicua")
    
    except ValueError:
        print("Error al ingresar los datos")