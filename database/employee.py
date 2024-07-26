import sqlite3
con=sqlite3.connect("emp.db")
try:
    con.execute("create  table employee(emp_id int,name text,email_id text,age int,position text,salary real)")
except:
    pass
while True:
    print("1.Add \n2.update \n3.delete \n4.display \n5.search ")
    ch=int(input("Enter your choice"))
    if ch==1:
        a=int(input("enter limit:"))
        for i in range(a):
            print(a)
        emp_id=int(input("enter ur emp_id:"))
        name=str(input("enter ur  name"))
        email_id= str(input("enter ur  mail"))
        age=int(input("enter ur  age"))
        position=input("enter ur position")
        salary=int(input("enter ur salary"))
        con.execute("insert into employee(emp_id,name,email_id,age,position,salary)values(?,?,?,?,?,?)",(emp_id,name,email_id,age,position,salary))
        con.commit()
        data=con.execute("select * from employee ")
        print(data)

        print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
        print('_'*80)
        for i in data:
            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
        print()

    elif ch==2:
        name=str(input("enter old name:"))
        data=con.execute("select * from employee")
        found = False
        for i in data:
            found = True
            new=str(input("enter new name:"))
            con.execute("update employee set name=? where name=? ",(new,name))
            con.commit()
            data=con.execute("select * from employee")
            print("updated succesfully")
            if  not found:
                print("invalid input !")
    elif ch==3:
        name=str(input("Enter name : "))
        data=con.execute("select * from employee where name=? ",(name,))
        found=False
        for i in data:
            found=True
            con.execute("delete from employee where name =?",(name,))
            con.commit()
            data=con.execute("select * from employee")
            print("Deleted duccessfully !")

        if not found:
            print("Invalid Input !")
 
    elif ch ==4:

        data=con.execute("select * from employee")

        print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
        print('_'*80)
        for i in data:
            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
        print()
        

    elif ch ==5:
        sname=str(input("Enter name : "))
        data=con.execute("select * from employee where name=? ",(sname,))  
        found = False
        for i in data:

            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format("name","age","email","salary","position","experiance")) ##print in a table
            print('_'*80)
            print("{:<15}{:<5}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[5])) 
            print()
            found=True
        if not found:
            print("Invalid Input !")
        

    elif ch ==6:
        print("You had exited")
        break    

    else:
         ("invalid input")
        
        





    


    





        
           
        










