'''--------------------------------- Dictionaries in Python --------------------------
In Python, a dictionary is a built-in data type that stores data in key-value pairs. It is an
unordered, mutable, and indexed collection. Each key in a dictionary is unique and maps
to a value. Dictionaries are often used to store data that is related, such as information
associated with a specific entity or object, where you can quickly retrieve a value based
on its key.
Python's dictionary is an example of a mapping type. A mapping object 'maps' the value
of one object to another. To establish mapping between a key and a value, the colon (:)
symbol is put between the two.
Each key-value pair is separated by a comma and enclosed within curly braces
{}. The key and value within each pair are separated by a colon (:), forming
the structure key:value.'''

''' Given below are some examples of Python dictionary objects − '''

capitals = {"Maharashtra":"Mumbai", 
            "Gujarat":"Gandhinagar", 
            "Telangana":"Hyderabad", 
            "Karnataka":"Bengaluru"}
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}

''' Key Features of Dictionaries
Following are the key features of dictionaries −
     Unordered − The elements in a dictionary do not have a specific order. Python
        dictionaries before version 3.7 did not maintain insertion order. Starting from 
        Python 3.7, dictionaries maintain insertion order as a language feature.
     Mutable − You can change, add, or remove items after the dictionary has been
        created.
     Indexed − Although dictionaries do not have numeric indexes, they use keys as
        indexes to access the associated values.
     Unique Keys − Each key in a dictionary must be unique. If you try to assign a
        value to an existing key, the old value will be replaced by the new value.
     Heterogeneous − Keys and values in a dictionary can be of any data type.

Example 1
Only a number, string or tuple can be used as key. All of them are immutable. You can
use an object of any type as the value. Hence following definitions of dictionary are also
valid'''
d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)

'''Python doesn't accept mutable objects such as list as key, and raises TypeError.
Example:- 
d1 = {["Mango","Banana"]:"Fruit", "Flower":["Rose", "Lotus"]}
print (d1)'''

''' You can assign a value to more than one keys in a dictionary, but a key cannot appear
more than once in a dictionary
Example:- '''
d1 = {"Banana":"Fruit", "Rose":"Flower", "Lotus":"Flower", "Mango":"Fruit"}
d2 = {"Fruit":"Banana","Flower":"Rose", "Fruit":"Mango", "Flower":"Lotus"}
print (d1)
print (d2)

''' Creating a Dictionary
You can create a dictionary in Python by placing a comma-separated sequence of key-
value pairs within curly braces {}, with a colon : separating each key and its associated
value. Alternatively, you can use the dict() function.
Example:-
The following example demonstrates how to create a dictionary called "student_info" using
both curly braces and the dict() function'''
# Creating a dictionary using curly braces
sports_player = {
"Name": "Sachin Tendulkar",
"Age": 48, 
"Sport": "Cricket"
}
print ("Dictionary using curly braces:", sports_player)
# Creating a dictionary using the dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():",student_info)

''' Accessing Dictionary Items
You can access the value associated with a specific key using square brackets [] or the
get() method'''
tudent_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing values using square brackets
name = student_info["name"]
print("Name:",name)
# Accessing values using the get() method
age = student_info.get("age")
print("Age:",age)

''' Modifying Dictionary Items
You can modify the value associated with a specific key or add a new key-value pair'''
student_info = {
"name": "Alice",
"age": 21,
"major": "Computer Science"
}
# Modifying an existing key-value pair
student_info["age"] = 22
# Adding a new key-value pair
student_info["graduation_year"] = 2023
print("The modified dictionary is:",student_info)

''' Removing Dictionary Items
You can remove items using the del statement, the pop() method, or the popitem()
method'''
student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "graduation_year": 2023
}
# Removing an item using the del statement
del student_info["major"]
# Removing an item using the pop() method
graduation_year = student_info.pop("graduation_year")
print(student_info)

''' Iterating Through a Dictionary
You can iterate through the keys, values, or key-value pairs in a dictionary using loops'''
student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "graduation_year": 2023
}
# Iterating through keys
for key in student_info:
    print("Keys:",key, student_info[key])
# Iterating through values
for value in student_info.values():
    print("Values:",value)
# Iterating through key-value pairs
for key, value in student_info.items():
    print("Key:Value:",key, value)

