num=int(input())
while num>1:
    for i in range (1,num, 1):
        print (i, end=" ")
    print(num)
    num-=1
print ("1")