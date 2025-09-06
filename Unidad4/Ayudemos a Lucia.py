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