''' Properties of Dictionary Keys
Dictionary values have no restrictions. They can be any arbitrary Python object, either
standard objects or user-defined objects. However, same is not true for the keys.
There are two important points to remember about dictionary keys −

     More than one entry per key not allowed. Which means no duplicate key is allowed.
        When duplicate keys encountered during assignment, the last assignment wins. For
        example:- 
        ...
        dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
        print ("dict['Name']: ", dict['Name'])

        When the above code is executed, it produces the following result −
        dict['Name']: Manni
     Keys must be immutable. Which means you can use strings, numbers or tuples as
        dictionary keys but something like ['key'] is not allowed. Following is a simple
        example −
        ...
        dict = {['Name']: 'Zara', 'Age': 7}
        print ("dict['Name']: ", dict['Name'])

        When the above code is executed, it produces the following result −
        Traceback (most recent call last):
        File "test.py", line 3, in <module>
        dict = {['Name']: 'Zara', 'Age': 7};
        TypeError: unhashable type: 'list'
'''

'''
In Python, following operators are defined to be used with dictionary operands. In the
example, the following dictionary objects are used.
d1 = {'a': 2, 'b': 4, 'c': 30}
d2 = {'a1': 20, 'b1': 40, 'c1': 60}'''

'''
#--------------------------- [Python Dictionary Operators] ----------------------------
Operator                Description                     Example
---------------------------------------------------------------------------------------
dict[key]           Extract/assign the value mapped     print (d1['b']) retrieves 4
                        with key                        d1['b'] = 'Z' assigns new
                                                        value to key 'b'
                                                  
dict1|dict2         Union of two dictionary objects,    d3=d1|d2 ; print (d3)
                    returning new object                {'a': 2, 'b': 4, 'c': 30, 'a1':
                                                        20, 'b1': 40, 'c1': 60}

dict1|=dict2        Augmented dictionary union          d1|=d2; print (d1)
                    operator                            {'a': 2, 'b': 4, 'c': 30, 'a1':
                                                        20, 'b1': 40, 'c1': 60}
'''

'''
Python Dictionary Methods
Python includes following dictionary methods −
#-------------------------------- [Python Dictionary Methods] ----------------------------
Sr.No.           Function & Description
----------------------------------------------------------------------
1                          dict.clear()
                       Removes all elements of dictionary dict.
----------------------------------------------------------
2                          dict.copy()
                       Returns a shallow copy of dictionary dict.
----------------------------------------------------------
3                          dict.fromkeys()
                       Create a new dictionary with keys from seq and
                       values set to value.
----------------------------------------------------------
4                          dict.get(key, default=None)
                       For key key, returns value or default if key not in dictionary.
----------------------------------------------------------
5                          dict.has_key(key)
                       Returns true if a given key is available in
                       the dictionary, otherwise it returns a false.
----------------------------------------------------------
6                          dict.items()
                       Returns a list of dict's (key, value) tuple pairs.
----------------------------------------------------------
7                          dict.keys()
                       Returns list of dictionary dict's keys.
----------------------------------------------------------
8                          dict.pop()
                       Removes the element with specified key from the collection
----------------------------------------------------------
9                          dict.popitem()
                       Removes the last inserted key-value pair
----------------------------------------------------------
10                         dict.setdefault(key, default=None)
                       Similar to get(), but will set dict[key]=default if key is not
                       already in dict.
----------------------------------------------------------
11                         dict.update(dict2)
                       Adds dictionary dict2's key-values pairs to dict.
----------------------------------------------------------
12                         dict.values()
                       Returns list of dictionary dict's values.
----------------------------------------------------------'''

''' Built-in Functions with Dictionaries
Following are the built-in functions we can use with Dictionaries −


#-------------------------------- [Python Dictionary Built-in Functions] ----------------------------
Sr.No.           Function & Description 
----------------------------------------------------------------------
1                          cmp(dict1, dict2)
                      Compares elements of both dict.
----------------------------------------------------------
2                          len(dict)
                      Gives the total length of the dictionary. This would be equal
                      to the number of items in the dictionary.
----------------------------------------------------------
3                          str(dict)
                      Produces a printable string representation of a dictionary.
----------------------------------------------------------
4                          type(variable)
                      Returns the type of the passed variable. If passed variable is
                      dictionary, then it would return a dictionary type.
----------------------------------------------------------'''


'''----------------------- Access Dictionary Items --------------------------
Accessing dictionary items in Python involves retrieving the values associated with specific
keys within a dictionary data structure. Dictionaries are composed of key-value pairs,
where each key is unique and maps to a corresponding value.
There are various ways to access dictionary items in Python. They include −
     Using square brackets []
     The get() method
     Iterating through the dictionary using loops
     Or specific methods like keys(), values(), and items()
We will discuss each method in detail to understand how to access and retrieve data from
dictionaries'''

''' Access Dictionary Items Using Square Brackets []
Example 1:- 
In the following example, we are defining a dictionary named "capitals" where each key
represents a state and its corresponding value represents the capital city.
Then, we access and retrieve the capital cities of Gujarat and Karnataka using their
respective keys 'Gujarat' and 'Karnataka' from the dictionary'''

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar",
"Telangana":"Hyderabad", "Karnataka":"Bengaluru"}

