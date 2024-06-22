a=int(input("enter starting no"))
b=int(input("enter ending no"))
sum=0
i=a
while i<=b:
    if i%2==1:
        sum=sum+i
    i+=1    
print(sum)
     