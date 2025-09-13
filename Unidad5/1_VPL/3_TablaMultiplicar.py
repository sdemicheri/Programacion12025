"""
Ingrese un número N y muestre la tabla de multiplicar del número. 
Muestre el multiplicando, el multiplicador y el producto
N = 7 , 7*1 = 7, 7*2 = 14 ...
"""
numero = int(input("Ingrese un número: "))
for i in range(1,11):
    print(f"{numero}*{i} = {numero*i}")