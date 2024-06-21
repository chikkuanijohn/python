a=int(input("enter units"))
if a<100:
    print("no charge")
elif a<200:
    a-=100
    total=a*5
    print("charge",total)
elif a>200:
    a-=200
    total=(a*10)+500
    print("charge",total) 