print ("Capital of Gujarat is : ", capitals['Gujarat'])
print ("Capital of Karnataka is : ", capitals['Karnataka'])

''' Python raises a KeyError if the key given inside the square brackets is not present in the
dictionary object −
Example:- 
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar",
"Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Captial of Haryana is : ", capitals['Haryana'])
Output:-
KeyError: 'Haryana'
'''

''' Access Dictionary Items Using get() Method
The get() method in Python's dict class is used to retrieve the value associated with a
specified key. If the key is not found in the dictionary, it returns a default value (usually
None) instead of raising a KeyError.
Syntax:-    Val = dict.get("key")
            where, key is an immutable object used as key in the dictionary object.
Example 1:- 
In the example below, we are defining a dictionary named "capitals" where each key-value
pair maps a state to its capital city. Then, we use the get() method to retrieve the capital
cities of "Gujarat" and "Karnataka'''

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar",
"Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Gujarat is: ", capitals.get('Gujarat'))
print ("Capital of Karnataka is: ", capitals.get('Karnataka'))

''' Example 2
Unlike the "[]" operator, the get() method doesn't raise error if the key is not found; it
return None'''
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar",
"Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Haryana is : ", capitals.get('Haryana'))

''' Example 3:-
The get() method accepts an optional string argument. If it is given, and if the key is not
found, this string becomes the return value −'''

capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar",
"Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Capital of Haryana is : ", capitals.get('Haryana', 'Not found'))

''' Access Dictionary Keys
In a dictionary, keys are the unique identifiers associated with each value. They act as
labels or indices that allow you to access and retrieve the corresponding value. Keys are
immutable, meaning they cannot be changed once they are assigned. They must be of an
immutable data type, such as strings, numbers, or tuples.
We can access dictionary keys in Python using the keys() method, which returns a view
object containing all the keys in the dictionary.
Example:- 
In this example, we are retrieving all the keys from the dictionary "student_info" using the
keys() method'''

# Creating a dictionary with keys and values
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing all keys using the keys() method
all_keys = student_info.keys()
print("Keys:", all_keys)


''' Access Dictionary Values
In a dictionary, values are the data associated with each unique key. They represent the
actual information stored in the dictionary and can be of any data type, such as strings,
integers, lists, other dictionaries, and more. Each key in a dictionary maps to a specific
value, forming a key-value pair.
We can access dictionary values in Python using −
     Square Brackets ([]) − By providing the key inside the brackets.
     The get() Method − By calling the method with the key as an argument,
        optionally providing a default value.
     The values() Method − which returns a view object containing all the values in
        the dictionary
'''

'''Example 1
In this example, we are directly accessing associated with the key "name" and "age" using
the sqaure brackets
...
name = student_info["name"]'''

''' Example 2
Here, we use the get() method to retrieve the value of name key in "student_info" dictionary.
name = student_info.get("name")'''

''' Example 3
Now, we are retrieving all the values from the dictionary "student_info" using the values()
method'''
#Creating a dictionary with keys and values
student_info = {
"name": "Alice",
"age": 21,
"major": "Computer Science"
}
# Accessing all values using the values() method
all_values = student_info.values()
print("Values:", all_values)

''' Access Dictionary Items Using the items() Function
The items() function in Python is used to return a view object that displays a list of a
dictionary's key-value tuple pairs.

Example:- 
In the following example, we are using the items() function to retrieve all the key-value
pairs from the dictionary "student_info'''
# Creating a dictionary with student information
student_info = {
"name": "Alice",
"age": 21,
"major": "Computer Science"
}
# Using the items() method to get key-value pairs
all_items = student_info.items()
print("Items:", all_items)
# Iterating through the key-value pairs
print("Iterating through key-value pairs:")
for key, value in all_items:
    print(f"{key}: {value}")


'''-------------------------- Python - Change Dictionary Items ------------------
Changing dictionary items in Python refers to modifying the values associated with specific
keys within a dictionary. This can involve updating the value of an existing key, adding a
new key-value pair, or removing a key-value pair from the dictionary.
Dictionaries are mutable, meaning their contents can be modified after they are created'''

''' Modifying Dictionary Values
Modifying values in a Python dictionary refers to changing the value associated with an
existing key. To achieve this, you can directly assign a new value to that key.
Example:- 
In the following example, we are defining a dictionary named "person" with keys 'name',
'age', and 'city' and their corresponding values. Then, we modify the value associated with
the key 'age' to 26'''
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Modifying the value associated with the key 'age'
person['age'] = 26
print(person)

