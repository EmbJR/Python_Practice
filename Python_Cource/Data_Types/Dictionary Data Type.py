# 7. Python Dictionary Data Type
'''Python dictionaries are kind of hash table type. A dictionary key can be almost any Python
type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary
Python object.
Dictionary is a mutable object, so it is possible to perform
add, modify or delete actions with corresponding functionality defined in dict class'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print (tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values