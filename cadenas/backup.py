arroba=False
punto=False
dominios=1
mail=input()
for i in range(1,len(mail)):
    if mail[i]=="@": 
        arroba=True
    if arroba==True:
        if mail[i]=='.' and mail[i-1]!="@":
            punto=True
            dominios+=1
if arroba==True and punto==True:
    print("mail válido")
else:
    print("mail inválido")
