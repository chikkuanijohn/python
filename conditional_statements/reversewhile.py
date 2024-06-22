a=int(input("enter a no"))
rev=0
i=a
while a>0:
    d=a%10
    rev=(rev*10)+d
    a//=10
print(rev)
        