''' Updating Multiple Dictionary Values
If you need to update multiple values in a dictionary at once, you can use the update()
method. This method is used to update a dictionary with elements from another dictionary
or an iterable of key-value pairs.

Example:- 
In the example below, we are using the update() method to modify the values associated
with the keys 'age' and 'city' in the 'persons' dictionary'''

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Updating multiple values
person.update({'age': 26, 'city': 'Los Angeles'})
print(person)

''' Conditional Dictionary Modification
Conditional modification in a Python dictionary refers to changing the value associated
with a key only if a certain condition is met.
You can use an if statement to check whether a certain condition is true before modifying
the value associated with a key.
Example:- 
In this example, we conditionally modify the value associated with the key 'age' to '26' if
the current value is '25' in the 'persons' dictionary '''
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Conditionally modifying the value associated with 'age'
if person['age'] == 25:
    person['age'] = 26
print(person)


''' Modify Dictionary by Adding New Key-Value Pairs
Adding new key-value pairs to a Python dictionary refers to inserting a new key along with
its corresponding value into the dictionary.
This process allows you to dynamically expand the data stored in the dictionary by
including additional information as needed

Example: Using Assignment Operator
You can add a new key-value pair to a dictionary by directly assigning a value to a new
key as shown below. In the example below, the key 'city' with the value 'New York' is
added to the 'person' dictionary'''

# Initial dictionary
person = {'name': 'Alice', 'age': 25}
# Adding a new key-value pair 'city': 'New York'
person['city'] = 'New York'
print(person)

''' Example: Using the setdefault() Method
You can use the setdefault() method to add a new key-value pair to a dictionary if the key
does not already exist.
In this example, the setdefault() method adds the new key 'city' with the value 'New York'
to the 'person' dictionary only if the key 'city' does not already exist'''
# Initial dictionary
person = {'name': 'Alice', 'age': 25}
# Adding a new key-value pair 'city': 'New York'
person.setdefault('city', 'New York')
print(person)


''' Modify Dictionary by Removing Key-Value Pairs
Removing key-value pairs from a Python dictionary refers to deleting specific keys along
with their corresponding values from the dictionary.
This process allows you to selectively remove data from the dictionary based on the keys
you want to eliminate.

Example: Using the del Statement
You can use the del statement to remove a specific key-value pair from a dictionary. In
this example, the del statement removes the key 'age' along with its associated value from
the 'person' dictionary'''
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
del person['age']
print(person)


''' Example: Using the pop() Method
You can also use the pop() method to remove a specific key-value pair from a dictionary
and return the value associated with the removed key.'''

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
removed_age = person.pop('age')
print(person)
print("Removed age:", removed_age)

''' Example: Using the popitem() Method
You can use the popitem() method as well to remove the last key-value pair from a
dictionary and return it as a tuple'''
# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the last key-value pair
removed_item = person.popitem()
print(person)
print("Removed item:", removed_item)


'''------------------------------ Python - Add Dictionary Items ------------------------
Adding dictionary items in Python refers to inserting new key-value pairs into an existing
dictionary.
Adding items to a dictionary allows you to dynamically update and expand its contents as
needed during program execution.
We can add dictionary items in Python using various ways such as
     Using square brackets
     Using the update() method
     Using a comprehension
     Using unpacking
     Using the Union Operator
     Using the |= Operator
     Using setdefault() method
     Using collections.defaultdict() method'''

''' Add Dictionary Item Using Square Brackets
The square brackets [] in Python is used to access elements in sequences like lists and
strings through indexing and slicing operations. Additionally, when working with
dictionaries, square brackets are used to specify keys for accessing or modifying
associated values.
If the key is already present in the dictionary object, its value will
be updated to val. If the key is not present in the dictionary, a new key-value pair will be
added.
Example:- To add or modify the key named "Kavya", the following code can be used:
marks['Kavya'] = 58'''

''' Add Dictionary Item Using the update() Method
The update() method in Python dictionaries is used to merge the contents of another
dictionary or an iterable of key-value pairs into the current dictionary. It adds or updates
key-value pairs, ensuring that existing keys are updated with new values and new keys
are added to the dictionary.
You can add multiple items to a dictionary using the update() method by passing another
dictionary or an iterable of key-value pairs
Example:- '''
marks = {"Savita":67, "Imtiaz":88}
print ("Initial dictionary: ", marks)
marks.update({'Kavya': 58, 'Mohan': 98})
print ("Dictionary after new addition: ", marks)

''' Add Dictionary Item Using Unpacking
Unpacking in Python refers to extracting individual elements from a collection, such as a
list, tuple, or dictionary, and assigning them to variables in a single statement. This can
be done using the * operator for iterables like lists and tuples, and the ** operator for
dictionaries.
We can add dictionary items using unpacking by combining two or more dictionaries with
the ** unpacking operator
Example:- 
In the example below, we are initializing two dictionaries named "marks" and "marks1",
both containing names and their corresponding integer values. Then, we create a new
dictionary "newmarks" by merging "marks" and "marks1" using dictionary unpacking −'''

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = {**marks, **marks1}
print ("marks dictionary after update: \n", newmarks)

