#Lucía, una niña de 8 años quiere comprarse un peluche que cuesta un determinado monto. Sin embargo, Lucía no sabe cuántos billetes necesita llevar a la tienda para pagar su peluche. Tiene billetes de $100, $50, $20, $10, $5 y $1.
#Se necesita crear un algoritmo que, solo utilizando lo aprendido hasta el momento, le diga cuántos billetes de cada denominación necesita. Así, Lucía podrá ir a la tienda con la seguridad de que tiene el monto exacto en billetes, listo para comprar su peluche favorito.
#Entrada:
#Hola Lu, ingresa el precio del peluche: $ 237
#Salida:
#2 billetes de $100
#0 billetes de $ 50
#1 billetes de $ 20
#1 billetes de $ 10
#1 billetes de $ 5
#2 billetes de $ 1

precioPeluche= int(input("Hola Lu, ingresa el precio del peluche: "))
billete100= precioPeluche // 100
resto= precioPeluche % 100
billete50= resto // 50
resto= resto % 50
billete20= resto // 20
resto = resto % 20
billete10 = resto // 10
resto = resto % 10
billete5 = resto // 5
resto = resto % 5
billete1= resto
if billete100 > 0: 
    print(billete100, "billetes de $100")
elif billete100 ==  0:
    print("0 billetes de 100")
if billete50 > 0: 
    print(billete50, "billetes de $50")
elif billete50 == 0:
    print("0 billetes de 50")
if billete20 > 0: 
    print(billete20, "billetes de $20")
elif billete20 == 0:
    print("0 billetes de 20")
if billete10 > 0: 
    print(billete10, "billetes de $10")
elif billete10 == 0:
    print("0 billetes de 10")
if billete5 > 0: 
    print(billete5, "billetes de $5")
elif billete5 == 0:
    print("0 billetes de 5")
if billete1 > 0: 
    print(billete1, "billetes de $1")
elif billete1 == 0:
    print("0 billetes de 1")