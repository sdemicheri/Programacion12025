arroba=0
punto=False
dominios=1
mail=input()
for i in range(1,len(mail)):
    if mail[i]=="@" and mail[i-1]!=' ': 
        arroba+=1
    if arroba==1:
        if mail[i]=='.' and mail[i-1]!="@":
            punto=True
            dominios+=1
if arroba==1 and punto==True:
    print("mail válido")
else:
    print("mail inválido")
