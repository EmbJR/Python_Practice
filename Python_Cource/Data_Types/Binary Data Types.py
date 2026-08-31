# 6. Python Binary Data Types
'''A binary data type in Python is a way to represent data as a series of binary digits, which
are 0's and 1's.
Python provides three different ways to represent binary data. They are as follows −
     bytes
     bytearray
     memoryview
'''
#6a. Bytes Data Type
b1 = bytes([65, 66, 67, 68, 69])
print(b1)

'''Here we are using the "b" prefix before a string to automatically create a bytes objec'''
# Using prefix 'b' to create bytes
b2 = b'Hello'
print(b2)

#6b. Python Bytearray Data Type
'''The bytearray data type in Python is quite similar to the bytes data type, but with one key
difference: it is mutable, meaning you can modify the values stored in it after it is createdBytearray Data Type'''
# Creating a bytearray from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])
print(value)

'''Now, we are creating a bytearray by encoding a string using a "UTF-8" encoding'''
# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')
print(val)

#6c. Python Memoryview Data Type
'''In Python, a memoryview is a built-in object that provides a view into the memory of the
original object, generally objects that support the buffer protocol, such as byte arrays (bytearray) and bytes (bytes)
You can create a memoryview using various methods. These methods include using the memoryview() constructor, slicing bytes or bytearray objects, extracting from array
objects, or using built-in functions like open() when reading from files.

In the given example, we are creating a memoryview object directly by passing a
supported object to the memoryview() constructor. The supported objects generally
include byte arrays (bytearray), bytes (bytes), and other objects that support the buffer
protocol.'''
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)
'''If you have an array object, you can create a memoryview using the buffer interface as
shown below:'''
import array
arr = array.array('i', [1, 1, 1])
view = memoryview(arr)
print(view)
# You can also create a memoryview by slicing a bytes or bytearray object
data = b'Hello, world!'
# Creating a view of the last part of the data
view = memoryview(data[7:])
print(view)