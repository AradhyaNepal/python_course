"""
Ask from user
If it contains vowel print: It has vowel
Else print: Does not vowel
"""

print("Welcome to vowel finder")
print("Vowel are letter which contains a,e,i,o,u")
print("-----------------------------------------")
letter=input("Enter a letter: ")
print("-----------------------------------------")
if letter=="a" or letter=="A" or letter=="e" or letter=="E" or letter=="i" or letter=="I" or letter=="o" or letter=="O" or letter=="u" or letter=="U":
    print("Letter is vowel")
else:
    print("Letter is not vowel")


# Testing data : a,e,i,o,u,A,E,I,O,U