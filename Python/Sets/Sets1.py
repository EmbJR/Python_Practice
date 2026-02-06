'''------------------------- Sets in Python ---------------------   
In Python, a set is an unordered collection of unique elements. Unlike lists or tuples, sets
do not allow duplicate values i.e. each element in a set must be unique. Sets are mutable,
meaning you can add or remove items after a set has been created.
Sets are defined using curly braces {} or the built-in set() function. They are particularly
useful for membership testing, removing duplicates from a sequence, and performing
common mathematical set operations like union, intersection, and difference.'''

''' Creating a Set in Python 
You can create a set in Python using curly braces {} or the set() function −

Using Curly Braces
You can directly define a set by listing its elements within curly braces, separating each
element by a comma as shown below 
Example:- '''
my_set = {1, 2, 3, 4, 5}
print (my_set)
''' Using the set() Function
Alternatively, you can create a set using the set() function by passing an iterable (like a
list or a tuple) containing the elements you want to include in the set
Example:- '''
my_set = set([1, 2, 3, 4, 5])
print (my_set)

''' Duplicate Elements in Set
Sets in Python are unordered collections of unique elements. If you try to create a set with
duplicate elements, duplicates will be automatically removed
Example:- '''
my_set = {1, 2, 2, 3, 3, 4, 5, 5}
print (my_set)
''' Sets can contain elements of different data types, including numbers, strings, and even
other sets (as long as they are immutable)
Example:- 
mixed_set = {1, 'hello', (1, 2, 3)}
print (mixed_set)'''

''' Adding Elements in a Set
To add an element to a set, you can use the add() function. If the element is already present in the set,
the set remains unchanged −'''
my_set = {1, 2, 3, 3}
# Adding an element 4 to the set
my_set.add(4)
print (my_set)

''' Removing Elements from a Set
You can remove an element from a set using the remove() function. If the element is not present, a
KeyError is raised −'''
my_set.remove(3)
print (my_set)
''' Alternatively, you can use the discard() function to remove an element from the set if it is
present. Unlike remove(), discard() does not raise an error if the element is not found in
the set −'''
my_set = {1, 2, 3, 4}
# No error even if 5 is not in the set
my_set.discard(5)
print (my_set)

''' Membership Testing in a Set 
Example:- '''
my_set = {1, 2, 3, 4}
if 2 in my_set:
    print("2 is present in the set")
else:
    print("2 is not present in the set")

''' Set Operations
In Python, sets support various set operations, which is used to manipulate and compare
sets. These operations are described below. Sets are particularly useful when dealing with 
collections of unique elements and performing operations based on set theory.
     Union − 
    It combines elements from both sets using the union() function or the | operator.
     Intersection − 
    It is used to get common elements using the intersection() function or the & operator.
     Difference − 
    It is used to get elements that are in one set but not the other using the difference() function or the - operator.
     Symmetric Difference − 
    It is used to get elements that are in either of the sets but not in both using the symmetric_difference() method or the ^ operator'''

''' Python Set Comprehensions
Set comprehensions in Python is a concise way to create sets based on iterable objects,
similar to list comprehensions
Syntax
The syntax for set comprehensions is similar to list comprehensions, but instead of square
brackets [ ], you use curly braces { } to denote a set −
set_variable = {expression for item in iterable if condition}'''
''' Example
In the following example, we are creating a set containing the squares of numbers from 1
to 5 using a set comprehension −'''
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)

''' Filtering Elements Using Set Comprehensions
You can include conditional statements in set comprehensions to filter elements based on
certain criteria. For instance, to create a set of even numbers from 1 to 10, you can use a
set comprehension with an if condition as shown below'''
even_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_set)

''' Nested Set Comprehensions
Set comprehensions also support nested loops, allowing you to create sets from nested
iterables. This can be useful for generating combinations or permutations of elements.
Example:- '''
nested_set = {(x, y) for x in range(1, 3) for y in range(1, 3)}
print(nested_set)

