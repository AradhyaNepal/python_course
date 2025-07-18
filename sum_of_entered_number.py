times=int(input("How many time you want to run: "))
sum=0
print("Starting the program, the program will run ",times," times except if 0 is pressed")
for i in range(times):
    value=int(input("Enter number "))
    if value==0:
        print("Breaking the sum since 0 is")
        break
    sum=sum+value
print("Total sum is ",sum)



sum=0
print("Welcome to the program. Program will print sum of all entered number.")
while True:
    value=input("Enter the next number (e to stop): ")
    if value=="e":
        print("Breaking the program since e is found")
        break
    else:
        value=int(value)
        sum=value+sum
print("Total sum is ",sum)

    