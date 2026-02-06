'''
List is one of the built-in data types in Python. A Python list is a sequence of comma
separated items, enclosed in square brackets [ ]. The items in a Python list need not be
of the same data type

Following are some examples of Python lists
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]

A Python list is mutable. Any item from the list can be accessed using its
index, and can be modified.
'''

''' Accessing Values in Lists'''
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

''' Updating Lists
You can update single or multiple elements of lists
Example:- '''
list = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])

'''Delete List Elements
To remove a list element, you can use either the del statement if you know exactly which
element(s) you are deleting or the remove() method if you do not know. 
For example:-
'''
list1 = ['physics', 'chemistry', 1997, 2000];
print (list1)
del list1[2];
print ("After deleting value at index 2 : ")
print (list1)

'''Python List Operations
In Python, List is a sequence. Hence, we can concatenate two lists with "+" operator and
concatenate multiple copies of a list with "*" operator. The membership operators "in" and
"not in" work with list object
Example:- 
Python Expression           Results                         Description
--------------------------------------------------------------------------
[1, 2, 3] + [4, 5, 6]       [1, 2, 3, 4, 5, 6]              Concatenation
['Hi!'] * 4                 ['Hi!', 'Hi!', 'Hi!', 'Hi!']    Repetition
3 in [1, 2, 3]              TRUE                            Membership
'''

''' Indexing, Slicing, and Matrixes
Because lists are sequences, indexing and slicing work the same way for lists as they do
for strings. 
Example for L = ['spam', 'Spam', 'SPAM!']

Python Expression           Results                         Description
--------------------------------------------------------------------------
L[2]                        SPAM!                           Offsets start at zero
L[-2]                       Spam                            Negative: count from the right
L[1:]                       ['Spam', 'SPAM!']               Slicing fetches sections
'''

''' Python List Methods
Python includes following list methods

#------- Python List Methods ---------------------------------
Sr.No.           Methods & Description 
---------------------------------------------------------
1                          list.append(obj)  
                     Appends object obj to list. 
2                          list.clear() 
                    Clears the contents of list. 
3                          list.copy()  
                    Returns a copy of the list object. 
4                          list.count(obj)  
                    Returns count of how many times obj occurs in list. 
5                          list.extend(seq) 
                    Appends the contents of seq to list. 
6                          list.index(obj)  
                    Returns the lowest index in list that obj appears. 
7                          list.insert(index, obj)  
                    Inserts object obj into list at offset index. 
8                          list.pop(obj=list[-1])  
                    Removes and returns last object or obj from list.
9                          list.remove(obj) 
                    Removes object obj from list. 
10                         list.reverse()  
                    Reverses objects of list in place. 
11                         list.sort([func])  
                    Sorts objects of list, use compare func if given.
------------------------------------------------------------------------------
'''

''' Built-in Functions with Lists
Following are the built-in functions we can use with lists

#------- Built-in Functions with Lists ---------------------------------
Sr.No.           Function & Description 
---------------------------------------------------------
1                          cmp(list1, list2)  
                     Compares elements of both lists. 
2                          len(list) 
                    Gives the total length of the list. 
3                          max(list)  
                    Returns item from the list with max value. 
4                          min(list)  
                    Returns item from the list with min value. 
5                          list(seq)  
                    Converts a tuple into list.
------------------------------------------------------------------------------
'''

'''Accessing List Items
Example:-'''
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["Rohan", "Physics", 21, 69.75]
print ("Item at 0th index in list1: ", list1[0])
print ("Item at index 2 in list2: ", list2[2])

print ("Item at 0th index in list1: ", list1[-1])
print ("Item at index 2 in list2: ", list2[-3])
# using Slice Operator [:]
print ("Items from index 1 to last in list1: ", list1[1:])
print ("Items from index 0 to 1 in list2: ", list2[:2])
print ("Items from index 0 to index last in list3", list3[:])