''' Frozen Sets
In Python, a frozen set is an immutable collection of unique elements, similar to a regular
set but with the distinction that it cannot be modified after creation. Once created, the
elements within a frozen set cannot be added, removed, or modified, making it a suitable
choice when you need an immutable set.
Example:- 
In the following example, we are creating a frozen set of integers and then adding an
element to it'''
my_frozen_set = frozenset([1, 2, 3])
print(my_frozen_set)
# we cannot add to this set by "my_frozen_set.add(4)". It will throw an error

'''-------------------------- Access Set Items ------------------------------
The primary way to access set items is by traversing the set using a loop, such as a for
loop.
In Python, sets are unordered collections of unique elements, and unlike sequences (such
as lists or tuples), sets do not have a positional index for their elements. This means that
you cannot access individual elements of a set directly by specifying an index.'''


''' Access Set Items Using List Comprehension
Example:- '''
my_set = {1, 2, 3, 4, 5}
# Accessing set items using list comprehension
accessed_items = [item for item in my_set]
print(accessed_items)

''' Access Subset from a Set
Mathematically, a subset is a set that contains only elements that are also contained in
another set. In other words, every element of the subset is also an element of the original
set. If every element of set A is also an element of set B, then A is considered a subset of
B, denoted as A ⊆ B.
In Python, you can access subsets from a set using set operations or by iterating over the
power set (the set of all subsets) and filtering based on specific criteria.
     Using Set Operations − You can use built-in set operations such as issubset()
        function to check if one set is a subset of another.
     Iterating Over Power Set − Iterate over all possible subsets of the set and filter
        based on certain criteria to access specific subsets
Example
Following is the basic example demonstrating how to access subsets from a set −
'''
import itertools
# Defining a set
original_set = {1, 2, 3, 4}
# Checking if {1, 2} is a subset of the original set
is_subset = {1, 2}.issubset(original_set)
print("{1, 2} is a subset of the original set:", is_subset)
# Generating all subsets with two elements
subsets_with_two_elements = [set(subset) for subset in
itertools.combinations(original_set, 2)]
print("Subsets with two elements:", subsets_with_two_elements)

''' Checking if Set Item Exists
You can check whether a certain item available in the set is using the Python's membership
operators, in and not in.
Example:- 
In the below example, the "in" operator verifies whether the item "Java" exists in the set
"langs", and the "not in" operator checks whether the item "SQL" does not exist in the se'''
# Defining a set
langs = {"C", "C++", "Java", "Python"}
# Checking if an item exists in the set
if "Java" in langs:
    print("Java is present in the set.")
else:
    print("Java is not present in the set.")
# Checking if an item does not exist in the set
if "SQL" not in langs:
    print("SQL is not present in the set.")
else:
    print("SQL is present in the set.")

'''-------------------------- Add Set Items ----------------------
Adding set items means adding new elements into an existing set. In Python, sets are
mutable, which means you can modify them after they have been created. While the
elements within a set are immutable (such as integers, strings, or tuples), the set itself
can be modified.
You can add items to a set using various methods, such as add(), update(), or set
operations like union (|) and set comprehension.

One of the defining features of sets is their ability to hold only immutable
(hashable) objects. This is because sets internally use a hash table for fast
membership testing. Immutable objects are hashable, meaning they have a hash
value that never changes during their lifetime'''

''' Add Set Items using the add() Method
The add() method in Python is used to add a single element to the set
If the element is already in the set, the add() method does not make any changes in the set.
Syntax:- set.add(obj)
Example:- 
In the following example, we are initializing an empty set called "language" and adding
elements to it using the add() method'''
# Defining an empty set
language = set()
# Adding elements to the set using add() method
language.add("C")
language.add("C++")
language.add("Java")
language.add("Python")
# Printing the updated set
print("Updated Set:", language)