''' Add Dictionary Item Using the Union Operator (|)
The union operator in Python, represented by the | symbol, is used to combine the
elements of two sets into a new set that contains all the unique elements from both sets.
It can also be used with dictionaries in Python 3.9 and later to merge the contents of two
dictionaries.
Example:- 
In this example, we are using the | operator to combine the dictionaries "marks" and
"marks1" with "marks1" values taking precedence in case of duplicate keys'''

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = marks | marks1
print ("marks dictionary after update: \n", newmarks)

''' Add Dictionary Item Using the "|=" Operator
The |= operator in Python is an in-place union operator for sets and dictionaries. It updates
the set or dictionary on the left-hand side with elements from the set or dictionary on the
right-hand side.
If there are overlapping keys, the values from the right-hand dictionary will overwrite 
those in the left-hand dictionary.
Example:- 
In the following example, we use the |= operator to update "marks" with the key-value
pairs from "marks1", with values from "marks1" taking precedence in case of duplicate
keys −'''

marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
marks |= marks1
print ("marks dictionary after update: \n", marks)

''' Add Dictionary Item Using the setdefault() Method
The setdefault() method in Python is used to get the value of a specified key in a dictionary.
If the key does not exist, it inserts the key with a specified default value.
Example:- 
In this example, we use the setdefault() to add the key-value pair "major": "Computer
Science" to the "student" dictionary'''

# Initial dictionary
student = {"name": "Alice", "age": 21}
# Adding a new key-value pair
major = student.setdefault("major", "Computer Science")
print(student)

''' Add Dictionary Item Using the collections.defaultdict() Method
The collections.defaultdict() method in Python is a subclass of the built-in "dict" class that
creates dictionaries with default values for keys that have not been set yet. It is part of
the collections module in Python's standard library.

When accessing a missing key for the first time, the default factory is called to create a
default value, and this value is inserted into the dictionary
Example:- 
In this example, we are initializing instances of defaultdict with different default factories:
int to initialize missing keys with 0, list to initialize missing keys with an empty list, and a
custom function default_value to initialize missing keys with the return value of the
function
'''
from collections import defaultdict
# Using int as the default factory to initialize missing keys with 0
d = defaultdict(int)
# Incrementing the value for key 'a'
d["a"] += 1
print(d)
# Using list as the default factory to initialize missing keys with an empty
list
d = defaultdict(list)
# Appending to the list for key 'b'
d["b"].append(1)
print(d)
# Using a custom function as the default factory
def default_value():
    return "N/A"
d = defaultdict(default_value)
print(d["c"])

'''------------------------------- Python - Remove Dictionary Items ------------------------
Remove Dictionary Items Removing dictionary items in Python refers to deleting key-value pairs from an existing
dictionary.
We can remove dictionary items in Python using various ways such as −
     using the del keyword
     using the pop() method
     using the popitem() method
     using the clear() method
     using dictionary comprehension
'''

''' Remove Dictionary Items Using del Keyword
The del keyword in Python is used to delete objects. In the context of dictionaries, it is
used to remove an item or a slice of items from the dictionary, based on the specified
key(s).
Example 1:- 
In the following example, we are creating a dictionary named numbers with integer keys
and their corresponding string values. Then, delete the item with the key '20' using the
del keyword'''
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before delete operation: \n", numbers)
del numbers[20]
print ("numbers dictionary before delete operation: \n", numbers)

''' The del keyword, when used with a dictionary object, removes the dictionary from memory
Example:- '''
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before delete operation: \n", numbers)
del numbers
print ("numbers dictionary before delete operation: \n", numbers)

