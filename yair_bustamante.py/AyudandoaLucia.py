#Analisis
<<<<<<< HEAD
precioPeluche = int(input("Hola Lu, ingresa el precio del peluche: "))
billete100 = precioPeluche // 100
resto = precioPeluche % 100
billete50 = resto // 50
resto = resto % 50
billete20 = resto // 20
resto = resto % 20
billete10 = resto // 10
resto = resto % 10
billete5 = resto // 5
resto = resto % 5
billete1 = resto
print(billete100, "billetes de $100")
print(billete50, "billetes de $50")
print(billete20, "billetes de $20")
print(billete10, "billetes de $10")
print(billete5, "billetes de $5")
print(billete1, "billetes de $1")
=======
#Entrada = Precio del peluche
precio=int(input("Hola Lucía, ingresa el precio del peluche"))
#Proceso = Calcular la cantidad de billetes que se necesitan para llegar al precio del peluche
billete100 = precio // 100
resto = precio % 100

billete50 = resto // 50
resto = resto % 50

billete20 = resto // 20
resto = resto % 20

billete10 = resto // 10
resto = resto % 10

billete5 = resto // 5
resto = resto % 5

billete1 = resto
#Salida = Cantidad de billetes que se necesitan para pagar el precio del peluche
print(billete100, "billetes de $100")
print(billete50, "billetes de $ 50")
print(billete20, "billetes de $ 20")
print(billete10, "billetes de $ 10")
print(billete5, "billetes de $ 5")
print(billete1, "billetes de $ 1")
>>>>>>> d270e1416467932f8d1bff410f9e7ba62a397e4b
