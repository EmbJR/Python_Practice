'''
Python dictionary is like associative arrays or hashes found in Perl and consist of key:value pairs. 
The pairs are separated by comma and put inside curly brackets {}. 
To establish mapping between key and value, the colon':' symbol is put between the two.

Dictionary is a mutable object, so it is possible to perform add, modify or delete actions with corresponding functionality defined in dict class.
'''
dict = {} 
dict['one'] = "This is one" 
dict[2]   = "This is two" 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'} 
print (dict['one'])   # Prints value for 'one' key 
print (dict[2])     # Prints value for 2 key 
print (tinydict)    # Prints complete dictionary 
print (tinydict.keys())  # Prints all the keys 
print (tinydict.values()) # Prints all the values


'''A set in Python is a collection, but is not an indexed or ordered collection as string, list or tuple. 
An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.

Note that items in the set collection may not follow the same order in which they are entered. The position of items is optimized by Python to perform operations over set as defined in mathematics.
A set can store only immutable objects such as number (int, float, complex or bool), string or tuple. If you try to put a list or a dictionary in the set collection, Python raises a TypeError.
'''
print("set...")
set1 = {123, 452, 5, 6} 
set2 = {'Java', 'Python', 'JavaScript'} 
print(set1)
print(set2)
