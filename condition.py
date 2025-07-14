x = int(input("Enter your number: "))

if x == 10:
    x=x+20
    print("Number is 10")
    print("Increasing number by 20")
elif x == 20:
    x=x+30
    print("Number is 20")
    print("Increasing number by 30")
elif x == 30:
    x=x+40
    print("Number is 30")
    print("Increasing number by 40")
else:
    print("Number is not 10 neither 20")

print("Final number is")
print(x)