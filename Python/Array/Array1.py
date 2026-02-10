'''----------------------------- Python - Arrays ------------------------------
Arrays in Python
Unlike other programming languages like C++ or Java, Python does not have built-in
support for arrays. However, Python has several data types like lists and tuples (especially
lists) that are often used as arrays but, items stored in these types of sequences need not
be of the same type.
In addition, we can create and manipulate arrays the using the array module. Before
proceeding further, let's understand arrays in general.
What are arrays?
    An array is a container which can hold a fix number of items and these items should be of
    the same type. Each item stored in an array is called an element and they can be of any
    type including integers, floats, strings, etc.
    These elements are stored at contiguous memory location. Each location of an element in
    an array has a numerical index starting from 0. These indices are used to identify and
    access the elements
Array Representation
    Arrays are represented as a collection of multiple containers where each container stores
    one element. These containers are indexed from '0' to 'n-1', where n is the size of that
    particular array.
    Arrays can be declared in various ways in different languages.'''

''' Creating Array in Python
To create an array in Python, import the array module and use its array() function. We
can create an array of three basic types namely integer, float and Unicode characters using
this function.
The array() function accepts typecode and initializer as a parameter value and returns an
object of array class.
Syntax:- below is the syntax for creating an array in Python.
    # importing
    import array as array_name
    # creating array
    obj = array_name.array(typecode[, initializer])
Where,
     typecode − The typecode character used to specify the type of elements in the
    array.
     initializer − It is an optional value from which array is initialized. It must be a list,
    a bytes-like object, or iterable elements of the appropriate type.
Example'''
import array as arr
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)
# creating an array with char type
a = arr.array('u', 'BAT')
print (type(a), a)
# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)

''' Python array type is decided by a single character Typecode argument. The type codes
and the intended data type of array is listed below

#-------------------------------- Array Typecodes ----------------------------
Typecode                Python Data Type                Byte Size
----------------------------------------------------------------------
'b'                     signed integer                   1
'B'                     unsigned integer                 1
'u'                     Unicode character                2
'h'                     signed integer                   2
'H'                     unsigned integer                 2
'i'                     signed integer                   2
'I'                     unsigned integer                 2
'l'                     signed integer                   4
'L'                     unsigned integer                 4
'q'                     signed integer                   8
'Q'                     unsigned integer                 8
'f'                     floating point                   4
'd'                     floating point                   8
'''
''' Basic Operations on Python Arrays
Following are the basic operations supported by an array −
     Traverse − Print all the array elements one by one.
     Insertion − Adds an element at the given index.
     Deletion − Deletes an element at the given index.
     Search − Searches an element using the given index or by the value.
     Update − Updates an element at the given index.
'''
'''Accessing Array Element
We can access each element of an array using the index of the elemen
Example
The below code shows how to access elements of an array'''
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])

''' Insertion Operation
In insertion operation, we insert one or more data elements into an array. Based on the
requirement, a new element can be added at the beginning, end, or any given index of
array.
Example
Here, we add a data element at the middle of the array using the python in-built insert()
method'''
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
    print(x)

'''Deletion Operation
Deletion refers to removing an existing element from the array and re-organizing all
elements.
Here, we remove a data element at the middle of the array using the python in-built
remove() method.'''
from array import *
array1 = array('i', [10,20,30,40,50])
array1.remove(40)
for x in array1:
    print(x)

'''Search Operation
You can perform a search operation on an array to find an array element based on its
value or its index.
Example
Here, we search a data element using the python in-built index() method 
When we compile and execute the above program, it will display the index of the searched
element. If the value is not present in the array, it will return an error.'''
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1.index(40))

''' Update Operation
Update operation refers to updating an existing element from the array at a given index.
Here, we simply reassign a new value to the desired index we want to update.
Example
In this example, we are updating the value of array element at index 2.'''
from array import *
array1 = array('i', [10,20,30,40,50])
array1[2] = 80
for x in array1:
    print(x)

'''-------------------------------- Python - Access Array Items ---------------------------
Accessing an array item in Python refers to the process of retrieving the value stored at a
specific index in the given array. Here, index is a numerical value that indicates the location
of array items. Thus, you can use this index to access elements of an array in Python.

Accessing array items in Python
You can use the following ways to access array items in Python −
     Using indexing
     Using iteration
     Using enumerate() function
'''
''' 
Using indexing
The process of accessing elements of an array through the index is known as Indexing. In
this process, we simply need to pass the index number inside the index operator []. The
index of an array in Python starts with 0 which means you can find its first element at
index 0 and the last at one less than the length of given array
Exampl:- '''
import array as arr
# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
#indexing
print (numericArray[0])
print (numericArray[1])
print (numericArray[2])