''' Add Set Items using the update() Method
In Python, the update() method of set class is used to add multiple elements to the set.
The elements in the iterable are inserted into the set if they
are not already present.
Syntax:- set.update(obj)
    Where, obj is a set or a sequence object (list, tuple, string).

Example:- Adding a Single Set Item
In the example below, we initialize a set called "my_set". Then, we use the update()
method to add the element "4" to the set'''
# Define a set
my_set = {1, 2, 3}
# Adding element to the set
my_set.update([4])
# Print the updated set
print("Updated Set:", my_set)

''' Adding any Sequence Object as Set Items
The update() method also accepts any sequence object as argument.
Example:- 
In this example, we first define a set and a tuple, lang1 and lang2, containing different
programming languages. Then, we add all elements from "lang2" to "lang1" using the
update() method'''
# Defining a set
lang1 = {"C", "C++", "Java", "Python"}
# Defining a tuple
lang2 = {"PHP", "C#", "Perl"}
lang1.update(lang2)
print (lang1)

''' Example
In this example, a set is constructed from a string, and another string is used as argument
for update() method'''
set1 = set("Hello")
set1.update("World")
print (set1)

''' Add Set Items using Union Operator
In Python, the union operator (|) is used to perform a union operation between two sets.
The union of two sets contains all the distinct elements present in either of the sets,
without any duplicates.
Example:- 
The following example combine sets using the union() method and the | operator to create
new sets containing unique elements from the original sets '''
# Defining three sets
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = {"SQL", "C#"}
# Performing union operation
combined_set1 = lang1.union(lang2)
combined_set2 = lang2 | lang3
# Print the combined set
print ("Combined Set1:", combined_set1)
print("Combined Set2:", combined_set2)
''' If a sequence object is given as argument to union() method, Python automatically
converts it to a set first and then performs union 
Example:- '''
lang1 = {"C", "C++", "Java", "Python"}
lang2 = ["PHP", "C#", "Perl"]
lang3 = lang1.union(lang2)
print (lang3)

''' Add Set Items Using Set Comprehension
In Python, set comprehension is a way to create sets using a single line of code
We can add set items using set comprehension by iterating over an iterable, applying an
expression to each element, and enclosing the comprehension expression within curly
braces {} to generate a new set containing the results of the expression applied to each
element.
Example:- 
In the following example, we are defining a list of integers and then using set
comprehension to generate a set containing the squares of those integers'''
# Defining a list containing integers
numbers = [1, 2, 3, 4, 5]
# Creating a set containing squares of numbers using set comprehension
squares_set = {num ** 2 for num in numbers}
# Printing the set containing squares of numbers
print("Squares Set:", squares_set)

''' Remove Set Items Removing set items implies deleting elements from a set'''

''' Remove Set Item Using remove() Method
The remove() method in Python is used to remove the first occurrence of a specified item
from a set.
We can remove set items using the remove() method by specifying the element we want
to remove from the set. If the element is present in the set, it will be removed. However,
if the element is not found, the remove() method will raise a KeyError exception.
Example:- 
In the following example, we are deleting the element "Physics" from the set "my_set"
using the remove() method'''
my_set = {"Rohan", "Physics", 21, 69.75}
print ("Original set: ", my_set)
my_set.remove("Physics")
print ("Set after removing: ", my_set)
# my_set.remove("PHP") will raise an error since "PHP" is not present in the set

''' Remove Set Item Using discard() Method
The discard() method in set class is similar to remove() method. The only difference is, it
doesn't raise error even if the object to be removed is not already present in the set
collection.
Example:- 
In this example, we are using the discard() method to delete an element from a set
regardless of whether it is present or not'''
my_set = {"Rohan", "Physics", 21, 69.75}
print ("Original set: ", my_set)
# removing an existing element
my_set.discard("Physics")
print ("Set after removing Physics: ", my_set)
# removing non-existing element
my_set.discard("PHP")
print ("Set after removing non-existent element PHP: ", my_set)

