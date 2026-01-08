# 3. Python Sequence Data Types
''' Python sequences are bounded and iterable - Whenever we say an iterable in Python, it
means a sequence data type (for example, a list).'''

#3a. List Data Type
my_list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(my_list)
print (my_list[0]) # Prints first element of the list
print (my_list[1:3]) # Prints elements starting from 2nd till 3rd
print (my_list[2:]) # Prints elements starting from 3rd element
print (tinylist * 2) # Prints list two times
print (my_list + tinylist) # Prints concatenated list

#3b. Tuple Data Type
'''A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
To form a tuple, use of parentheses is optional. Data items separated by comma without
any enclosing symbols are treated as a tuple by default.

lists are mutable, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated (immutable). 
Tuples can be thought of as read-only lists'''
my_tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print (my_tuple) # Prints the complete tuple
print (my_tuple[0]) # Prints first element of the tuple
print (my_tuple[1:3]) # Prints elements of the tuple starting from 2nd till 3rd
print (my_tuple[2:]) # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2) # Prints the contents of the tuple twice
print (my_tuple + tinytuple) # Prints concatenated tuples

#3c. Range Data Type
'''Python Range Data Type A Python range is an immutable sequence of numbers which is typically used to iterate
through a specific number of items.
It is represented by the Range class. The constructor of this class accepts a sequence of numbers starting from 0 and increments to 1 until it reaches a specified number.
ere is the description of the parameters used
     start: Integer number to specify starting position, (Its optional, Default: 0)
     stop: Integer number to specify ending position (It's mandatory)
     step: Integer number to specify increment, (Its optional, Default: 1)'''

for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(1, 5, 2):
    print(i)