print ("Items from index 1 to 2 in list1: ", list1[1:3])
print ("Items from index 0 to 1 in list2: ", list2[0:2])

'''Change List Items
List is a mutable data type in Python. It means, the contents of list can be modified in
place, after the object is stored in the memory. You can assign a new value at a given
index position in the list
Example:-
In the following code, we change the value at index 2 of the given list.'''
list3 = [1, 2, 3, 4, 5]
print ("Original list ", list3)
list3[2] = 10
print ("List after changing value at index 2: ", list3)

'''Change Consecutive List Items
You can replace more consecutive items in a list with another sublist.
Example
In the following code, items at index 1 and 2 are replaced by items in another sublist
'''
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['Y', 'Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)

'''Change a Range of List Items'''
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['X','Y', 'Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)

''' Example
If the sublist with which a slice of original list is to be replaced, has lesser items, the items
with match will be replaced and rest of the items in original list will be removed.
In the following code, we try to replace "b" and "c" with "Z" (one less item than items to
be replaced). It results in Z replacing b and c removed'''
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)

'''------------------------ Add List Items --------------------
Adding list items in Python implies inserting new elements into an existing list. Lists are
mutable, meaning they can be modified after creation, allowing for the addition, removal,
or modification of their elements
We can add list items in Python using various methods such as append(), extend() and
insert(). Let us explore through all these methods in this tutorial'''

'''Adding List Items Using append() Method
The append() method in Python is used to add a single element to the end of a list.
Example:-:
'''
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list1.append('e')
print ("List after appending: ", list1)

'''Adding List Items Using insert() Method
The insert() method in Python is used to add an element at a specified index (position)
within a list, shifting existing elements to accommodate the new one.
Example:- 
In this example, we have an original list containing various items. We use the insert()
method to add new elements to the list at specific positions'''
list1 = ["Rohan", "Physics", 21, 69.75]
list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)
list1.insert(-1, 'Pass')
print ("List after appending: ", list1)
'''We can see that "Pass" is not inserted at the updated index "-1", but the previous index
"-1". This behavior is because when appending or inserting items into a list, Python does
not dynamically update negative index positions.'''

''' Adding List Items Using extend() Method
The extend() method in Python is used to add multiple elements from an iterable (such as
another list) to the end of a list.
Example:- 
In the below example, we are using the extend() method to add the elements from
"another_list" to the end of "list1'''
# Original list
list1 = [1, 2, 3]
# Another list to extend with
another_list = [4, 5, 6]
list1.extend(another_list)
print("Extended list:", list1)

'''-------------------- Removing List Items ------------------
We can remove list items in Python using various methods such as remove(), pop() and
clear(). Additionally, we can use the del statement to remove items at a specific index. '''

'''Remove List Item Using remove() Method
The remove() method in Python is used to remove the first occurrence of a specified item
from a list
Example:-'''
list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)
list1.remove("Physics")
print ("List after removing: ", list1)

