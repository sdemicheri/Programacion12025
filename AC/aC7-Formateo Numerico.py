num1=input()
num2=""
for i in range(len(num1)):
    if num1[i]==".":
        num2+=","
    elif num1[i]==",":
        num2+="."
    else:
        num2+=num1[i]
print(num2)