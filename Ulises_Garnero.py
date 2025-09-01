precio = int(input("Hola Lu, ingresa el precio del peluche: $ "))
b100 = precio // 100
precio = precio % 100

b50 = precio // 50
precio = precio % 50

b20 = precio // 20
precio = precio % 20

b10 = precio // 10
precio = precio % 10

b5 = precio // 5
precio = precio % 5

b1 = precio

print(b100, "billetes de $100")
print(b50, "billetes de $ 50")
print(b20, "billetes de $ 20")
print(b10, "billetes de $ 10")
print(b5, "billetes de $ 5")
print(b1, "billetes de $ 1")