''' Remove Dictionary Items Using pop() Method
The pop() method in Python is used to remove a specified key from a dictionary and return
the corresponding value. If the specified key is not found, it can optionally return a default
value instead of raising a KeyError.

Example:-
In this example, we are using the pop() method to remove the item with the key '20'
(storing its value in val) from the 'numbers' dictionary. We then retrieve the updated
dictionary and the popped value'''

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before pop operation: \n", numbers)
val = numbers.pop(20)
print ("nubvers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)

''' Remove Dictionary Items Using popitem() Method
The popitem() method in Python is used to remove and return the last key-value pair from
a dictionary.
Since Python 3.7, dictionaries maintain the insertion order, so popitem()
removes the most recently added item. If the dictionary is empty, calling
popitem() raises a KeyError.
Example:- '''
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before pop operation: \n", numbers)
val = numbers.popitem()
print ("numbers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)

''' Remove Dictionary Items Using clear() Method
The clear() method in Python is used to remove all items from a dictionary. It effectively
empties the dictionary, leaving it with a length of 0.

Example:- '''
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("numbers dictionary before clear method: \n", numbers)
numbers.clear()
print ("numbers dictionary after clear method: \n", numbers)

''' Remove Dictionary Items using Dictionary Comprehension
Dictionary comprehension is a concise way to create dictionaries in Python. It follows the
same syntax as list comprehension but generates dictionaries instead of lists. With
dictionary comprehension, you can iterate over iterable objects (such as lists, tuples, or
other dictionaries), apply an expression to each item, and construct key-value pairs based
on the result of that expression.
We cannot directly remove dictionary items using dictionary comprehension.
Dictionary comprehension is primarily used for creating new dictionaries based
on some transformation or filtering of existing data, rather than for removing
items from dictionaries.
If you need to remove items from a dictionary based on certain conditions, you would
typically use other methods like del, pop(), or popitem(). These methods allow you to
explicitly specify which items to remove from the dictionary.
Example:-
In this example, we remove items 'age' and 'major' from the 'student_info' dictionary
based on a predefined list of keys to remove'''

# Creating a dictionary
student_info = {
"name": "Alice",
"age": 21,
"major": "Computer Science"
}
# Removing items based on conditions
keys_to_remove = ["age", "major"]
for key in keys_to_remove:
    student_info.pop(key, None)
print(student_info)

'''------------------------------------ Python - Dictionary View Objects ------------------------
The items(), keys(), and values() methods of dict class return view objects. These views
are refreshed dynamically whenever any change occurs in the contents of their source
dictionary object.
The items() Method
    The items() method returns a dict_items view object. It contains a list of tuples, each tuple
    made up of respective key, value pairs.
Syntax:-  Obj = dict.items()
            Return value
            The items() method returns dict_items object which is a dynamic view of (key,value)
            tuples.
Example:- 
In the following example, we first obtain the dict_items object with items() method and
check how it is dynamically updated when the dictionary object is updated'''

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.items()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)

''' The keys() Method
The keys() method of dict class returns dict_keys object which is a list of all keys defined
in the dictionary. It is a view object, as it gets automatically updated whenever any update
action is done on the dictionary object.
Syntax Obj = dict.keys()
            Return value
            The keys() method returns dict_keys object which is a view of keys in the dictionary.
Example
In this example, we are creating a dictionary named "numbers" with integer keys and their
corresponding string values. Then, we obtain a view object "obj" of the keys using the
keys() method, and retrieve its type and content −'''

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.keys()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)

''' The values() Method
The values() method returns a view of all the values present in the dictionary. The object
is of dict_value type, which gets automatically updated.
Syntax:- Obj = dict.values()
            Return value
            The values() method returns dict_values object which is a view of values in the dictionary.
Example:- 
In the example below, we obtain a view object "obj" of the values using the values()
method from the "numbers" dictionary '''
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.values()
print ('type of obj: ', type(obj))
print (obj)
print ("update numbers dictionary")
numbers.update({50:"Fifty"})
print ("View automatically updated")
print (obj)

'''-------------------------------------- Python - Loop Dictionaries -------------------
Loop Through Dictionaries
Looping through dictionaries in Python refers to iterating over key-value pairs within the
dictionary and performing operations on each pair. This allows you to access both keys
and their corresponding values. There are several ways/methods for looping through
dictionaries −
     Using a for Loop
     Using dict.items() method
     Using dict.keys() method
     Using dict.values() method
'''
''' Loop Through Dictionary Using a For Loop
A for loop in Python is a control flow statement that iterates over a sequence of elements.
It repeatedly executes a block of code for each item in the sequence. The sequence can
be a range of numbers, a list, a tuple, a string, or any iterable object.
1> Iterating over Keys
    In this approach, the loop iterates over the keys of the dictionary. Inside the loop, you can
    access the value corresponding to each key using dictionary indexing
    Example:-
        student = {"name": "Alice", "age": 21, "major": "Computer Science"}
        for key in student:
            print(key, student[key])
2>  Iterating over Key-Value Pairs
    In this approach, the loop iterates over the key-value pairs using the items() method of
    the dictionary. Each iteration provides both the key and its corresponding value
    Example:- 
        student = {"name": "Alice", "age": 21, "major": "Computer Science"}
        for key, value in student.items():
            print(key, value)'''

''' Loop through Dictionary Using dict.items() Method
The dict.items() method in Python is used to return a view object that displays a list of
key-value pairs in the dictionary. 
Example:-
'''
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
# Looping through key-value pairs
for key, value in student.items():
    print(key, value)

