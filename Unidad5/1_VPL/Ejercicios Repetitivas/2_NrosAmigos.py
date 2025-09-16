"""
Como ocurre con las personas, hay números que tienen una cierta afinidad. Vamos a ver en qué consiste esa relación de amistad.

Dos números amigos son dos números enteros positivos a y b tales que la suma de los divisores propios de uno es igual al otro número y viceversa (la unidad se considera divisor propio, pero no lo es el mismo número).

Un ejemplo es el par de números naturales (220, 284), ya que:

los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, que suman 284;
los divisores propios de 284 son 1, 2, 4, 71 y 142, que suman 220
Un profesor de matemática necesita un programa que ingresando dos números indique si los mismos son amigos
"""

nro_a = int(input("Ingrese el primer numero: "))
nro_b = int(input("Ingrese el segundo numero: "))

suma_a = 0
for i in range(1,nro_a,1):
    if nro_a % i == 0:
        suma_a  += i

suma_b = 0
for j in range(1,nro_b,1):
    if nro_b % j == 0:
        suma_b  += j

if suma_a == nro_b and suma_b == nro_a:
    print(f"Los numeros {nro_a} y {nro_b} son amigos")
else:
    print(f"Los numeros {nro_a} y {nro_b} NO son amigos")