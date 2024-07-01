dtl=[]
for i in range(4):
    name=input('name')
    age=int(input("age"))
    dtl.append({'name':name,'age':age})
    print("{:<10} {:<6}".format("name","age"))
    print('_'*20)
    for i in dtl:
        print("{:10} {:<6}".format(i['name'],i['age']))

        print('AGE>30')
        print("{:<10}{:<6}".format("name","age"))
        for i in dtl:
                if i['age']>=30:
                     print("{:10}{:<6}".format(i['name'],i['age']))

                     print('AGE<30')
                     print("{:<10}{:<6}".format("name","age"))
                     for i in dtl:
                          if i['age']<30:
                               print("{:<10}{:<6}".format(i['name'],i['age']))
                       