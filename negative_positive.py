print("Welcome to negative, positive or zero finder!")
print("---------------------------------------------")
user_input= int(input("Enter a number: "))
print("---------------------------------------------")
if user_input<0:
    print("Number you entered is negative")
elif user_input==0:
    print("Number you entered is zero")
else:
    print("Number you entered is positive")