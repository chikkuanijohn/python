# a=int(input("enter a no"))
# rev=0
# for i in range(a):
#     d=a%10
#     rev=(rev*10)+d
#     a//=10
#     if a==0:
#         break
# print(rev) 

#Binary pattern

# for i in range(1,6):
#     for j in range(i):
#         print((i+j)%2,end="")
#     print()    

for i in range(1,6):
    for j in range(i):
        if i%2==0:
            print('+',end="")
        else:
            print('#',end="")
    print()                

