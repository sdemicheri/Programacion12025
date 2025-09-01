#analisis
#entrada
#precio del peluche
#proceso
# Billetes de $100
# (237−(2×100)=37) 
# Billetes de $50
#37÷50=0 
# Billetes de $20
#37÷20=1 
#37−(1×20)=17.
# Billetes de $10
#17÷10=1 billete.
# 17−(1×10)=7.
# Billetes de $5
#7÷5=1
# 7−(1×5)=2.
# Billetes de $1
#2÷1=2 
#mostrar cuantos billetes de 100, 50, 20,10,5, 1 se ultizaron
#salida
#2 billetes de $100
#0 billetes de $ 50
#1 billetes de $ 20
#1 billetes de $ 10
#1 billetes de $ 5
#2 billetes de $ 1
precio_peluche = int(input())
billetes_100 = precio_peluche // 100
monto_restante = precio_peluche % 100
billetes_50 = monto_restante // 50
monto_restante = monto_restante % 50
billetes_20 = monto_restante // 20
monto_restante = monto_restante % 20
billetes_10 = monto_restante // 10
monto_restante = monto_restante % 10
billetes_5 = monto_restante // 5
monto_restante = monto_restante % 5
billetes_1 = monto_restante // 1
print(billetes_100, "billetes de $100")
print(billetes_50, "billetes de $50")
print(billetes_20, "billetes de $20")
print(billetes_10, "billetes de $10")
print(billetes_5, "billetes de $5")
print(billetes_1, "billetes de $1")