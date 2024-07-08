def delete(data):
    id=int(input("enter user id to delete:"))
    for i in data:
        if i["id"]==id:
            data.remove(i)
            print("user deleted successfully!\n")
            break
    else:
        print("id not found!\n")        
        
    
            
            
            