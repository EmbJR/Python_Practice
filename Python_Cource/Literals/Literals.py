'''
Python literals or constants are the notation for representing a fixed value in source code.
In contrast to variables, literals (123, 4.3, "Hello") are static values or you can say
constants which do not change throughout the operation
'''
#a. Python Integer Literal
#1 Decimal Literal
x = 10
y = -20

#2 Octal Litera
x = 0O34

#3 Hexadecimal Literal
y = 0x5A

#4 Float Literal
x = 25.55
z = -12.2345
'''For a floating point number which is too large or too small, where number of digits before
or after decimal point is more, a scientific notation is used for a compact literal representation. The symbol E or e followed by positive or negative integer, follows after
the integer part.
>> Example of Float Scientific Notation Literal
For example, a number 1.23E05 is equivalent to 123000.00. Similarly, 1.23e-2 is
equivalent to 0.0123'''

x = 1.23E5
print ("1.23E5 in scientific notation is", x, type(x))
x = 1.23E-2
print ("1.23E-2 in scientific notation is", x, type(x))

#5 Python Complex Literal
'''
A complex number comprises of a real and imaginary component. The imaginary
component is any number (integer or floating point) multiplied by square root of "-1"
(√ −1). In literal representation (√-1) is representation by "j" or "J". Hence, a literal
representation of a complex number takes a form x+yj.'''

x = 2+3j
print ("2+3j complex literal is", x, type(x))
y = 2.5+4.6j
print ("2.5+4.6j complex literal is", x, type(x))

#b. Python String Literal

str1 = 'hello'
str2 = "hello"
str3 = '''hello'''
str4 = """hello"""
print(str1)
print(str2)
print(str3)
print(str4)
var1='Welcome to "Python Tutorial" from TutorialsPoint'
print (var1)
var2="Welcome to 'Python Tutorial' from TutorialsPoint"
print (var2)

#c Python List Literal
L1=[1,"Ravi",75.50, True]
print("List L1:", L1, type(L1))

#d Python Tuple Literal
T1=(10, "Hello", 25.50, False)
print("Tuple T1:", T1, type(T1))

T2=1,"Ravi",75.50, True
print (T2, type(T2))

#e Python Dictionary Literal
'''Here, Key should not be repeated. Values can repeat for different keys.'''
D1={"Name":"Ravi", "Age":25, "Salary":75000.50, "IsEmployed":True}
print("Dictionary D1:", D1, type(D1))