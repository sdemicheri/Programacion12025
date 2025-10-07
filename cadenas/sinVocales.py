cad=input().lower()
cad2=''
for i in range (len(cad)):
    if cad[i]!='a' and cad[i]!='e' and cad[i]!='i' and cad[i]!='o' and cad[i]!='u':
        cad2+=cad[i]
print (cad2)