''' Remove Set Item Using pop() Method
We can also remove set items using the pop() method by removing and returning an
arbitrary element from the set. If the set is empty, the pop() method will raise a KeyError
exception.
Example:- 
In the example below, we are defining a set with elements "1" through "5" and removing
an arbitrary element from it using the pop() method'''
my_set = {1, 2, 3, 4, 5}
# removing and returning an arbitrary element from the set
removed_element = my_set.pop()  # this clould raise an error if the set is empty
# Printing the removed element and the updated set
print("Removed Element:", removed_element)
print("Updated Set:", my_set)

''' Remove Set Item Using clear() Method
The clear() method in set class removes all the items in a set object, leaving an empty
set
Example:- '''
my_set = {1, 2, 3, 4, 5}
# removing all the elements in the set
my_set.clear()
print("Set after removing all elements: ", my_set)

''' Remove Items Existing in Both Sets
You can remove items that exist in both sets (i.e., the intersection of two sets) using the
difference_update() method or the subtraction operator (-=). This removes all elements
that are present in both sets from the original set.
Example:-
In this example, we are defining two sets "s1" and "s2", and then using the
difference_update() method to remove elements from "s1" that are also in "s2"'''

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1 before running difference_update: ", s1)
s1.difference_update(s2)
print ("s1 after running difference_update: ", s1)

''' Remove Items Existing in Either of the Sets
To remove items that exist in either of two sets, you can use the symmetric difference
operation. The symmetric difference between two sets results in a set containing elements
that are in either of the sets but not in their intersection.
In Python, the symmetric difference operation can be performed using the ^ operator or
symmetric_difference() method.
Example:-
In the following example, we are defining two sets "set1" and "set2". We are then using
the symmetric difference operator (^) to create a new set "result_set" containing elements
that are in either "set1" or "set2" but not in both'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Removing items that exist in either set
result_set = set1 ^ set2
print("Resulting Set:", result_set)

''' Remove Uncommon Set Items
You can remove uncommon items between two sets using the intersection_update()
method. The intersection of two sets results in a set containing only the elements that are
present in both sets.
To keep only the common elements in one of the original sets and remove the uncommon
ones, you can update the set with its intersection.
Example:- 
In this example, we are defining two sets "set1" and "set2". We are then using the
intersection_update() method to modify "set1" so that it only contains elements that are
also in "set2"'''
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Keeping only common items in set1
set1.intersection_update(set2)
print("Set 1 after keeping only common items:", set1)

''' The intersection() Method
The intersection() method in set class is similar to its intersection_update() method,
except that it returns a new set object that consists of items common to existing sets.
Syntax:- set.intersection(obj)
Where, obj is a set object. Return value

The intersection() method returns a set object, retaining only those items common in itself
and obj.
Example:- 
In the following example, we are defining two sets "s1" and "s2", then using the
intersection() method to create a new set "s3" containing elements that are common to
both "s1" and "s2"'''
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.intersection(s2)
print ("s3 = s1 & s2: ", s3)

'''Symmetric Difference Update of Set Items
The symmetric difference between two sets is the collection of all the uncommon items,
rejecting the common elements. The symmetric_difference_update() method updates a
set with symmetric difference between itself and the set given as argument.
Example:- 
In the example below, we are defining two sets "s1" and "s2", then using the
symmetric_difference_update() method to modify "s1" so that it contains elements that
are in either "s1" or "s2", but not in both'''
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s1.symmetric_difference_update(s2)
print ("s1 after running symmetric difference ", s1)

''' Symmetric Difference of Set Items
The symmetric_difference() method in set class is similar to
symmetric_difference_update() method, except that it returns a new set object that holds
all the items from two sets minus the common items.
Example:-
In the following example, we are defining two sets "s1" and "s2". We are then using the
symmetric_difference() method to create a new set "s3" containing elements that are in
either "s1" or "s2", but not in both'''
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.symmetric_difference(s2)
print ("s1 = s1^s2 ", s3)

'''------------------------------------ Python - Loop Sets -----------------------'''
''' Access Set Items Using For Loop 
Example:- '''

set1 = {1,2,3,4,5,6,7,8,9,10}
for i in set1:
    print(i)

''' Loop Through Set Items with While Loop
Example:- In the below example, we are iterating through a set using an iterator and a while loop.
The "try" block retrieves and prints each item, while the "except StopIteration" block
breaks the loop when there are no more items to fetch'''
# Defining a set with multiple elements
my_set = {1, 2, 3, 4, 5}
# Converting the set to an iterator
set_iterator = iter(my_set)
# Looping through each item in the set using a while loop
while True:
    try:
        # Getting the next item from the iterator
        item = next(set_iterator)
        # Performing operations on each element
        print("Item:", item)
    except StopIteration:
        # If StopIteration is raised, break from the loop
        break
'''Iterate using Set Comprehension 
Syntax:- result_set = {expression for item in iterable if condition}
Where,
     expression − It is an expression to evaluate for each item in the iterable.
     item − It is a variable representing each element in the iterable.
     iterable − It is a collection to iterate over (e.g., list, tuple, set).
     condition − It is optional condition to filter elements included in the resulting set.
