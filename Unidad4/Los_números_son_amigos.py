#Como ocurre con las personas, hay números que tienen una cierta afinidad. Vamos a ver en qué consiste esa relación de amistad.
#Dos números amigos son dos números enteros positivos a y b tales que la suma de los divisores propios de uno es igual al otro número y viceversa (la unidad se considera divisor propio, pero no lo es el mismo número).
#Un ejemplo es el par de números naturales (220, 284), ya que:
#los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, que suman 284;
#los divisores propios de 284 son 1, 2, 4, 71 y 142, que suman 220
#Un profesor de matemática necesita un programa que ingresando dos números indique si los mismos son amigos

num1 = int(input)
num2 = int(input)

suma_1 = 0
i = 1
while i < num1:
    if num1 % i == 0:
        suma_1 += i
    i += 1

suma_2 = 0
j = 1
while j < num2:
    if num2 % j == 0:
        suma_2 += j
    j += 1

if suma_1 == num2 and suma_2 == num1:
    print(num1, "y", num2, "son números amigos")
else: 
    print(num1, "y", num2, "no son amigos") 