''' Loop through Dictionary Using dict.keys() Method
The dict.keys() method in Python is used to return a view object that displays a list of keys
in the dictionary. 
Example:- '''
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
# Looping through keys
for key in student.keys():
    print(key)

''' Loop through Dictionary Using dict.values() Method
The dict.values() method in Python is used to return a view object that displays a list of
values in the dictionary. 
Example:- '''
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
# Looping through values
for value in student.values():
    print(value)

'''--------------------------------- Python - Copy Dictionaries -----------------------
Copying dictionaries in Python refers to creating a new dictionary that contains the same
key-value pairs as the original dictionary.
We can copy dictionaries using various ways, depending on the requirements and the
nature of the dictionary's values (whether they are mutable or immutable, nested or not).
Shallow Copy
    When you perform a shallow copy, a new dictionary object is created, but it contains
    references to the same objects as the original dictionary references.
    This is useful when you want to duplicate the structure of a dictionary without duplicating
    the nested objects it contains.
    This can be done using the copy() method or the dict() function as shown below −
Example: Using the copy() Method
In the following example, we can see that changing the "age" in the shallow copy does not
affect the original.
However, modifying the list in the shallow copy also affects the original because the list is
a mutable object and only a reference is copied.'''
original_dict = {"name": "Alice", "age": 25, "skills": ["Python", "Data Science"]}
shallow_copy = original_dict.copy()
# Modifying the shallow copy
shallow_copy["age"] = 26
shallow_copy["skills"].append("Machine Learning")
print("Original dictionary:", original_dict)
print("Shallow copy:", shallow_copy)

''' Example: Using the dict() Method
Similar to the copy() method, the dict() method creates a shallow copy as shown in the
example below-'''
original_dict = {"name": "Bob", "age": 30, "skills": ["Java", "C++"]}
shallow_copy = dict(original_dict)
# Modifying the shallow copy
shallow_copy["age"] = 31
shallow_copy["skills"].append("C#")
print("Original dictionary:", original_dict)
print("Shallow copy:", shallow_copy)

''' Deep Copy
A deep copy creates a new dictionary and recursively copies all objects found in the original
dictionary. This means that not only the dictionary itself but also all objects it contains
(including nested dictionaries, lists, etc.) are copied. As a result, changes made to the
deep copy do not affect the original dictionary and vice versa.
We can achieve this using the deepcopy() function in the copy module.
Example:-
We can see in the example below that the "age" value in the deep copy is changed, the
"skills" list in the deep copy is modified (an item is appended) and the "education"
dictionary in the deep copy is modified, all without affecting the original'''

import copy
original_dict = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Science"],
    "education": {
    "degree": "Bachelor's",
    "field": "Computer Science"
}
}
# Creating a deep copy
deep_copy = copy.deepcopy(original_dict)
# Modifying the deep copy
deep_copy["age"] = 26
deep_copy["skills"].append("Machine Learning")
deep_copy["education"]["degree"] = "Master's"
# Retrieving both dictionaries
print("Original dictionary:", original_dict)
print("Deep copy:", deep_copy)


'''------------------------------------------- Python - Nested Dictionaries -------------------------
Nested dictionaries in Python refer to dictionaries that are stored as values within another
dictionary. In other words, a dictionary can contain other dictionaries as its values, forming
a hierarchical or nested structure.
Nested dictionaries can be modified, updated, or extended in the same way as regular
dictionaries. You can add, remove, or update key-value pairs at any level of the nested
structure'''

''' Creating a Nested Dictionary in Python
We can create a nested dictionary in Python by defining a dictionary where the values of
certain keys are themselves dictionaries. This allows for the creation of a hierarchical
structure where each key-value pair represents a level of nested information. This can be
achieved in several ways −

Example: Direct Assignment
In this approach, we can directly assign dictionaries as values to outer keys within a single
dictionary definition'''
# Define the outer dictionary
nested_dict = {
"outer_key1": {"inner_key1": "value1", "inner_key2": "value2"},
"outer_key2": {"inner_key3": "value3", "inner_key4": "value4"}
}
print(nested_dict)

'''Example: Using a Loop
With this method, an empty outer dictionary is initialized, and then populated with
dictionaries as values using a loop to define nested dictionaries −'''
# Define an empty outer dictionary
nested_dict = {}
# Add key-value pairs to the outer dictionary
outer_keys = ["outer_key1", "outer_key2"]
for key in outer_keys:
    nested_dict[key] = {"inner_key1": "value1", "inner_key2": "value2"}
print(nested_dict)