Example:-
In this example, we are using a set comprehension to generate a set containing squares
of even numbers from the original list "numbers"'''
# Original list
numbers = [1, 2, 3, 4, 5]
# Set comprehension to create a set of squares of even numbers
squares_of_evens = {x**2 for x in numbers if x % 2 == 0}
# Print the resulting set
print(squares_of_evens)

''' Iterate through a Set Using the enumerate() Function 
We can iterate through a set using the enumerate() function by converting the set into a
list and then applying enumerate() to iterate over the elements along with their index
positions. Following is the syntax −
...
for index, item in enumerate(list(my_set)):
    # Your code here
...
Example:-
In the following example, we are first converting a set into a list. Then, we iterate through
the list using a for loop with enumerate() function, retrieving each item along with its
index'''

# Converting the set into a list
my_set = {1, 2, 3, 4, 5}
set_list = list(my_set)
# Iterating through the list
for index, item in enumerate(set_list):
    print("Index:", index, "Item:", item)

'''----------------------------- Join Sets in Python -----------------------------
Joining sets in Python refers to merging two or more sets as a single set. When you join
sets, you merge the elements of multiple sets while ensuring that duplicate elements are
removed, as sets do not allow duplicate elements.
This can be achieved using various methods, such as union, update, set comprehension,
set concatenation, copying, and iterative addition.'''

''' Join Python Sets Using "|" Operator. We have covered this topic'''
''' oin Python Sets Using union() Method. We have covered this topic'''
''' Join Python Sets Using update() Method. We have covered this topic'''
''' Join Python Sets Using Unpacking Operator
In Python, the "*" symbol is used as unpacking operator. The unpacking operator internally
assigns each element in a collection to a separate variable.
We can join Python sets using the unpacking operator (*) by unpacking the elements of
multiple sets into a new set.
Example:-
In the following example, we are creating a new set "s3" by unpacking the elements of
sets "s1" and "s2" using the * operator within a set literal'''
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = {*s1, *s2}
print (s3)

''' Join Python Sets Using Set Comprehension
We can join python sets using set comprehension by iterating over multiple sets and
adding their elements to a new set.
Example
In this example, we are creating a new set "joined_set" using a set comprehension. By
iterating over a list containing "set1" and "set2", and then iterating over each element "x"
within each set "s", we merge all elements from both sets into "joined_set'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}
joined_set = {x for s in [set1, set2] for x in s}
print(joined_set)