''' Using iteration
In this approach, a block of code is executed repeatedly using loops such as for and while.
It is used when you want to access array elements one by one.
Example
In the below code, we use the for loop to access all the elements of the specified array.'''
import array as arr
# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
# iteration through for loop
for item in numericArray:
    print(item)

''' Using enumerate() function
The enumerate() function can be used to access elements of an array. It accepts an array
and an optional starting index as parameter values and returns the array items by
iterating.
Example
In the below example, we will see how to use the enumerate() function to access array
items.'''
import array as arr
# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
# use of enumerate() function
for loc, val in enumerate(numericArray):
    print(f"Index: {loc}, value: {val}")

''' Accessing a range of array items in Python
In Python, to access a range of array items, you can use the slicing operation which is
performed using index operator [] and colon (:).
This operation is implemented using multiple formats, which are listed below −
     Use the [:index] format to access elements from beginning to desired range.
     To access array items from end, use [:-index] format.
     Use the [index:] format to access array items from specific index number till the
    end.
     Use the [start index : end index] to slice the array elements within a range. You
    can also pass an optional argument after end index to determine the increment
    between each index.
Example:- '''
import array as arr
# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
# slicing operation
print (numericArray[2:])
print (numericArray[0:3])

'''--------------------------------- Python - Add Array Items --------------------------
Python array is a mutable sequence which means they can be changed or modified
whenever required. However, items of same data type can be added to an array. In the
similar way, you can only join two arrays of the same data type.
Python does not have built-in support for arrays, it uses array module to
achieve the functionality like an array'''

''' Adding Elements to Python Array
There are multiple ways to add elements to an array in Python −
     Using append() method
     Using insert() method
     Using extend() method
'''
'''
Using append() method
To add a new element to an array, use the append() method. It accepts a single item as
an argument and append it at the end of given array.
Syntax:- append(v)
Where,
     v − new value is added at the end of the array. The new value must be of the same
    type as datatype argument used while declaring array object
    
Example:-'''
import array as arr
a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)

''' Using insert() method
It is possible to add a new element at the specified index using the insert() method. The
array module in Python defines this method. It accepts two parameters which are index
and value and returns a new array after adding the specified value.
Syntax:- insert(i, v)
Where,
     i − The index at which new value is to be inserted.
     v − The value to be inserted. Must be of the arraytype.
Example:- '''
import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1,20)
print (a)

''' Using extend() method
The extend() method belongs to Python array module. It is used to add all elements from
an iterable or array of same data type.
Syntax:- extend(x)
Where,
     x − This parameter specifies an array or iterable
Example:- '''
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)

'''---------------------------------- Python - Remove Array Items --------------------------
Removing array items in Python
Python arrays are a mutable sequence which means operation like adding new elements
and removing existing elements can be performed with ease. We can remove an element
from an array by specifying its value or position within the given array.

The array module defines two methods namely remove() and pop(). The remove() method
removes the element by value whereas the pop() method removes array item by its
position.

Python does not provide built-in support for arrays, however, we can use the
array module to achieve the functionality like an array'''

''' Remove First Occurrence
To remove the first occurrence of a given value from the array, use remove() method.
This method accepts an element and removes it if the element is available in the array.
Syntax:- array.remove(v)
        Where, v is the value to be removed from the array.

Example:-'''
import array as arr
# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.remove(311)
# after removing array
print ("After removing:", numericArray)

''' Remove Items from Specific Indices
To remove an array element from specific index, use the pop() method. This method
removes an element at the specified index from the array and returns the element at its
position after removal.
Syntax:- array.pop(i)
        Where, i is the index for the element to be removed.
Example:-
'''
import array as arr
# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])
# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.pop(3)
# after removing array
print ("After removing:", numericArray)

'''-------------------------------------- Python - Loop Arrays -------------------------
Loops are used to repeatedly execute a block of code. In Python, there are two types of
loops named for loop and while loop. Since the array object behaves like a sequence, you
can iterate through its elements with the help of loops.
'''
'''Python for Loop with Array
The for loop is used when the number of iterations is known. If we use it with an iterable
like array, the iteration continues until it has iterated over every element in the array.
Example:-'''
import array as arr
newArray = arr.array('i', [56, 42, 23, 85, 45])
for iterate in newArray:
    print (iterate)

