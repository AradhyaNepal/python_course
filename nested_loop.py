"""
# Question 1
-------------
1
12
123
1234
12345

# Question 2
-------------
12345
1234
123
12
1


# Question 3
-------------
54321
4321
321
21
1


print(5,end="")
"""


for i in range(6):
    for j in range(i):
        print(j+1,end="")
    print()