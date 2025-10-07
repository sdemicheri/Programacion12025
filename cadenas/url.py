url=input()
dobleBarra=0
i=0
while dobleBarra==0:
    if url[i]=="/" and url[i+1]=="/":
        dobleBarra=i
    i+=1
for i in range (dobleBarra, len(url)):
    if url[i]=='/':
        ultimaBarra=i
subUrl= url[dobleBarra+2:ultimaBarra+1]
print (subUrl)