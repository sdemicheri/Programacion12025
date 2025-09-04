"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el
índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu
índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado
redondeado con dos decimales.
"""
peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en metros: "))

imc = peso / (altura)**2

print(f"tu indice de masa corporal es: {imc:.2f}")