''' Remove List Item Using pop() Method
The pop() method in Python is used to remove and return the last element from a list if
no index is specified. It can also remove and return the element at a specified index,
altering the original list.
Example:- '''
list2 = [25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop(2)
print ("List after popping: ", list2)

''' Remove List Item Using clear() Method
The clear() method in Python is used to remove all elements from a list, leaving it empty.'''
my_list = [1, 2, 3, 4, 5]
# Clearing the list
my_list.clear()
print("Cleared list:", my_list)

''' Remove List Item Using del Keyword
The del keyword in Python is used to delete element either at a specific index or a slice of
indices from memory.
We can remove list items using the del keyword by specifying the index or slice of the
items we want to delete, like del my_list[index] to delete a single item or del
my_list[start:stop] to delete a range of items.
Example:- '''
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
del list1[2]
print ("List after deleting: ", list1)


'''Example
In here, we are deleting a series of consecutive items from a list with the slicing operator'''
list2 = [25.50, True, -55, 1+2j]
print ("List before deleting: ", list2)
del list2[0:2]
print ("List after deleting: ", list2)

'''--------------------------- Loop Through List Items ----------------------
Looping through list items in Python refers to iterating over each element within a list. We
do so to perform the desired operations on each item. These operations include list
modification, conditional operations, string manipulation, data analysis, etc.'''

''' Loop Through List Items with For Loop
Example:-
In the following example, we are using a for loop to iterate through each element in the
list "lst" and retrieving each element followed by a space on the same line'''

lst = [25, 12, 10, -21, 10, 100]
for num in lst:
    print (num, end = ' ')

''' Loop Through List Items with While Loop
A while loop in Python is used to repeatedly execute a block of code as long as a specified
condition evaluates to "True"
We can loop through list items using the while loop by initializing an index variable, then
iterating through the list using the index variable and incrementing it until reaching the
end of the list
Example:-'''
my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

''' Loop Through List Items with Index
An index is a numeric value representing the position of an element within a sequence,
such as a list, starting from 0 for the first element.
We can loop through list items using index by iterating over a range of indices
corresponding to the length of the list and accessing each element using the index within
the loop
Example:- '''
lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
for i in indices:
    print ("lst[{}]: ".format(i), lst[i])

''' Iterate using List Comprehension
A list comprehension in Python is a concise way to create lists by applying an expression
to each element of an iterable. These expressions can be arithmetic operations, function
calls, conditional expressions etc.
We can iterate using list comprehension by specifying the expression and the iterable (like
a list, tuple, dictionary, string, or range). Following is the syntax
[expression for item in iterable]

Example:-
In this example, we use list comprehension to iterate through each number in a list of
numbers, square each one, and store the squared result in the new list "squared_numbers"'''
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print (squared_numbers)

''' Iterate using the enumerate() Function
The enumerate() function in Python is used to iterate over an iterable object while also
providing the index of each element. Following is the synta
for index, item in enumerate(iterable):
This provides both the index and item of each element in the iterable during iteration

Example
In the following example, we are using the enumerate() function to iterate through a list
"fruits" and retrieve each fruit along with its corresponding index'''
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

'''--------------------- List Comprehension in Python ---------------------
A list comprehension is a concise way to create lists. It is similar to set builder notation in
mathematics. It is used to define a list based on an existing iterable object, such as a list,
tuple, or string, and apply an expression to each element in the iterable
Syntax of Python List Comprehension
The basic syntax of list comprehension is as below

new_list = [expression for item in iterable if condition]
Where,
     expression is the operation or transformation to apply to each item in the iterable.
     item is the variable representing each element in the iterable.
     iterable is the sequence of elements to iterate over.
     condition (optional) is an expression that filters elements based on a specified condition
'''
''' Example of Python List Comprehension
Suppose we want to convert all the letters in the string "hello world" to their upper-case
form. Using list comprehension, we iterate through each character, check if it is a letter,
and if so, convert it to uppercase, resulting in a list of uppercase letters'''
string = "hello world"
uppercase_letters = [char.upper() for char in string if char.isalpha()]
print(uppercase_letters)

''' List Comprehensions and Lambda
In Python, lambda is a keyword used to create anonymous functions. An anonymous
function is a function defined without a name. These functions are created using the
lambda keyword followed by a comma-separated list of arguments, followed by a colon :,
and then the expression to be evaluated
Example:- 
In the following example, we are using list comprehension with a lambda function to double
each element in a given list "original_list". We iterate over each element in the
"original_list" and apply the lambda function to double it'''
original_list = [1, 2, 3, 4, 5]
doubled_list = [(lambda x: x * 2)(x) for x in original_list]
print(doubled_list)

''' Nested Loops in Python List Comprehension
A nested loop in Python is a loop inside another loop, where the inner loop is executed
multiple times for each iteration of the outer loop.
Example:- 
In this example, all combinations of items from two lists in the form of a tuple are added
in a third list objec'''
list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2]
print (CombLst)

