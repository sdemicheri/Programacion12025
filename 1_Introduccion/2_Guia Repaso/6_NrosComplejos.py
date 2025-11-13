"""
Realizar un programa que lea dos número complejos, (a,b) y (c,d), y calcule su producto:
(a,b) * (c,d) = (ac - db, ad + bc)
"""
print("por favor, paso a paso ingrese dos números complejos")

a=int(input("ingrese la primer parte del primer número complejo: "))
b=int(input("ingrese la segunda parte del primer número complejo: "))
c=int(input("ingrese la primer parte del segundo número complejo: "))
d=int(input("ingrese la segunda parte del segundo número complejo: "))

print(f"{(a*c-d*b),(a*d+b*c)}")