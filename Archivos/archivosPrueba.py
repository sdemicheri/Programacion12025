#prueba2=open("Archivos\\prueba2.txt","r")
prueba5=open("Archivos\\prueba5.txt","w")
num1=input("num1")
num2=input('num2')

for i in range (1,101):
    for j in range(1,101):
            r=i*j
            prueba5.write(str(i) + "," + str(j) + "," + str(r) + "\n")

prueba5.close()
prueba5=open("Archivos\\prueba5.txt","r")

cadena=prueba5.readlines()
for i in range(len(cadena)):
    registro=cadena[i].strip().split(",")
    if registro[0]==num1 and registro[1]==num2:
        print(registro[2])
prueba5.close()
