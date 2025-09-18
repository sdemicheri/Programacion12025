acu = 0
dias = 7
for i in range (dias):
    temperatura_dia = int(input("poner la temperatura:"))
    acu =  temperatura_dia + acu


prome = acu / 5
print(prome)