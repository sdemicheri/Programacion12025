precio=int(input())
billete100= precio//100
precio= precio%100
billete50= precio//50
precio= precio%50   
billete20= precio//20
precio= precio%20
billete10= precio//10
precio= precio%10
billete5= precio//5
precio= precio%5
billete1= precio
print (billete100, "billetes de $100")
print (billete50, "billetes de $50")
print (billete20, "billetes de $20")
print (billete10, "billetes de $10")
print (billete5, "billetes de $5")
print (billete1, "billetes de $1")

#ANALISIS
#Lucía, una niña de 8 años quiere comprarse un peluche que cuesta un determinado monto. Sin embargo, Lucía no sabe cuántos billetes necesita llevar a la tienda para pagar su peluche. Tiene billetes de $100, $50, $20, $10, $5 y $1.

#Se necesita crear un algoritmo que, solo utilizando lo aprendido hasta el momento, le diga cuántos billetes de cada denominación necesita. Así, Lucía podrá ir a la tienda con la seguridad de que tiene el monto exacto en billetes, listo para comprar su peluche favorito.

#ENTRADA:
#Precio del peluche
#Tipos de billetes disponibles

#PROCESO:
#pedir precio de billete
#billete100= precio//100
#precio= precio%100
#billete100= precio//50
#precio= precio%50   
#billete100= precio//20
#precio= precio%20
#billete100= precio//10
#precio= precio%10
#billete100= precio//5
#precio= precio%5
#billete100= precio//2
#precio= precio%2
#billete100= precio//1
#mostrar una lista con los tipos de billete y la cantidad necesaria para comprar el peluche

#SALIDA:
#cantidad de billetes de cada demnominacion para comprar el peluche 