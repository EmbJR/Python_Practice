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


'''
Primitive Types The primitive data types are the fundamental data types that are used to create complex data types (sometimes called complex data structures). There are mainly four primitive data types, which are 
      Integers 
      Floats
       Booleans, and 
       Strings
Non-primitive Types
     Lists 
     Tuples 
     Dictionaries, 
     Sets
'''
# Data Type Conversion Functions
'''
There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.

Sr.No. Function & Description 
1 Python int() function Converts x to an integer. base specifies the base if x is a string. 
2 Python long() function Converts x to a long integer. base specifies the base if x is a string. This function has been deprecated. 
3 Python float() function  Converts x to a floating-point number. 
4 Python complex() function  Creates a complex number. 
5 Python str() function  Converts object x to a string representation. 
6 Python repr() function  Converts object x to an expression string. 
7 Python eval() function Evaluates a string and returns an object.
8 Python tuple() function Converts s to a tuple. 
9 Python list() function Converts s to a list. 
10 Python set() function  Converts s to a set. 
11 Python dict() function Creates a dictionary. d must be a sequence of (key,value) tuples. 
12 Python frozenset() function  Converts s to a frozen set. 
13 Python chr() function  Converts an integer to a character. 
14 Python unichr() function Converts an integer to a Unicode character. 
15 Python ord() function  Converts a single character to its integer value. 
16 Python hex() function  Converts an integer to a hexadecimal string. 
17 Python oct() function  Converts an integer to an octal string.
'''

# Python Tutorial 13. Python - Type Casting
# Python Implicit Casting 
'''When a compiler/interpreter of any language automatically converts object of one type into other, it is called automatic or implicit casting.
'''
a = 10 # int object
b = 10.4 # Float object

c = a+b
print(c)

# Python Explicit Casting 
'''Although automatic or implicit casting is limited to int to float conversion, you can use Python's built-in functions int(), float() and str() to perform the explicit conversions such as string to integer.'''

#1 Python int() Function
a = int(10.5)
print(type(a))

a = int("123")
print(type(a))

h = "4356"
h1 = "213de"
print(h.isdigit())
print(h1.isdigit())
if h.isdigit():
     print(int(h))

# Binary String to Integer
a = int("110011", 2)
print (a)

# Octal String to Integer
a = int("20", 8) 
print(a)

# Hexa-Decimal String to Integer
a = int("2A9", 16)
print(a)

#2 Python float() Function
'''In Python, there is no restriction on how many digits after the decimal point can a floating
point number have. However, to shorten the representation, the E or e symbol is used. E
stands for Ten raised to. For example, E4 is 10 raised to 4 (or 4th power of 10), e-3 is 10
raised to -3.
In scientific notation, number has a coefficient and exponent part. The coefficient should
be a float greater than or equal to 1 but less than 10. Hence, 1.23E+3, 9.9E-5, and 1E10
are the examples of floats with scientific notation.
'''
a = float(9.99)
print(type(a))

g = float( "12.76")
print(g)

'''
In mathematics, infinity is an abstract concept. Physically, infinitely large number can
never be stored in any amount of memory. For most of the computer hardware
configurations, however, a very large number with 400th power of 10 is represented by
Inf. If you use "Infinity" as argument for float() function, it returns Inf
'''
a=1.00E400
print (a, type(a))
a=float("Infinity")

'''
One more such entity is Nan (stands for Not a Number). It represents any value that is
undefined or not representable
'''
a=float("Nan")
print(a)

#3 Python str() Function
a = str(10.4)
print(type(a))
print(a)

v = str(10E4)
print(v)

a=str([1,2,3])
b=str((1,2,3))
print(a)
print(b)

#4 Conversion of Sequence Types

a=[1,2,3,4,5]  # List Object 
b=(1,2,3,4,5)  # Tuple Object 
c="Hello"   # String Object

obj=list(c)
print(obj)

obj=tuple(c)
print(obj)

obj=str(a)
print(obj)

#–--------------------------------------------------------------
# Python Tutorial 14. Python - Unicode System

'''A character is the smallest possible component of a text. 'A', 'B', 'C', etc., are all different characters. So are 'È' and 'Í'.
A unicode string is a sequence of code points, which are numbers from 0 through 0x10FFFF (1,114,111 decimal). 
This sequence of code points needs to be represented in memory as a set of code units, and code units are then mapped to 8-bit bytes which is called.
The rules for translating a Unicode string into a sequence of bytes are called a character encoding.

Python 3.0 onwards has built-in support for Unicode. The default encoding for Python source code is UTF-8.

'''
var = "\u0031\u0030" 
print (var)

'''Strings display the text in a human-readable format, and bytes store the characters as binary data. 
Encoding converts data from a character string to a series of bytes. 
Decoding translates the bytes back to human-readable characters and symbols. 
It is important not to confuse these two methods. Encode is a string method, while decode is a method of the Python byte object.
'''
string = "Hello" 
tobytes = string.encode('utf-8') 
print (tobytes) 
string = tobytes.decode('utf-8') 
print (string)

'''In the following example, the Rupee symbol (₹) is stored in the variable using its Unicode value. 
We convert the string to bytes and back to str.'''
string = "\u20B9" 
print (string) 
tobytes = string.encode('utf-8') 
print (tobytes) 
string = tobytes.decode('utf-8') 
print (string)


#-------------------------------------------------------------
#15. Python - Literals

