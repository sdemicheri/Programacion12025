"""
Con tu grupo de amigos salen muy seguido a comer a distintos bares y restaurantes de la ciudad. 
Dividir la cuenta es un problema, ya que el importe es grande y la cantidad de amigos siempre varía en cada salida. 
Haz un programa que resuelva el problema, donde la primera entrada sea la cantidad de amigos, 
la segunda entrada sea el total de la cuenta (sin símbolo de $, y con valores decimales).

La salida debe ser:
El total que debe pagar cada uno es de: ${monto}
"""
cantidad_amigos = int(input("ingrese la cantidad de amigos: "))
total_cuenta = float(input("ingrese el total de la cuenta a pagar: "))

monto = total_cuenta / cantidad_amigos

print(f"El total que debe pagar cada uno es de: ${monto:.2f}")