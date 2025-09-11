num1=int(input("ingrese num1: "))
num2=int(input("ingrese num2: "))
suma="+"
resta="-"
divi="/"
mult="*"
simbolo=input("ingrese simbolo: ")
try:
    if simbolo =="+":
        print (num1+num2)
    elif simbolo =="-":
        print (num1-num2)
    elif simbolo =="/":
       if num2 !=0:
            print (num1/num2)
       else: 
           print("Error no se puede divir por 0")
    elif simbolo =="*":
        print (num1*num2)
except ValueError:
        print ("error al ingreso de los numeros")