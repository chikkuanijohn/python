def update(data):
    id=int(input("enter user id to update:"))
    for i in data:
        if i["id"]==id:
            print("current name : " + i['name'])
            new_name=input("enter new name(leave blank to keep current):")
            i["name"]=new_name or i["name"]

            print("Current Age : " , i['age'])
            new_age=input("enter new age(leave blank to keep current):")
            i["age"]=new_age or i["age"]

            print("Current Place:"+ i['place'])
            new_place=input("enter new place(leave blank to keep current):")
            i["place"]=new_place or i["place"]

            print("profile updated successfully")
            break

        else:
            print("id not found!\n")
