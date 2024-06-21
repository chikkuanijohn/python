a=int(input("enter the costprice"))
if a>100000:
    tax = a*0.15
    print("cost",tax)
elif (a>50000) and (a<=100000):
     tax = a*0.1
     print("cost",tax)
elif(a<=50000):
     tax = a*0.05
     print("cost",tax)