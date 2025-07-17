"""
Ask word from user
If it contains vowel print: It has vowel
Else print: Does not vowel
"""

print("Welcome to vowel finder")
print("Vowel are word which contains a,e,i,o,u")
print("-----------------------------------------")
word=input("Enter a word: ")
print("-----------------------------------------")
if "a" in word or "A" in word or "e" in word or "E" in word or "i" in word or "I" in word or "o" in word or "O" in word or "u" in word or "U" in word:
    print("Letter is vowel")
else:
    print("Letter is not vowel")


# Testing data : a,e,i,o,u,A,E,I,O,U