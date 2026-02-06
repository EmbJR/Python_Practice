''' Python Tuple Exercise 1
Python program to find unique numbers in a given tuple'''
T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
T2 = ()

for x in T1:
    if x not in T2:
        T2 = T2 + (x,)

print(T2)

''' Python Tuple Exercise 2
Python program to find sum of all numbers in a tuple'''
T1 = (1, 9, 1, 6, 3, 4)
ttl = 0

for x in T1:
    ttl = ttl + x

print(ttl)
ttl = sum(T1)
print ("Sum of all numbers sum() function:", ttl)

''' Python Tuple Exercise 3
Python program to create a tuple of 5 random integers'''
import random
t1 = ()
for i in range(5):
    x = random.randint(0, 100)
t1+=(x,)
print (t1)