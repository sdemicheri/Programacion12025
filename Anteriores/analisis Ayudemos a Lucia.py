"""
ENTRADA:
precioPeluche
billete100
billete50
billete20
billete10
billete5
billete1

PROCESO:
Leer precioPeluche 
billete100= precioPeluche // 100
resto= precioPeluche % 100
billete50= precioPeluche // 50
resto= precioPeluche % 50
billete20= precioPeluche // 20
resto= precioPeluche % 20
billete10= precioPeluche // 10
resto= precioPeluche % 10
billete5= precioPeluche // 5
resto= precioPeluche % 5
billete1= precioPeluche // 1
resto= precioPeluche % 1
si billete100 > 0: 
    mostrar billete100, "billetes de $100"
sino si billete100 ==  0:
    mostrar "0 billetes de 100"
(...)

SALIDA:
Cantidad que necesita Lucia de cada billete

"""