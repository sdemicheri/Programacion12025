try:
    num=int(input("Ingrese un numero: "))
    c=num//100
    r=num%100
    d=r//10
    u=r%10
    print("La unidad es: ",u)
    print("La decena es: ",d)
    print("La centena es: ",c)
except ValueError:
    print("Error en el ingreso de los datos")
    