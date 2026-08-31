#--------------------------- Python - Tuples ---------------------
''' Tuple is one of the built-in data types in Python. It is a sequence of comma separated
items, enclosed in parentheses (). The items in a Python tuple need not be of same data
type.
tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1+2j)

Tuple is one of the fundamental data structures in Python, and it is an immutable
sequence. Unlike lists, tuples cannot be modified after creation, making them ideal for
representing fixed collections of data'''

''' The empty tuple is written as two parentheses containing nothing −
tup1 = ();'''
''' To write a tuple containing a single value you have to include a comma, even though there
is only one value
Example:- tup1 = (50,);'''

''' Following are the points to be noted −
         In Python, tuple is a sequence data type. It is an ordered collection of items. Each item in the tuple has a unique position index, starting from 0.
         In C/C++/Java array, the array elements must be of same type. On the other hand, Python tuple may have objects of different data types.
         Python tuple and list both are sequences. One major difference between the two is, Python list is mutable, whereas tuple is immutable. Although any item from the
        tuple can be accessed using its index, and cannot be modified, removed or added.'''

'''Accessing Values in Tuples'''
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0]);
print ("tup2[1:5]: ", tup2[1:5]);

'''Updating Tuples
Tuples are immutable which means you cannot update or change the values of tuple
elements. You are able to take portions of existing tuples to create new tuples as the
following example demonstrates'''
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');
# Following action is not valid for tuples
# tup1[0] = 100;
# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3);

'''Delete Tuple Elements
Removing individual tuple elements is not possible. There is, of course, nothing wrong with
putting together another tuple with the undesired elements discarded.
Example:-'''
tup = ('physics', 'chemistry', 1997, 2000);
print (tup);
del tup;
print ("After deleting tup : ");
#print (tup);   # It will raise the exception that tup is not defined

'''Python Tuple Operations
In Python, Tuple is a sequence. Hence, we can concatenate two tuples with + operator
and concatenate multiple copies of a tuple with "*" operator. The membership operators
"in" and "not in" work with tuple object.

Python Expression           Results                         Description
--------------------------------------------------------------------------
(1, 2, 3) + (4, 5, 6)       (1, 2, 3, 4, 5, 6)              Concatenation
('Hi!',) * 4                ('Hi!', 'Hi!', 'Hi!', 'Hi!')     Repetition
3 in (1, 2, 3)              TRUE                            Membership
'''

''' Indexing, Slicing, and Matrixes
Because tuples are sequences, indexing and slicing work the same way for tuples as they
do for strings. Assuming following input −
L = ('spam', 'Spam', 'SPAM!')

Python Expression           Results                         Description
--------------------------------------------------------------------------
L[2]                        'SPAM!'                         Offsets start at zero
L[-2]                       'Spam'                          Negative: count from the right
L[1:]                       ['Spam', 'SPAM!']               Slicing fetches sections
'''

'''No Enclosing Delimiters
Any set of multiple objects, comma-separated, written without identifying symbols, i.e.,
brackets for lists, parentheses for tuples, etc., default to tuples, as indicated in these short
examples
print ('abc', -4.24e93, 18+6.6j, 'xyz');
x, y = 1, 2;
print ("Value of x , y : ", x,y);'''

'''Built-in Functions with Tuples
Following are the built-in functions we can use with tuples −

#------- Tuple Functions ---------------------------------
Sr.No.           Function & Description 
---------------------------------------------------------
1                          cmp(tuple1, tuple2)  
                     Compares elements of both tuples. 
2                          len(tuple) 
                    Gives the total length of the tuple. 
3                          max(tuple)  
                    Returns item from the tuple with max value. 
4                          min(tuple) 
                    Returns item from the tuple with min value. 
5                          tuple(seq)  
                    Converts a list into tuple. 
------------------------------------------------------------------------------
'''


'''------------------------------ Access Tuple Items -------------------------
The most common way to access values within a Python tuple is using indexing. We just
need to specify the index of the elements we want to retrieve to the square bracket []
notation.'''
''' Accessing Tuple Items with Indexing
Example
Following is the basic example to access tuple items with slicing index −
'''
tuple1 = ("Rohan", "Physics", 21, 69.75)
tuple2 = (1, 2, 3, 4, 5)
print ("Item at 0th index in tuple1: ", tuple1[0])
print ("Item at index 2 in tuple2: ", tuple2[2])

