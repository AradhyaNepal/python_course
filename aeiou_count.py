value = input("Enter the value: ")
vowels = "aeiouAEIOU"
count = 0
for char in value:  
    if char in vowels:
        count += 1
print("The number of vowels in the value are:", count)