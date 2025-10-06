
cad='la casa'
cad2=''
for i in range (len(cad)):
    if cad[i].lower()=='a':
        cad2+=' '
    else:
        cad2+=cad[i]
print (cad2[2,5])