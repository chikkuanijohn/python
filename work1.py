name=[]
while True:
     print("1.add \n 2.display \n 3.update \n 4. delete \n 5.exit\n")
     ch=int(input("enter your choice"))
     if ch==1:
        a=int(input("enter how many students"))
        for i in range(a):
            b=input(" name")
            name.append(b)
     elif ch==2:
         for i in name:
             print(i)
     elif ch==3:
         a_name=input('name')
         if a_name in name:
             new_name=input('new name')
             pos=name.index(a_name)
             name[pos]=new_name
         else:
             print('no')
     elif ch==4:
         a_name=input("enter the name")
         if a_name in name:
             name.remove(a_name)
         else:
             print('no')
     elif ch==5:
         break
     a_name in name:
     name.delete(a_name)
else:
    print('no')
     
         

    
        

    
     
            
        

     

     
 
            
        


            

      


        
          


                        