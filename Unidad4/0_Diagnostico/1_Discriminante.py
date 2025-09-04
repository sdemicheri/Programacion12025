"""
Las raíces de una ecuación de segundo grado ax2+bx+c=0 
son reales si y sólo si el discriminante dado por (b**2-4ac) no es negativo. Se desea leer 
el valor de los coeficientes "a","b", "c" e imprimir el resultado del discriminante.
"""
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))

discriminante=(b**2)-(4*a*c)

print("El valor del discriminante es:",(discriminante))