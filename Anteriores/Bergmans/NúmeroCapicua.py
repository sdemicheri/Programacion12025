try:
    
    numero_str = input("Ingrese un número entero de tres cifras: ")

   
    if not numero_str:
        print("Error al ingresar los datos")
    else:
        
        numero = int(numero_str)

        
        if numero < 0:
            print("El numero debe ser mayor a 0")
        
        
        elif numero < 100 or numero > 999:
            print("El numero debe ser de 3 cifras")
        
       
        else:
            
            primer_digito = numero // 100
            
            
            ultimo_digito = numero % 10

            
            if primer_digito == ultimo_digito:
                print("Es capicúa")
            else:
                print("No es capicúa")

except ValueError:
  
    print("Error al ingresar los datos")