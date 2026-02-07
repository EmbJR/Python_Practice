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
                      Returns true if key in dictionary dict, false otherwise.
----------------------------------------------------------
6                          dict.items()
                      Returns a list of dict's (key, value) tuple pairs.
----------------------------------------------------------
7                          dict.keys()
                      Returns list of dictionary dict's keys.
----------------------------------------------------------
8                          dict.setdefault(key, default=None)
                      Similar to get(), but will set dict[key]=default if key is not
                      already in dict.
----------------------------------------------------------
9                          dict.update(dict2)
                      Adds dictionary dict2's key-values pairs to dict.
----------------------------------------------------------
10                         dict.values()
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

'''------------------------------- Python - Remove Dictionary Items ------------------------'''