''' Python while Loop with Array
In while loop, the iteration continues as long as the specified condition is true. When you
are using this loop with arrays, initialize a loop variable before entering the loop. 
This variable often represents an index for accessing elements in the array. Inside the while
loop, iterate over the array elements and manually update the loop variable.
Example:- '''
import array as arr
# creating array
a = arr.array('i', [96, 26, 56, 76, 46])
# checking the length
l = len(a)
# loop variable
idx = 0
# while loop
while idx < l:
    print (a[idx])
# incrementing the while loop
idx+=1

''' Python for Loop with Array Index
We can find the length of array with built-in len() function. Use it to create a range object
to get the series of indices and then access the array elements in a for loop.
Example:- '''
import array as arr
a = arr.array('d', [56, 42, 23, 85, 45])
l = len(a)
for x in range(l):
    print (a[x])

'''------------------------------------- Python - Copy Arrays ------------------------------
In Python, copying an array refers to the process of creating a new array that contains all
the elements of the original array. This operation can be done using assignment operator
(=) and deepcopy() method. In this chapter, we discuss how to copy an array object to
another. 
'''

''' Copy Arrays Using Assignment Operator
We can assign an array to another by using the assignment operator (=). However, such
assignment doesn't create a new array in the memory. Instead, it creates a new reference
to the same array.
Example:-
'''
import array as arr
a = arr.array('i', [110, 220, 330, 440, 550])
b = a
print("Copied array:",b)
print (id(a), id(b))
''' Here Check the id() of both a and b. Same value of id confirms that simple assignment doesn't
create a copy. Since "a" and "b" refer to the same array object, any change in the array
"a" will reflect in "b" too'''

''' Copy Arrays using Deep Copy
To create another physical copy of an array, we use another module in Python library,
named copy and use deepcopy() function in the module. A deep copy constructs a new
compound object and then, recursively inserts copies into it of the objects found in the
original.
Example:- '''
import array as arr
import copy
a = arr.array('i', [110, 220, 330, 440, 550])
b = copy.deepcopy(a)
print("Copied array:",b)

''' Now check the id() of both "a" and "b". You will find the ids are different.
This proves that a new object "b" is created which is an actual copy of "a". If we change
an element in "a", it is not reflected in "b".'''
print (id(a), id(b))

'''------------------------------------- Python - Reverse Arrays -------------------------
Reversing an array is the operation of rearranging the array elements in the opposite
order. There are various methods and approaches to reverse an array in Python including
reverse() and reversed() methods.

Ways to Reverse an Array in Python
To reverse an array, use the following approaches −
     Using slicing operation
     Using reverse() method
     Using reversed() method
     Using for loop'''

'''Using slicing operation
Slicing operation is the process of extracting a part of array within the specified indices.
In Python, if we use the slice operation in the form [::-1] , it will display a new array by
reversing the original one.
In this process, the interpreter starts from the end and stepping backwards by 1 until it
reaches the beginning of the array. As a result, we get a reverse copy of original array.
Example
The below example demonstrates how to use the slicing operation to reverse an array in
Python'''

import array as arr
# creating array
numericArray = arr.array('i', [88, 99, 77, 55, 66])
print("Original array:", numericArray)
revArray = numericArray[::-1]
print("Reversed array:",revArray)

''' Reverse an Array Using reverse() Method
We can also reverse the sequence of numbers in an array using the reverse() method of
list class. Here, list is a built-in type in Python.
Since reverse() is a method of list class, we cannot directly use it to reverse an array
created through the Python array module. We have to first transfer the contents of an
array to a list with tolist() method of array class, then we call the reverse() method and
at the end, when we convert the list back to an array, we get the array with reversed
order.
Example:- 
Here, we will see the use of reverse() method in reversing an array in Python.'''
import array as arr
# creating an array
numericArray = arr.array('i', [10,5,15,4,6,20,9])
print("Array before reversing:", numericArray)
# converting the array into list
newArray = numericArray.tolist()
# reversing the list
newArray.reverse()
# creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)

''' Reverse an Array Using reversed() Method
The reversed() method is another way to reverse elements of an array. It accepts an array
as a parameter value and returns an iterator object that displays array elements in reverse
order.
Example
In this example, we are using the reversed() method to reverse an array in Python.'''
import array as arr
# creating an array
numericArray = arr.array('i', [12, 10, 14, 16, 20, 18])
print("Array before reversing:", numericArray)
# reversing the array
newArray = list(reversed(numericArray))
# creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)

''' Using for Loop
To reverse an array using a for loop, we first traverse the elements of the original array in
reverse order and then append each element to a new array.
Example:- 
The following example shows how to reverse an array in Python using for loop.'''
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i')
for i in range(len(a)-1, -1, -1):
    b.append(a[i])
print(a)
print(b)

