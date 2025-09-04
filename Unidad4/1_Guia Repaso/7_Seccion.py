"""
Se desea calcular el valor de la sección (S) de un conductor, la cual se determina en función
de la corriente eléctrica I y de la conductividad C del material (C=I/S). Además, a la sección
así obtenida se le incrementa un 25% por razones de seguridad.
"""
corriente_eléctrica=float(input("ingrese el valor de la corriente eléctrica: "))
conductividad=float(input("ingrese el valor de la conductividad: "))

sección=(corriente_eléctrica/conductividad)*(1+25/100)

print("el valor de la sección del conductor es:",sección)