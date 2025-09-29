def imprimirlinea():
    print("-"*5)

def suma(a,b):
    r= a+b
    return r
def dividir(divisor,dividendo):
    d=dividendo/divisor
    return d

if __name__ == "__main__":
    imprimirlinea()
    print("hola")
    x= int(input())
    y= int(input())
    imprimirlinea()
    if y != 0:
        print("la division es:",dividir(diviendo=y, divisor=x))
    else:
        dividir(y,x)
        print ("la division es:",dividir(y,x))
    print("la suma es:",suma(x,y))
    edad1= int(input())
    edad2= int(input())
    print("la suma de edades es: ",suma(edad1,edad2))