print("Welcome to fruits inventory")
fruits=[]
while True:
    print(f"Your current fruits are {fruits}")
    print("What action you can to perform")
    print("1. Add a new fruit")
    have_some_fruit=len(fruits)>0
    if have_some_fruit:
        print("2. Remove one fruit")
        print("3. Edit one fruit")
    print("e. Exit")
    value= input("Enter value from the option: ").lower()
    if value=="e":
        break
    elif value=="1":
        new_item=input("Enter new fruit to add: ")
        fruits.append(new_item)
    elif value=="2" and have_some_fruit:
         item_to_remove=input("Enter fruit you want to remove: ")
         if item_to_remove in fruits:
            fruits.remove(item_to_remove)
         else:
             print(f"{item_to_remove} not found in the inventory")    
    elif value=="3" and have_some_fruit:
        value_to_update=input("Which fruit you want to update: ")
        
        auto_found_index=-1
        for i in range(len(fruits)):
            if fruits[i]==value_to_update:
                auto_found_index=i
                break
        if auto_found_index!=-1:
           print(f"{value_to_update} is located at {auto_found_index+1} position of the inventory")
           from_what_to_update=input(f"Which fruit you want to put in this place: ")
           fruits[auto_found_index]=from_what_to_update
        else:
            print(f"{value_to_update} not found in the inventory")   
    else:
        print("Please pick valid options")

print("Your final fruits available in your inventory are")
print(fruits)