print ("Item at 0th index in tup1: ", tuple1[-1])
print ("Item at index 2 in tup2: ", tuple2[-3])
print ("Items from index 1 to last in tup1: ", tuple1[1:])
print ("Items from index 2 to last in tup2", tuple2[2:-1])

print ("Items from index 1 to last in tuple1: ", tuple1[1:])
print ("Items from index 0 to 1 in tuple2: ", tuple2[:2])
print ("Items from index 0 to index last in tuple3", tuple2[:])

print ("Items from index 1 to 2 in tuple1: ", tuple1[1:3])
print ("Items from index 0 to 1 in tuple2: ", tuple2[0:2])


'''------------------------------ Updating Tuples in Python -----------------------'''
''' Updating Tuples Using Concatenation Operator
Example
In the following example, we create a new tuple by concatenating "T1" with "T2" using the
"+" operator − '''
# Original tuple
T1 = (10, 20, 30, 40)
# Tuple to be concatenated
T2 = ('one', 'two', 'three', 'four')
# Updating the tuple using the concatenation operator
T1 = T1 + T2
print(T1)

''' Updating Tuples Using Slicing 
The syntax for slicing is as follows −
sequence[start:stop:step]
Where,
     start is the index at which the slice begins (inclusive).
     stop is the index at which the slice ends (exclusive).
     step is the interval between elements in the slice (optional).

Example
In this example, we are updating a tuple by slicing it into two parts and inserting new
elements between the slices '''
# Original tuple
T1 = (37, 14, 95, 40)
# Elements to be added
new_elements = ('green', 'blue', 'red', 'pink')
# Extracting slices of the original tuple
# Elements before index 2
part1 = T1[:2]
# Elements from index 2 onward
part2 = T1[2:]
# Create a new tuple
updated_tuple = part1 + new_elements + part2
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)

''' Updating Tuples using List Comprehension 
List comprehension in Python is a concise way to create lists. It allows you to generate
new lists by applying an expression to each item in an existing iterable, such as a list,
tuple, or string, optionally including a condition to filter elements.
Example:- '''
# Original tuple
T1 = (10, 20, 30, 40)
# Converting the tuple to a list
list_T1 = list(T1)
# Using list comprehension
updated_list = [item + 100 for item in list_T1]
# Converting the updated list back to a tuple
updated_tuple = tuple(updated_list)
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)

''' Updating Tuples using append() function
Example:- 
In the following example, we first convert the original tuple "T1" to a list "list_T1". We
then use a loop to iterate over the new elements and append each one to the list using
the append() function. Finally, we convert the updated list back to a tuple to get the
updated tuple − '''
# Original tuple
T1 = (10, 20, 30, 40)
# Convert tuple to list
list_T1 = list(T1)
# Elements to be added
new_elements = [50, 60, 70]
# Updating the list using append()
for element in new_elements:
    list_T1.append(element)
# Converting list back to tuple
updated_tuple = tuple(list_T1)
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)

'''---------------- Unpack Tuple Items -------------------------
Example
To store tuple items in individual variables, use multiple variables on the left of assignment
operator, as shown in the following example
If the number of variables is more or less than the length of tuple, Python raises a
ValueError.'''
# Original tuple
T1 = (10, 20, 30, 40)
# Unpacking the tuple into individual variables
a, b, c, d = T1
# Printing the unpacked variables
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

''' Unpack Tuple Items Using Asterisk (*)
In such a case, the "*" symbol is used for unpacking. Prefix "*" to "y", as shown below −
Example:- '''
tup1 = (10,20,30)
x, *y = tup1
print ("x: ", "y: ", y)

'''Example2:-'''
tup1 = (10,20,30, 40, 50, 60)
x, *y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)
'''Example3:-'''
*x, y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)

'''------------------------- Loop Through Tuple Items ----------------------'''
''' using for loop '''
tup = (25, 12, 10, -21, 10, 100)
for num in tup:
    print (num, end = ' ')

''' using while loop '''
tup1 = (10,20,30, 40, 50, 60)
i = 0
while i < len(tup1):
    print(tup1[i])
    i += 1
''' Loop Through Tuple Items with Index
Example:-
This example initializes a tuple "tup" with integers and creates a range of indices
corresponding to the length of the tuple. Then, it iterates over each index in the range and
prints the value at that index in the tuple "tup'''
tup = (25, 12, 10, -21, 10, 100)
indices = range(len(tup))
for i in indices:
    print ("tup[{}]: ".format(i), tup[i])

