"""
Imprimir números en secuencia es una tarea relativamente simple. 
Pero, ¿es así cuando la secuencia es en un espejo? 
Esta es una secuencia, que tiene un número al comienzo y uno al final 
y todos los números entre ellos, 
incluyendo éstos, están dispuestos en una secuencia creciente sin espacios, 
por lo cual esta secuencia está diseñada en forma invertida, 
como un reflejo en el espejo. Por ejemplo, si la secuencia es de 7 a 12, 
el resultado sería 789101112211101987

Escriba un programa que, dado dos enteros, imprima su secuencia espejo.

Entrada
La entrada tiene un valor entero C que indica el número de casos de prueba. 
Cada caso tiene dos valores enteros ​​E y B ( 1 ≤ B ≤ E ≤ 12221 ), 
que indican el inicio y el final de la secuencia.

Salida
Para cada caso de prueba, imprima la secuencia espejo respectiva.
"""
CasosDePrueba = int(input())

for i in range(CasosDePrueba):
    nros = input().split()
    inicio_secuencia = int(nros[0])
    fin_secuencia = int(nros[1])

    cadena = ""
    secuencia_espejo = ""

    for i in range(inicio_secuencia,fin_secuencia+1,1):
        cadena += str(i)

    for j in range(len(cadena)-1,-1,-1):
        secuencia_espejo += cadena[j]

    print(cadena+secuencia_espejo)  