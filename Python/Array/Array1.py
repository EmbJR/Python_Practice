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
'''