''' Join Python Sets Using Iterative Addition
Example:-
In the example below, we first initialize an empty set. Then, we iterate over each element
in "set1" and "set2" separately, adding each element into a new set named "joined_set"
using the add() method'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Initializing an empty set to hold the merged elements
joined_set = set()
# Iterating over set1 and adding its elements to the joined set
for element in set1:
    joined_set.add(element)
# Iterating over set2 and adding its elements to the joined set
for element in set2:
    joined_set.add(element)
print(joined_set)

'''-------------------------------- Python Copy Sets ---------------------------
Copying sets in Python refers to creating a new set that contains the same elements as an
existing set. Unlike simple variable assignment, which creates a reference to the original
set, copying ensures that changes made to the copied set do not affect the original set,
and vice versa.
There are different methods for copying a set in Python, including using the copy() method,
the set() function or set comprehension.'''

''' Copy Sets Using the copy() Method
The copy() method in set class is used to create a shallow copy of a set object.
A shallow copy means that the method creates a new collection object, but does not create
copies of the objects contained within the original collection. Instead, it copies the
references to these objects.
Therefore, if the original collection contains mutable objects (like lists, dictionaries, or
other sets), modifications to these objects will be reflected in both the original and the
copied collections.
Syntax:- set.copy()
Return Value
    The copy() method returns a new set which is a shallow copy of existing set.
Example:- 
In the following example, we are creating a copy of the set "lang1" and storing it in "lang2",
then retrieving both sets and their memory addresses using id().
After adding an element to "lang1", we retrieve both sets and their memory addresses
again to show that "lang1" and "lang2" are independent copies −'''
lang1 = {"C", "C++", "Java", "Python"}
print ("lang1: ", lang1, "id(lang1): ", id(lang1))
lang2 = lang1.copy()
print ("lang2: ", lang2, "id(lang2): ", id(lang2))
lang1.add("PHP")
print ("After updating lang1")
print ("lang1: ", lang1, "id(lang1): ", id(lang1))
print ("lang2: ", lang2, "id(lang2): ", id(lang2))

'''Copy Sets using the set() Function
The Python set() function is used to create a new set object. It takes an iterable as an
argument and convert it into a set, removing any duplicate elements in the process. If no
argument is provided, it creates an empty set
Example:- 
In this example, we are creating a copy of "original_set" using the set() function and
storing it in "copied_set"'''
# Original set
original_set = {1, 2, 3, 4}
# Copying the set using the set() function
copied_set = set(original_set)
print("copied set:", copied_set)
# Demonstrating that the sets are independent
copied_set.add(5)
print("copied set:",copied_set)
print("original set:",original_set)

''' Copy Sets Using Set Comprehension
The syntax is similar to list comprehension but with curly braces {} instead of square brackets
Syntax:- {expression for item in iterable if condition}
Example:- '''
# Original set
original_set = {1, 2, 3, 4, 5}
# Copying the set using set comprehension
copied_set = {x for x in original_set}
print("Copied set:", copied_set)

'''------------------------ Set Operators in Python ----------------------
The set operators in Python are special symbols and functions that allow you to perform
various operations on sets, such as union, intersection, difference, and symmetric
difference.'''

''' Python Set Union Operator (|)
The union of two sets is a set containing all distinct elements that are in A or in B or both.
For example,
{1,2}∪{2,3}={1,2,3}
Example:- '''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 45, 73}
union_set1 = set1.union(set2)
union_set2 = set3 | set4
print ('The union of set1 and set2 is', union_set1)
print ('The union of set3 and set4 is', union_set2)

''' Python Set Intersection Operator (&)
The intersection of two sets AA and BB, denoted by A∩B, consists of all elements that are
common to both in A and B. For example,
{1,2}∩{2,3}={2}
Example:-'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}
intersection_set1 = set1.intersection(set2)
intersection_set2 = set3 & set4
print ('The intersection of set1 and set2 is', intersection_set1)
print ('The intersection of set3 and set4 is', intersection_set2)

''' Python Set Difference Operator (-)
The difference (subtraction) between two sets consists of elements present in the first set
but not in the second set. It is defined as follows. The set A−B consists of elements that
are in A but not in B. For example,
If A={1,2,3} and B={3,5}, then A−B={1,2}
Example:- '''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}
difference_set1 = set1.difference(set2)
difference_set2 = set3 - set4
print ('The difference between set1 and set2 is', difference_set1)
print ('The difference between set3 and set4 is', difference_set2)

