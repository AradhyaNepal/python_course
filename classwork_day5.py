"""
num1: Input from user
num2: Input from user


choice - input from user addition (1), subtraction(2), division(3), multiplication(4)


"""


number1=int(input("Enter your first number: "))
number2=int(input("Enter your second number: "))
print("What you want to perform")
print("1. Addition")
print("2. Substraction")
print("3. Division")
print("4. Multiplication")
choice=input("Enter one of your choice: (1,2,3,4):")

if choice=="1":
    print("Performing Addition....")
    sum=number1+number2
    print("Sum is")
    print(sum)
elif choice=="2":
    print("Performing Substraction....")
    substraction=number1-number2
    print("Substraction is")
    print(substraction)
elif choice=="3":
    if number2==0:
        print("Second number cannot be zero")
    else:
        print("Performing Division....")
        division=number1/number2
        print("Division is")
        print(division)
elif choice=="4":
    print("Performing Multiplication....")
else:
    print("Invalid option. Please ensure that the number is 1,2,3,4")
