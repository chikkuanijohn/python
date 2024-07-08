'''dtl=[]
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
                               print("{:<10}{:<6}".format(i['name'],i['age']))'''


dtls=[{"name":"anu","age":20},{"name":"akhil","age":25},{"name":"achu","age":22},{"name":"ammu","age":24}]
for i in range(0):
    name=input("name")
    age=int(input("age"))
    dtls.append({"name":name,"age":age})
    print("{:<10}{:6}".format("name","age"))
    print('_'*20)
    for i in dtls:
        print("{:<10}{:<6}".format(i["name"],i["age"]))
        print("age>22")
        print("{:<10}{:6}".format("name","age"))
    for i in dtls:
              if i["age"]>=22:
                    print("{:<10}{:6}".format(i["name"],i["age"]))
    print("age<22")
    print("{:<10}{:6}".format("name","age"))
    for i in dtls:
          if i["age"]<22:
                print("{:<10}{:<6}".format(i["name"],i["age"]))
    
        
              





