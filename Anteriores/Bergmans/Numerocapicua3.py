try:
   
    numero = int(input())

   
    if numero < 0:
        print("El numero debe ser mayor a 0")
    
    
    elif numero < 100 or numero > 999:
        print("El numero de ser de 3 cifras")
    
    
    else:
        
        primer_digito = numero // 100
        ultimo_digito = numero % 10

        
        if primer_digito == ultimo_digito:
            print("Es capicua")
        else:
            print("No es capicua")

except ValueError:
    
    print("Error en el ingreso de los datos")