''' Python Set Symmetric Difference Operator
The symmetric difference of two sets consists of elements that are present in either set
but not in both sets. The symmetric difference of A and B is denoted by "A Δ B" and is
defined by −
A Δ B = (A − B) ⋃ (B − A)
f A = {1, 2, 3, 4, 5, 6, 7, 8} and B = {1, 3, 5, 6, 7, 8, 9}, then A Δ B = {2, 4, 9}.
Example:- '''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}
symmetric_difference_set1 = set1.symmetric_difference(set2)
symmetric_difference_set2 = set3 ^ set4
print ('The symmetric difference of set1 and set2 is',
symmetric_difference_set1)
print ('The symmetric difference of set3 and set4 is',
symmetric_difference_set2)

''' Python Subset Testing Operation
You can check whether one set is a subset of another using the issubset() function or the
<= operator. A set A is considered a subset of another set B if all elements of A are also
present in B −
Example
The following example uses the "<=" operator and the issubset() function, and returns
subset testing of two sets - '''
set1 = {1, 2}
set2 = {1, 2, 3, 4}
set3 = {64, 47, 245, 48}
set4 = {64, 47, 3}
is_subset1 = set1.issubset(set2)
is_subset2 = set3 <= set4
print ('set1 is a subset of set2:', is_subset1)
print ('set3 is a subset of set4:', is_subset2)

'''----------------------------------- Python - Set Methods --------------------------
The set class includes several built-in methods that allow you to add, update, and delete
elements efficiently, as well as to perform various set operations such as union,
intersection, difference, and symmetric difference on elements.
You can view all available methods for sets, using the Python dir() function to list all
properties and functions related to the set class. Additionally, the help() function provides
detailed documentation for each method.'''

''' Python Set Methods
Below are the built-in methods for sets in Python, categorized based on their functionality.'''

''' Adding and Removing Elements
The following are the methods specifically designed for adding and removing item/items
into a set

#------- Set Methods ----------------------------------------
Sr.No.           Function & Description 
---------------------------------------------------------
1                          set.add()
                      Add an element to a set.
                      
2                          set.clear()
                      Remove all elements from a set.
                      
3                          set.copy()
                      Return a shallow copy of a set.
                      
4                          set.discard()
                      Remove an element from a set if it
                      is a member.
                      
5                          set.pop()
                      Remove and return an arbitrary set
                      element.
                      
6                          set.remove()
                      Remove an element from a set; it
                      must be a member.
----------------------------------------------------------
'''

''' These methods perform set operations such as union, intersection, difference, and
symmetric difference −
Here's the text formatted in **TJ1 format**:

```
#------- Set Methods ----------------------------------------
Sr.No.           Function & Description 
---------------------------------------------------------
1                          set.update()
                      Update a set with the union of itself and
                      others.
                      
2                          set.difference_update()
                      Remove all elements of another set from this
                      set.
                      
3                          set.intersection()
                      Returns the intersection of two sets as a new
                      set.
                      
4                          set.intersection_update()
                      Updates a set with the intersection of itself and
                      another.
                      
5                          set.isdisjoint()
                      Returns True if two sets have a null
                      intersection.
                      
6                          set.issubset()
                      Returns True if another set contains this set.
                      
7                          set.issuperset()
                      Returns True if this set contains another set.
                      
8                          set.symmetric_difference()
                      Returns the symmetric difference of two sets
                      as a new set.
                      
9                          set.symmetric_difference_update()
                      Update a set with the symmetric difference of
                      itself and another.
                      
10                         set.union()
                      Returns the union of sets as a new set.
                      
11                         set.difference()
                      Returns the difference of two or more sets as a
                      new set.
----------------------------------------------------------
'''