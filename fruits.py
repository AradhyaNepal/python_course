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
         fruits.remove(item_to_remove)
    elif value=="3" and have_some_fruit:
        value_to_update=input("Which fruit you want to update: ")
        from_what_to_update=input(f"From what you want to update {value_to_update}: ")
        fruits.remove(value_to_update)
        fruits.append(from_what_to_update)
    else:
        print("Please pick valid options")

print("Your final fruits available in your inventory are")
print(fruits)