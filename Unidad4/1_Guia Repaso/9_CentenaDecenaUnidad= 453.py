"""
Te presentan un número misterioso y te desafían a determinar y anunciar en voz alta la decena, centena y
unidad de este número en el menor tiempo posible.Ademas debes desarrollar un programa que realice esta
tarea de manera automatizada.
"""
try:
    num = int(input("ingrese un número: "))

    centena = num // 100
    resto = num % 100
    decena = resto // 10
    unidad = num % 10

    print (centena)
    print (decena)
    print (unidad)

except ValueError:
  print("error en el ingreso de los datos")
except ZeroDivisionError:
  print("no se puede dividir por cero")