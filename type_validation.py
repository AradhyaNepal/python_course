value=input("Please enter a number: ")
if value.isdigit():
    num=int(value)
    print(f"Converted integer: {num}")
elif "." in value:
    num=float(value)
    print(f"Converted double: {num}")
else:
    print("Invalid number input")