''' Adding Items to a Nested Dictionary in Python
Once a nested dictionary is created, we can add items to it by accessing the specific nested
dictionary using its key and then assigning a new key-value pair to it.
In the following example, we are defining a nested dictionary "students" where each key
represents a student's name and its value is another dictionary containing details about
the student.
Then, we add a new key-value pair to Alice's nested dictionary and add a new nested
dictionary for a new student, Charlie'''
# Initial nested dictionary
students = {
"Alice": {"age": 21, "major": "Computer Science"},
"Bob": {"age": 20, "major": "Engineering"}
}
# Adding a new key-value pair to Alice's nested dictionary
students["Alice"]["GPA"] = 3.8
# Adding a new nested dictionary for a new student
students["Charlie"] = {"age": 22, "major": "Mathematics"}
print(students)

''' Accessing Items of a Nested Dictionary in Python
Accessing items of a nested dictionary in Python refers to retrieving values stored within
the nested structure by using a series of keys. Each key corresponds to a level in the
hierarchy of the dictionary.
We can achieve this through direct indexing with square brackets or by using the get()
method
Example: Using Direct Indexing
In this approach, we access values in a nested dictionary by specifying each key in a
sequence of square brackets. Each key in the sequence refers to a level in the nested
dictionary, progressing one level deeper with each key'''
# Define a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}
# Access Alice's major
alice_major = students["Alice"]["major"]
print("Alice's major:", alice_major)
# Access Bob's age
bob_age = students["Bob"]["age"]
print("Bob's age:", bob_age)

''' Example: Using the get() Method
The get() method is used to fetch the value associated with the specified key. If the key
does not exist, it returns a default value (which is None if not specified) −'''

# Define a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}
# Access Alice's major using .get()
alice_major = students.get("Alice", {}).get("major", "Not Found")
print("Alice's major:", alice_major)
# Safely access a non-existing key using .get()
dave_major = students.get("Dave", {}).get("major", "Not Found")
print("Dave's major:", dave_major)

''' Deleting a Dictionary from a Nested Dictionary
We can delete dictionaries from a nested dictionary by using the del keyword. This keyword
allows us to remove a specific key-value pair from the nested dictionary.
Example
In the following example, we delete the nested dictionary for "Bob" from "students"
dictionary using the del statemen'''
# Define a nested dictionary
students = {
"Alice": {"age": 21, "major": "Computer Science"},
"Bob": {"age": 20, "major": "Engineering"},
"Charlie": {"age": 22, "major": "Mathematics"}
}
# Delete the dictionary for Bob
del students["Bob"]
# Print the updated nested dictionary
print(students)

''' Iterating Through a Nested Dictionary in Python
Iterating through a nested dictionary refers to looping through the keys and values at each
level of the dictionary. This allows you to access and manipulate items within the nested
structure.
Example
In this example, we are iterating through the "students" dictionary, retrieving each
student's name and their corresponding details by iterating through the nested dictionaries'''

# Defining a nested dictionary
students = {
"Alice": {"age": 21, "major": "Computer Science"},
"Bob": {"age": 20, "major": "Engineering"},
"Charlie": {"age": 22, "major": "Mathematics"}
}
# Iterating through the Nested Dictionary:
for student, details in students.items():
    print(f"Student: {student}")
    for key, value in details.items():
        print(f" {key}: {value}")

'''----------------------------------- Python - Dictionary Methods ---------------------------'''        
'''A Python dictionary is an object of the built-in dict class, which defines the following
methods

#-------------------------------- [Dictionary Methods] ----------------------------
Sr.No.           Function & Description 
----------------------------------------------------------------------
1                          dict.clear()
                        Removes all elements of dictionary dict.
----------------------------------------------------------
2                          dict.copy()
                        Returns a shallow copy of dictionary dict.
----------------------------------------------------------
3                          dict.fromkeys()
                        Create a new dictionary with keys from seq and
                        values set to value.
----------------------------------------------------------
4                          dict.get(key, default=None)
                        For key key, returns value or default if key not
                        in dictionary.
----------------------------------------------------------
5                          dict.has_key(key)
                        Returns true if a given key is available in the
                        dictionary, otherwise it returns a false.
----------------------------------------------------------
6                          dict.items()
                        Returns a list of dict's (key, value) tuple pairs.
----------------------------------------------------------
7                          dict.keys()
                        Returns list of dictionary dict's keys.
----------------------------------------------------------
8                          dict.pop()
                        Removes the element with specified key from the
                        collection.
----------------------------------------------------------
9                          dict.popitem()
                        Removes the last inserted key-value pair.
----------------------------------------------------------
10                         dict.setdefault(key, default=None)
                        Similar to get(), but will set dict[key]=default if
                        key is not already in dict.
----------------------------------------------------------
11                         dict.update(dict2)
                        Adds dictionary dict2's key-values pairs to dict.
----------------------------------------------------------
12                         dict.values()
                        Returns list of dictionary dict's values.
----------------------------------------------------------'''
