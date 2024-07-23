import sqlite3
con = sqlite3.connect("sample.db")
try:
   con.execute("create table student(age int,name text,mark real)")
except:
    pass
con.execute("insert into student(age,name,mark)values(22,'akshay',65)")
# con.commit() 

# age=int(input("age"))
# name=str(input("name"))
# mark =float(input("mark"))
# con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark))
# con.commit()

# a=int(input("enter a limit"))
# for i in range(a):
#     age=int(input("age"))
#     name=str(input("name"))
#     mark=float(input("mark"))
# con.execute("insert into student(age,name,mark)values(?,?,?)",(age,name,mark))
# con.commit()

# data=con.execute("select * from student")
# print(data)
# for i in data:
#     print(i)

# data=con.execute("select name,age from student")
# print(data)
# for i in data:
#     print(i)

data=con.execute("select * from student")
print("{:<15}{:<15}{:<15}".format("age","name","mark"))
for i in data:
   #print(i)
 print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 