'''--------------------------------------- Python - Sort Arrays -----------------------------
The array class doesn't have any function/method to give a sorted arrangement of its
elements. However, we can achieve it with one of the following approaches −
     Using a sorting algorithm
     Using the sort() method from List
     Using the built-in sorted() function
Let's discuss each of these methods in detail.'''

''' Sort Arrays Using a Sorting Algorithm
We implement the classical bubble sort algorithm to obtain the sorted array. To do it, we
use two nested loops and swap the elements for rearranging in sorted order.
Example:- 
Run the following code using a Python code edito'''
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if(a[i] > a[j]):
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
print (a)

''' Sort Arrays Using sort() Method of List
Even though array module doesn't have a sort() method, Python's built-in List class does
have a sort method. We shall use it in the next example.

First, declare an array and obtain a list object from it, using tolist() method. Then, use the
sort() method to get a sorted list. Lastly, create another array using the sorted list which
will display a sorted array.
Example:- 
The following code shows how to get sorted array using the sort() method.'''
import array as arr
# creating array
orgnlArray = arr.array('i', [10,5,15,4,6,20,9])
print("Original array:", orgnlArray)
# converting to list
sortedList = orgnlArray.tolist()
# sorting the list
sortedList.sort()
# creating array from sorted list
sortedArray = arr.array('i', sortedList)
print("Array after sorting:",sortedArray)

''' Sort Arrays Using sorted() Method
The third technique to sort an array is with the sorted() function, which is a built-in
function.

The syntax of sorted() function is as follows −
sorted(iterable, reverse=False)

The function returns a new list containing all items from the iterable in ascending order.
Set reverse parameter to True to get a descending order of items.

The sorted() function can be used along with any iterable. Python array is an iterable as it
is an indexed collection. Hence, an array can be used as a parameter to sorted() function.'''
import array as arr
a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
sorted(a)
print(a)

'''-------------------------------------- Python - Join Arrays --------------------------------
The process of joining two arrays is termed as Merging or concatenating. Python provides
multiple ways to merge two arrays such as append() and extend() methods. But, before
merging two arrays always ensure that both arrays are of the same data type otherwise
program will throw error.

Join two Arrays in Python
To join arrays in Python, use the following approaches −
     Using append() method
     Using + operator
     Using extend() method'''

''' Using append() Method
To join two arrays, we can append each item from one array to other using append()
method. To perform this operation, run a for loop on the original array, fetch each element
and append it to a new array.

Example: 
Here, we use the append() method to join two arrays.'''
import array as arr
# creating two arrays
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
# merging both arrays
for i in range(len(b)):
    a.append(b[i])
print (a)

''' Using + operator
We can also use + operator to concatenate or merge two arrays. In this approach, we first
convert arrays to list objects, then concatenate the lists using the + operator and convert
back to get merged array.
Example:-
In this example, we will see how to join two arrays using + operator.'''
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
x = a.tolist()
y = b.tolist()
z = x+y
a = arr.array('i', z)
print (a)

''' Using extend() Method
Another approach to concatenate arrays is the use of extend() method from the List class.
Similar to above approach, we first convert the array to a list and then call the extend()
method to merge the two lists.

Example:-
In the following example, we will use the extend() method to concatenate two arrays in
Python.'''
import array as arr
a = arr.array('i', [88, 99, 77, 66, 44, 22])
b = arr.array('i', [12, 17, 18, 11, 13, 10])
a.extend(b)
print (a)

'''--------------------------------------- Python - Array Methods -----------------------------
The array module in Python offers an efficient object type for representing arrays of basic
values like characters, integers, and floating point numbers. Arrays are similar to lists but
they stores a collection of homogeneous data elements in order. At the time of creating
array's, type is specified using a single character type code.
Array methods provides various operations on array objects, including appending,
extending, and manipulating elements. These methods are used for efficient handling of
homogeneous collections of basic data types, making them suitable for tasks requiring
compact data storage, such as numerical computations.

Below are categorized methods based on their functionality.
Let's explore and understand the functionality of each method.
Arrays are created using the array.array(typecode[, initializer]) class, where typecode is
a single character that defines the type of elements in the array, and initializer is an
optional value used to initialize the array.
'''

'''Adding and Removing Elements
Below methods are used for appending, extending, inserting, and removing elements from
arrays

Sr.No. Methods with Description
1
append(x)
Appends a new item with value x to the end of the
array.
2
extend(iterable)
Appends items from iterable to the end of the
array.
3 insert(i, x)
Inserts a new item with value x before position i.
4
pop([i])
Removes and returns the item with index i. If i is
not specified, removes and returns the last item.
5 remove(x)
Removes the first occurrence of x from the array.'''