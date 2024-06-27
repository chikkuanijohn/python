'''names=[]
a=int(input("enter how many students"))
for i in range(a):
    name=input("enter the name")
    names.append(name)
print(names)'''

'''l=[1,2,3,1,2,3]
a=[]
for i in l:
    if i not in a:
       a.append(i)
print(a)''' 

'''l=["manu","akhil","sanu"]
for i in l:
    rev=""
    for j in i:
        rev=j+rev
    print(rev)''' 

l=[1,2,3,'a,b,c',20.5]
sum=0
for i in l:
    if type(i)==int or type(i)==float:
        sum=sum+i
print(sum)        

    

    




    

