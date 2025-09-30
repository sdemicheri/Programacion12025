"""
Acabas de abrir una cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer
, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
saldo_inicial = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))
interés = 4 / 100

ahorros_año_1 = saldo_inicial * (1+interés)
ahorros_año_2 = ahorros_año_1 * (1+interés)
ahorros_año_3 = ahorros_año_2 * (1+interés)

print("Ahorros tras el primer año:", round(ahorros_año_1, 2))
print("Ahorros tras el segundo año:", round(ahorros_año_2, 2))
print("Ahorros tras el tercer año:", round(ahorros_año_3, 2))