''' Conditionals in Python List Comprehension
Conditionals in Python refer to the use of statements like "if", "elif", and "else" to control
the flow of a code based on certain conditions. They allow you to execute different blocks
of code depending on whether a condition evaluates to "True" or "False"
Example:- 
The following example uses conditionals within a list comprehension to generate a list of
even numbers from 1 to 20'''
list1=[x for x in range(1,21) if x%2==0]
print (list1)

'''List Comprehensions vs For Loop
List comprehensions are like shortcuts for creating lists in Python. They let you generate
a new list by applying an operation to each item in an existing list.
For loop, on the other hand, is a control flow statement used to iterate over elements of
an iterable one by one, executing a block of code for each element.

Advantages of List Comprehension
Following are the advantages of using list comprehension −
     Conciseness − List comprehensions are more concise and readable compared to traditional for loops, allowing you to create lists with less code.
     Efficiency − List comprehensions are generally faster and more efficient than for loops because they are optimized internally by Python's interpreter.
     Clarity − List comprehensions result in clearer and more expressive code, making it easier to understand the purpose and logic of the operation being performed.
     Reduced Chance of Errors − Since list comprehensions are more compact, there is less chance of errors compared to traditional for loops, reducing the likelihood of
    bugs in your code.

Example Using For Loop:- 
Suppose we want to separate each letter in a string and put all non-vowel letters in a list
object. We can do it by a for loop as shown below'''
chars=[]
for ch in 'TutorialsPoint':
    if ch not in 'aeiou':
        chars.append(ch)
print (chars)
# Example Using List Comprehension
chars = [ char for char in 'TutorialsPoint' if char not in 'aeiou']
print (chars)

''' Example:- 
The following example uses list comprehension to build a list of squares of numbers
between 1 to 10'''
squares = [x*x for x in range(1,11)]
print (squares)


'''---------------------- Sorting Lists in Python -------------------------
Sorting a list in Python is a way to arrange the elements of the list in either ascending or
descending order based on a defined criterion, such as numerical or lexicographical order.
This can be achieved using the built-in sorted() function or by calling the sort() method
on the list itself, both of which modify the original list or return a new sorted list depending
on the method used.'''

''' Sorting Lists Using sort() Method
The python sort() method is used to sort the elements of a list in place. This means that
it modifies the original list and does not return a new list.
Syntax:- 
list_name.sort(key=None, reverse=False)
Where,
 list_name is the name of the list to be sorted.
 key (optional) is a function that defines the sorting criterion. If provided, it is applied to each element of the list for sorting. Default is None.
 reverse (optional) is a boolean value. If True, the list will be sorted in descending order. If False (default), the list will be sorted in ascending order.'''

'''Example of Sorting List in Lexicographical Order
In the following example, we are using the sort() function to sort the items of the list
alphanumerically'''
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list2 = [10,16, 9, 24, 5]
print ("list before sort:", list1)
list1.sort()
print ("list after sort : ", list1)

print ("list before sort", list2)
list2.sort()
print ("list after sort : ", list2)

''' Sorting Lists Using sorted() Method
The sorted() function in Python is a built-in function used to sort the elements of an iterable
(such as a list, tuple, or string) and returns a new sorted list, leaving the original iterable
unchanged.
Syntax
The syntax for using the sorted() method is as follows −
sorted(iterable, key=None, reverse=False)
Where,
     iterable is the iterable (e.g., list, tuple, string) whose elements are to be sorted.
     key (optional) is a function that defines the sorting criterion. If provided, it is applied to each element of the iterable for sorting. Default is None.
     reverse (optional) is a boolean value. If True, the iterable will be sorted in descending order. If False (default), the iterable will be sorted in ascending order.'''

'''Example:- '''
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)

