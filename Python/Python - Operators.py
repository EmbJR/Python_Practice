'''
Docstring for Python - Operators
Python operators are special symbols used to perform specific operations on one or more
operands like '+' '-' 
>> Unary operators: 
Python operators that require one operand to perform a specific
operation are known as unary operators.
>> Binary operators: Python operators that require two operands to perform a
specific operation are known as binary operators.
>>Operands: Variables, values, or expressions that are used with the operator to
perform a specific operation are known as operands.

# Types of Python Operators
Python operators are divided in the following categories −
 Arithmetic Operators
 Comparison (Relational) Operators
 Assignment Operators
 Logical Operators
 Bitwise Operators
 Membership Operators
 Identity Operators'''

#a. Arithmetic Operators
'''
examples (assume that the values of a and b are 10 and 20, respectively) −
Operator Name               Example
+       Addition            a + b = 30
-       Subtraction         a - b = -10
*       Multiplication      a * b = 200
/       Division            b / a = 2
%       Modulus             b % a = 0
**      Exponent            a**b =10**20
//      Floor Division      9//2 = 4
'''

#b. Comparison (Relational) Operators
'''
examples (assume that the values of a and b are 10 and 20, respectively) −
Operator        Name                        Example
==              Equal                       (a == b) is not true.
!=              Not equal                   (a != b) is true.
>               Greater than                (a > b) is not true.
<               Less than                   (a < b) is true.
>=              Greater than or equal to    (a >= b) is not true.
<=              Less than or equal to       (a <= b) is true.
'''

#c. Assignment Operators
'''
Python Assignment Operators
Python Assignment operators are used to assign values to variables.

Operator            Example                 Same As
=                   a = 10                  a = 10
+=                  a += 30                 a = a + 30
-=                  a -= 15                 a = a - 15
*=                  a *= 10                 a = a * 10
/=                  a /= 5                  a = a / 5
%=                  a %= 5                  a = a % 5
**=                 a **= 4                 a = a ** 4
//=                 a //= 5                 a = a // 5
&=                  a &= 5                  a = a & 5
|=                  a |= 5                  a = a | 5
^=                  a ^= 5                  a = a ^ 5
>>=                 a >>= 5                 a = a >> 5
<<=                 a <<= 5                 a = a << 5
'''

#d Python Bitwise Operators
'''
Operator            Name            Example
&                   AND               a & b
|                   OR                a | b
^                   XOR               a ^ b
~                   NOT               ~a
<<            Zero fill left shift    a << 3
>>            Signed right shift      a >> 3
'''
a = 20
b = 10
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0
c = a & b;
print ("result of AND is ", c,':',bin(c))
c = a | b;
print ("result of OR is ", c,':',bin(c))
c = a ^ b;
print ("result of EXOR is ", c,':',bin(c))
c = ~a;
print ("result of COMPLEMENT is ", c,':',bin(c))
c = a << 2;
print ("result of LEFT SHIFT is ", c,':',bin(c))
c = a >> 2;
print ("result of RIGHT SHIFT is ", c,':',bin(c))

#e. Logical Operators
'''
Operator        Name        Example
and             AND         a and b
or              OR          a or b
not             NOT         not(a)
'''

#f. Membership Operators
'''
Python's membership operators test for membership in a sequence, such as strings, lists,
or tuples.
There are two membership operators as explained below

Operator        Description                         Example
in              Returns True if it finds a
                variable in the specified
                sequence, false otherwise.          a in b
not in          returns True if it does not finds
                a variable in the specified
                sequence and false otherwise.       a not in b
'''
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
print ("a:", a, "b:", b, "list:", list)
if ( a in list ):
    print ("a is present in the given list")
else:
    print ("a is not present in the given list")
if ( b not in list ):
    print ("b is not present in the given list")
else:
    print ("b is present in the given list")
c=b/a
print ("c:", c, "list:", list)
if ( c in list ):
    print ("c is available in the given list")
else:
    print ("c is not available in the given list")

#g. Identity Operators
'''
Python Identity Operators
Python identity operators compare the memory locations of two objects.
There are two Identity operators explained below.
Operator                    Description                     Example
is                      Returns True if both
                        variables are the same
                        object and false otherwise.         a is b
is not                  Returns True if both
                        variables are not the same
                        object and false otherwise.         a is not b
'''

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a
print(a is c)
print(a is b)
print(a is not c)
print(a is not b)

var = (10,20,30,40)
a = 10
b = 20
print ((a,b), "in", var, ":", (a,b) in var)
var = ((10,20),30,40)
a = 10
b = 20
print ((a,b), "in", var, ":", (a,b) in var)

# Python Operators Precedence
'''
Operators precedence decides the order of the evaluation in which an operator is
evaluated. Python operators have different levels of precedence.

The following table lists all operators from highest precedence to lowest.
Sr.No.          Operator & Description
1                   **
2                   ~ + -
3                   * / % //
4                    + -
5                   >> <<
6                   & Bitwise 'AND'
7                   ^ |
8                   <= < > >=
9                   <> == !=
10                  = %= /= //= -= += *= **=
11                  is is not
12                  in not in
13                  not or and
'''


#------------- Some examples --------------------------------------
a=6+4j
b=3+2j
c=a/b
c=(6+4j)/(3+2j)
c=(6+4j)*((3-2j)/(3+2j))*(3-2j)
c=(18-12j+12j+8)/(9-6j+6j+4)
c=26/13
c=2+0j


#-------------------------------------------------------------
'''Although complex object is a number data type in Python, its behavior is different from
others. Python doesn't support < and > operators, however it does support equality (==)
and inequality (!=) operators.
Example'''

print ("comparison of complex numbers")
a=10+1j
b=10.-1j
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)
#print ("a=",a, "b=",b,"a<b is",a<b) # will not work
#print ("a=",a, "b=",b,"a>b is",a>b) # will not work

#-------------------------------------------------------------------
'''Comparison of Sequence Types
In Python, comparison of only similar sequence objects can be performed. A string object
is comparable with another string only. A list cannot be compared with a tuple, even if
both have same items. 
Example'''
print ("comparison of different sequence types")
a=(1,2,3)
b=[1,2,3]
#print ("a=",a, "b=",b,"a<b is",a<b)

# Example 2
a=(1,2,4)
b=(1,2,3)
print ("a=",a, "b=",b,"a<b is",a<b)
print ("a=",a, "b=",b,"a>b is",a>b)
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)

# Comparison of Dictionary Objects
'''
The use of "<" and ">" operators for Python's dictionary is not defined. In case of these
operands, TypeError: '<' not supported between instances of 'dict' and 'dict' is reported.
Equality comparison checks if the length of both the dict items is same. Length of
dictionary is the number of key-value pairs in it.
Python dictionaries are simply compared by length. The dictionary with fewer elements is
considered less than a dictionary with more elements.
'''
print ("comparison of dictionary objects")
a={1:1,2:2}
b={2:2, 1:1, 3:3}
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)

# Python Logical Operators
age = 30
percentage = 85
marks = 90
attendance = 80
if age > 16 and marks > 80:
    print("Eligible for scholarship")
if percentage < 50 or attendance < 75:
    print("Not eligible for exam")
'''Along with the keyword False, Python interprets None, numeric zero of all types, and
empty sequences (strings, tuples, lists), empty dictionaries, and empty sets as False. All
other values are treated as True'''

x = 10
y = 20
gx = x & y
vx = x | y
print(gx, vx)
g = a and b
v = a or b
print(g, v)