'''-------------------- String modification using the Array Module ---------------------'''
import array as ar
# initializing a string
s1="WORD"
print ("original string:", s1)
# converting it to an array
sar=ar.array('w', s1)
# inserting an element
sar.insert(3,"L")
# getting back the modified string
s1=sar.tounicode()
print ("Modified string:", s1)
'''-------------------- Using the StringIO Class ---------------------
Python's io module defines the classes to handle streams. The StringIO class represents a
text stream using an in-memory text buffer. A StringIO object obtained from a string
behaves like a File object. Hence we can perform read/write operations on it. The
getvalue() method of StringIO class returns a string
Example:-'''
import io
s1="WORD"
print ("original string:", s1)
sio=io.StringIO(s1)
sio.seek(3)
sio.write("LD")
s1=sio.getvalue()
print ("Modified string:", s1)

'''-------------------- Using the bytearray() function ---------------------
The bytearray() function returns a mutable byte array object. We can modify the byte array
Example:-'''
s1="WORD"
print ("original string:", s1)
barr=bytearray(s1, 'utf-8')
barr[3]=ord('L')
s1=barr.decode('utf-8')
print ("Modified string:", s1)

'''-------------------- String Concatenation using '+' operator ---------------------'''
s1="WORD"
print ("original string:", s1)
s1=s1[:3] + "LD"
print ("Modified string:", s1)

'''--------------------- String Concatenation by Multiplying ---------------------'''
newString = "Hello" * 3
print(newString)

'''--------------------- String Concatenation with '+' and '*' Operators ---------------------
The "*" operator has a higher precedence over
the "+" operator
Example:'''
s1="WORD"
print ("original string:", s1)
s1=s1[:3] + "L" * 2
print ("Modified string:", s1)


#--------------------- formating strings ---------------------
''' Hence, Python offers following string formatting techniques −
     Using % operator
     Using format() method of str class
     Using f-string
     Using String Template class'''
'''--------------------- Using % operator ---------------------'''
name = "Tutorialspoint"
print("Welcome to %s!" % name)
'''--------------------- Using format() method of str class ---------------------
It is a built-in method of str class. The format() method works by defining placeholders
within a string using curly braces "{}". These placeholders are then replaced by the values
specified in the method's arguments.'''
str = "Welcome to {}"
print(str.format("Tutorialspoint"))

'''--------------------- Using f-string ---------------------
The f-strings, also known as formatted string literals, is used to embed expressions inside
string literals. The "f" in f-strings stands for formatted and prefixing it with strings creates
58. Python - String Formatting an f-string. The curly braces "{}" within the string will then act as placeholders that is
filled with variables, expressions, or function calls.'''
item1_price = 2500
item2_price = 300
total = f'Total: {item1_price + item2_price}'
print(total)
'''--------------------- Using String Template class ---------------------
The String Template class belongs to the string module and provides a way to format
strings by using placeholders. Here, placeholders are defined by a dollar sign ($) followed
by an identifie'''
from string import Template
# Defining template string
str = "Hello and Welcome to $name !"
# Creating Template object
templateObj = Template(str)
# now provide values
new_str = templateObj.substitute(name="Tutorialspoint")
print(new_str)

'''--------------------- Escape characters in strings ---------------------
Tt tells the Interpreter that this escape character (sequence) has a special meaning. 
For instance, \n is an escape sequence that represents a newline. When Python encounters 
this sequence in a string, it understands that it needs to start a new line.

Unless an 'r' or 'R' prefix is present, escape sequences in string and byte literals are
interpreted according to rules similar to those used by Standard C. In Python, a string
becomes a raw string if it is prefixed with "r" or "R" before the quotation symbols. Hence
'Hello' is a normal string whereas r'Hello' is a raw string.
Example:-'''
# normal string
normal = "Hello"
print (normal)
# raw string
raw = r"Hello"
print (raw)
'''In normal circumstances, there is no difference between the two. However, when the
escape character is embedded in the string, the normal string actually interprets the
escape sequence, whereas the raw string doesn't process the escape character.
Example:- 
In the following example, when a normal string is printed the escape character '\n' is
processed to introduce a newline. However, because of the raw string operator 'r' the
effect of escape character is not translated as per its meaning.'''
normal = "Hello\nWorld"
print (normal)
raw = r"Hello\nWorld"
print (raw)

'''-------------- Escape Characters in Python -------------------
The following table shows the different escape characters used in Python -
#------- Escape Characters and Meaning ---------------------------------
Sr.No.           Escape Sequence & Description 
---------------------------------------------------------'''
#1                          \<newline>  
                     #Backslash and newline ignored 
#2                          \\ 
                    #Backslash (\) 
#3                          \' 
                    #Single quote (') 
#4                          \" 
                    #Double quote (") 
#5                          \a 
                    #ASCII Bell (BEL) 
#6                          \b 
                    #ASCII Backspace (BS) 
#7                          \f 
                    #ASCII Formfeed (FF) 
#8                          \n 
                    #ASCII Linefeed (LF) 
#9                          \r 
                    #ASCII Carriage Return (CR) 
#10                         \t 
                    #ASCII Horizontal Tab (TAB) 
#11                         \v 
                    #ASCII Vertical Tab (VT) 
#12                         \ooo 
                    #Character with octal value ooo 
#13                         \xhh 
                    #Character with hex value hh

#Example:-
# ignore \
s = 'This string will not include \
backslashes or newline characters.'
print (s)
# escape backslash
s=s = 'The \\character is called backslash'
print (s)
# escape single quote
s='Hello \'Python\''
print (s)
# escape double quote
s="Hello \"Python\""
print (s)
# escape \b to generate ASCII backspace
s='Hel\blo'
print (s)
# ASCII Bell character
s='Hello\a'
print (s)
# newline
s='Hello\nPython'
print (s)
# Horizontal tab
s='Hello\tPython'
print (s)
# form feed
s= "hello\fworld"
print (s)
# Octal notation
s="\101"
print(s)
# Hexadecimal notation
s="\x41"
print (s)