''' Sorting List Items with Callback Function
In Python, a callback function refers to a function that is passed as an argument to another
function and is invoked or called within that function
We can sort list items with a callback function by using the sorted() function or sort()
function in Python. Both of these functions allows us to specify a custom sorting criterion
using the "key" parameter, which accepts a callback function. This callback function defines
how the elements should be compared and sorted

Example Using str.lower() as key Parameter
The str.lower() method in Python is used to convert all the characters in a string to
lowercase. It returns a new string with all alphabetic characters converted to lowercase
while leaving non-alphabetic characters unchanged.
In this example, we are passing the str.lower() method as an argument to the "key"
parameter within the sort() function'''
list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
print ("list before sort", list1)
list1.sort(key=str.lower)
print ("list after sort : ", list1)

''' Example using user-defined Function as key Parameter
We can also use a user-defined function as the key parameter in sort() method.
In this example, the myfunction() uses % operator to return the remainder, based on
which the sorting is performed'''
def myfunction(x):
    return x%10
list1 = [17, 23, 46, 51, 90]
print ("list before sort", list1)
list1.sort(key=myfunction)
print ("list after sort : ", list1)


'''--------------------------- Copying a List in Python ---------------------
Copying a list in Python refers to creating a new list that contains the same elements as
the original list. There are different methods for copying a list, including, using slice
notation, the list() function, and using the copy() method. '''

''' Shallow Copy on a Python List
A shallow copy in Python creates a new object, but instead of copying the elements
recursively, it copies only the references to the original elements. This means that the new
object is a separate entity from the original one, but if the elements themselves are
mutable, changes made to those elements in the new object will affect the original object
as well
Example:- '''
import copy
# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Creating a shallow copy
shallow_copied_list = copy.copy(original_list)
# Modifying an element in the shallow copied list
shallow_copied_list[0][0] = 100
# Printing both lists
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

''' Deep Copy on a Python List
A deep copy in Python creates a completely new object and recursively copies all the
objects referenced by the original object.
Example:- '''
import copy
# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Creating a deep copy
deep_copied_list = copy.deepcopy(original_list)
# Modifying an element in the deep copied list
deep_copied_list[0][0] = 100
# Printing both lists
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)
'''As you can see, when we modify the first element of the first sublist in the deep copied
list, it does not affect the original list.
This is because a deep copy creates a new object and recursively copies all the nested
objects, ensuring that the copied object is fully independent from the original one'''

''' Copying List Using Slice Notation
Slice notation in Python allows you to create a subsequence of elements from a sequence
(like a list, tuple, or string) by specifying a start index, an end index, and an optional step
size.
Syntax:- [start:end:step]
Where, start is the index where the slice starts, end is the index where the slice ends
(exclusive), and step is the step size between elements. (Any modifications made to the copied list will not affect the original list,
and vice versa, because they are separate objects in memory.)
Example:- '''
# Original list
original_list = [1, 2, 3, 4, 5]
# Copying the list using slice notation
copied_list = original_list[1:4]
# Modifying the copied list
copied_list[0] = 100
# Printing both lists
print("Original List:", original_list)
print("Copied List:", copied_list)

''' Copying List Using the list() Function '''
'''ExampleL- 
# Original list
original_list = [1, 2, 3, 4, 5]
# Copying the list using the list() constructor
copied_list = list(original_list)    
# Printing both lists
print("Original List:", original_list)
print("Copied List:", copied_list)
'''

'''------------------ Join Lists in Python ---------------------
Joining lists in Python refers to combining the elements of multiple lists into a single list.
This can be achieved using various methods, such as concatenation, list comprehension,
or using built-in functions like extend() or + operator'''
''' Join Lists Using Concatenation Operator
Example:-'''
# Two lists to be joined
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
# Joining the lists
joined_list = L1 + L2
# Printing the joined list
print("Joined List:", joined_list)

''' Join Lists Using List Comprehension
List comprehension is a concise way to create lists in Python. It is used to generate new
lists by applying an expression to each item in an existing iterable, such as a list, tuple, or
range. The syntax for list comprehension is −
new_list = [expression for item in iterable]

Example:- '''
# Two lists to be joined
L1 = [36, 24, 3]
L2 = [84, 5, 81]
# Joining the lists using list comprehension
joined_list = [item for sublist in [L1, L2] for item in sublist]
# Printing the joined list
print("Joined List:", joined_list)

