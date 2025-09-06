try:
    
    chocolates = int(input("Ingrese la cantidad de chocolates: "))
    precio = int(input("Ingrese el precio: "))
    impuesto = int(input("Ingrese el impuesto: "))

    porcentaje = chocolates * precio * impuesto
    total = chocolates * precio + porcentaje

    print("Total a pagar:", total)

except ValueError:
    print("Ingrese los valores correctos")