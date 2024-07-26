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

# data=con.execute("select * from student")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#    #print(i)
#  print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 

# name=str(input("name"))
# data=con.execute("select * from student where name=?",(name,))
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 

# age=int(input("age"))
# data=con.execute("select * from student where age=?",(age,))
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2])) 

# mark=float(input("mark"))
# data=con.execute("select * from student where mark=?",(mark,))
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))


# mark=float(input("mark"))
# data=con.execute("select * from student where mark>=95")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#      print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# age=int(input("age"))
# data=con.execute("select * from student where age>=12")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#       print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# con.execute("update student set name='kichu p'where name='kichu'")
# con.commit()
# data=con.execute("select * from student")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#        print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# data=con.execute("update student set age='27'where name='achu'")
# con.commit()
# data=con.execute("select * from student")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#         print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))


# data=con.execute("delete from student where name='akshay'")
# con.commit()
# data=con.execute("select * from student")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#         print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# data=con.execute("select * from student where name like 'a%y'")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# data= con.execute("select * from student order by name desc")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#     print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# data=con.execute("select name, min(mark)from student group by name")
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#     print(i)
   # print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# data=con.execute("select name, max(mark)from student group by name") 
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#      print(i)
     #print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# data=con.execute("select name, avg(mark)from student group by name") 
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#      print(i)
    #print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

# data=con.execute("select name, sum(mark)from student group by name") 
# print("{:<15}{:<15}{:<15}".format("age","name","mark"))
# for i in data:
#      print(i)
    #print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))

data=con.execute("select name, count(mark)from student group by name") 
print("{:<15}{:<15}{:<15}".format("age","name","mark"))
for i in data:
     print(i)
    #print("{:<15}{:<15}{:<15}".format(i[0],i[1],i[2]))
  



























    
    
    


    