''' Join Lists Using append() Function
The append() function in Python is used to add a single element to the end of a list. This
function modifies the original list by adding the element to the end of the list.'''
# List to which elements will be appended
list1 = ['Fruit', 'Number', 'Animal']
# List from which elements will be appended
list2 = ['Apple', 5, 'Dog']
# Joining the lists using the append() function
for element in list2:
    list1.append(element)
# Printing the joined list
print("Joined List:", list1)

''' Join Lists Using extend() Function
The Python extend() function is used to append elements from an iterable (such as another
list) to the end of the list. This function modifies the original list in place, adding the
elements of the iterable to the end of the list.
Example
In the following example, we are extending "list1" by appending the elements of "list2"
using the extend() function −'''
# List to be extended
list1 = [10, 15, 20]
# List to be added
list2 = [25, 30, 35]
# Joining the lists using the extend() function
list1.extend(list2)
# Printing the extended list
print("Extended List:", list1)

'''------------------------------ List Methods ---------------------------------'''
'''Printing All the List Methods
To view all the available methods for lists, you can use the Python dir() function, which
returns all the properties and functions related to an object. Additionally, you can use the
Python help() function to get more detailed information about each method. For example:
'''
print(dir([]))
print(help([].append))

''' Methods to Add Elements to a List
The following are the methods specifically designed for adding new item/items into a list
−
#------- List Methods ---------------------------------
Sr.No.           Methods with Description 
---------------------------------------------------------
1                          list.append(obj)  
                     Appends object obj to list. 
2                          list.extend(seq) 
                    Appends the contents of seq to list 
3                          list.insert(index, obj)  
                    Insert object obj into list at offset index 
-------------------------------------------------------------------
'''

''' Methods to Remove Elements from a List
The following are the methods specifically designed for removing items from a list −
#------- List Methods ---------------------------------
Sr.No.           Methods with Description 
---------------------------------------------------------
1                          list.clear()  
                     Clears all the contents of the list. 
2                          list.pop(obj=list[-1]) 
                    Removes and returns the last object or the object at the specified index from the list. 
3                          list.remove(obj)  
                    Removes the first occurrence of object obj from the list.
------------------------------------------------------------------------------
'''

''' Methods to Access Elements in a List
These are the methods used for finding or counting items in a list −
#------- List Methods ---------------------------------
Sr.No.           Methods with Description 
---------------------------------------------------------
1                          list.index(obj)  
                     Returns the lowest index in list that obj appears 
2                          list.count(obj) 
                    Returns count of how many times obj occurs in the list.
------------------------------------------------------------------------------
'''

'''Copying and Ordering Methods
These are the methods used for creating copies and arranging items in a list −
#------- List Methods ---------------------------------
Sr.No.           Methods with Description 
---------------------------------------------------------
1                          list.copy()  
                     Returns a copy of the list object. 
2                          list.sort([func]) 
                    Sorts the objects in the list in place, using a comparison function if provided. 
3                          list.reverse()  
                    Reverses the order of objects in the list in place.
------------------------------------------------------------------------------
'''

''' Python List Exercise 1
Python program to find unique numbers in a given list.'''
L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []

for i in L1:
    if i not in L2:
        L2.append(i)
print(L2)

''' Python List Exercise 2
Python program to find sum of all numbers in a list.'''
L1 = [1, 9, 1, 6, 3, 4]
ttl = 0
for x in L1:
    ttl+=x
print ("Sum of all numbers Using loop:", ttl)
ttl = sum(L1)
print ("Sum of all numbers sum() function:", ttl)

'''Python List Exercise 3
Python program to create a list of 5 random integers'''
import random
L1 = []
for i in range(5):
    x = random.randint(0, 100)
    L1.append(x)
print (L1)