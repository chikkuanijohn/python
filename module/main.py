from reg import *
from display import *
from update import *
from delete import *
data=[]
while True:
    print("1.add \n 2.display \n 3.update \n 4.delete \n 5.exit \n")
    ch=int(input("enter ur choice"))
    if ch==1:
        register(data)
    elif ch==2:
        dis(data)
    elif ch==3:
        update(data)
    elif ch==4:
        delete(data)
        print("you had exited")
        break
    else:
        ("invalid input")        


        

        
        
        



