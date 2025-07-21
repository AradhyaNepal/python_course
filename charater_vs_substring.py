s="Hello"
# s[0]="h"

s="h"+s[1:]
print(s)



name ="Hello Python"
name="Hi"+name[5:]
print(name) #Hi Python


helloName ="HelloPython"
helloName="Hi "+helloName[5:]
print(helloName) #Hi Python


anotherName="HelloPython"
anotherName=anotherName[:]+"World"
print(anotherName)