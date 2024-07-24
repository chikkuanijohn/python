import sqlite3
con=sqlite3.connect("emp.db")
try:
    con.execute("create  table employee(emp_id,name text,email_id,age int,position text,salary real)")
except:
    pass
while True:
    print("1.Add \ n2.update \n3.delete \n4.display \n5.search")
    ch=int(input("Enter your choice"))
    if ch==1:
        emp_id=
        name=str(input("enter name"))
        email_id=
        age=int(input("enter age"))
        position=input("enter position")
        salary=float("enter salary")
        con.execute("insert into employee(emp_id,email_id,age,position,salary)values(?,?,?,?,?)",(emp_id,email_id,age,position,salary))
        con.commit()




