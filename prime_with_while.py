number=int(input("Enter number to check whether its prime or not: "))
x=2
isPrime=True
while x<number:
    if number==0 or number==1:
        isPrime=False
        pass
    number=number+1
if isPrime:
    print("Number is prime")
else:
    print("Number is not prime")