'''--------------------------------- Joining Tuples in Python -------------------
Joining tuples does not modify the original tuples but creates a new tuple containing the
combined elements.'''

''' Joining Tuples Using Concatenation ("+") Operator
Example
In the following example, we are concatenating the elements of two tuples "T1" and "T2",
creating a new tuple "joined_tuple" containing all the elements from both tuples'''
# Two tuples to be joined
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
# Joining the tuples
joined_tuple = T1 + T2
# Printing the joined tuple
print("Joined Tuple:", joined_tuple)

''' Joining Tuples Using List Comprehension
List comprehension is a concise way to create lists in Python. It is used to generate new
lists by applying an expression to each item in an existing iterable, such as a list, tuple, or
range. 
The syntax for list comprehension is −
new_list = [expression for item in iterable]
Example:-
In this example, we are joining two tuples, T1 and T2, into a single tuple using list
comprehension. The resulting tuple, joined_tuple, contains all elements from both T1 and
T2'''
# Two tuples to be joined
T1 = (36, 24, 3)
T2 = (84, 5, 81)
# Joining the tuples using list comprehension
joined_tuple = [item for subtuple in [T1, T2] for item in subtuple]
# Printing the joined tuple
print("Joined Tuple:", joined_tuple)

''' Using extend() Function 
The Python extend() function is used to append elements from an iterable (such as another
list) to the end of the list. This function modifies the original list in place, adding the
elements of the iterable to the end of the list.
Example:- 
In the following example, we are extending the first tuple "T1" by converting it into a list
"L1", then adding elements from the second tuple "T2" by first converting it into a list "L2",
and finally converting the merged list back into a tuple, effectively joining the two tuples'''
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print ("Joined Tuple:", T1)

''' Join Tuples using sum() Function
In Python, the sum() function is used to add up all the elements in an iterable, such as a
list, tuple, or set. It takes an iterable as its argument and returns the sum of all the
elements in that iterable
However, since the sum() function is specifically designed for numeric data
types, this method only works for tuples containing numeric elements
Syntax
Following is the syntax for using the sum() function to join tuples in Python −
result_tuple = sum((tuple1, tuple2), ())
Here, the first argument is a tuple containing the tuples to be joined. The second argument
is the starting value for the sum. Since we are joining tuples, we use an empty tuple () as
the starting value.'''

''' Example:- '''
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
T3 = sum((T1, T2), ())
print ("Joined Tuple:", T3)

''' Joining Tuples using for Loop 
We can join a tuple using a for loop by iterating over the elements of one tuple and
appending each element to another tuple with the "+=" operator.
Example
In the following example, we are iterating over each element in tuple T2, and for each
element, we are appending it to tuple T1, effectively joining the two tuples'''
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')
for t in T2:
    T1+=(t,)
print (T1)

'''---------------------------- Python - Tuple Methods -----------------------
Since it is immutable, this class doesn't define methods for
adding or removing items. It defines only two methods and these methods provide a
convenient way to analyze tuple data

To list all the methods available in tuple, use the dir() function as shown below −
print (dir(tuple))
print(dir((1, 2)))
print(help((1, 2).index))'''

''' Below are the built-in methods for tuples. Let's explore each method's basic functionality

#------- Tuple Methods ---------------------------------
Sr.No.           Method & Description 
---------------------------------------------------------
1                          tuple.count(obj)  
                    Returns count of how many times obj occurs in tuple. 
2                          tuple.index(obj) 
                    Returns the lowest index in tuple that obj appears.
------------------------------------------------------------------------------
'''

''' Finding the Index of a Tuple Item
The index() method of tuple class returns the index of first occurrence of the given item.
Syntax:- tuple.index(obj)
Return value
    The index() method returns an integer, representing the index of the first occurrence of
    "obj".
Example:- 
Take a look at the following example '''
tup1 = (25, 12, 10, -21, 10, 100)
print ("Tup1:", tup1)
x = tup1.index(10)
print ("First index of 10:", x)

''' Counting Tuple Items
The count() method in tuple class returns the number of times a given object occurs in
the tuple.
Syntax:- tuple.count(obj)
Return Value
Number of occurrence of the object. The count() method returns an integer.

Example:-'''
tup1 = (10, 20, 45, 10, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(10)
print ("count of 10:", c) 

''' Example
Even if the items in the tuple contain expressions, they will be evaluated to obtain the
count'''
tup1 = (10, 20/80, 0.25, 10/40, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(0.25)
print ("count of 10:", c)