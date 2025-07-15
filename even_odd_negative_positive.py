"""
Positive and even
Positive and odd
zero and even
Negative and even
Negative and odd
"""

print("Welcome to Positive/Negative/Zero and Even/Odd finder")
print("-----------------------------------------------------")
user_input=int(input("Enter a number: "))
print("-----------------------------------------------------")
if(user_input<0 and user_input%2==0):
    print("The number you entered is Negative and Even")
if(user_input<0 and user_input%2!=0):
    print("The number you entered is Negative and Odd")
if(user_input==0):
    print("The number you entered is Zero and Even")
if(user_input>0 and user_input%2==0):
    print("The number you entered is Positive and Even")
if(user_input>0 and user_input%2!=0):
    print("The number you entered is Positive and Odd")



# Testing Data: -2 -1 0 1 2

# Asked Testing Data: 8 15 0 -15 -8