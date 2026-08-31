'''Creating Python Strings
As long as the same sequence of characters is enclosed, single or double or triple quotes
don't matter. Hence, following string representations are equivalent.'''

string1 = 'Hello, World!'
string2 = "Hello, World!"
string3 = '''Hello, World!'''
print(string1)
print(string2)
print(string3)

#----------------- Accessing Values in Strings -----------------
var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#----------------- Modifying Strings -----------------
var1 = var1[:6] + 'Python'
print("Modified String : ", var1)

#----------------- Escape Characters -----------------
'''
Following table is a list of escape or non-printable characters that can be represented with
backslash notation.
An escape character gets interpreted; in a single quoted as well as double quoted strings by Python.

    Backslash       Hexadecimal         Description
    notation        character   
    ------------------------------------------------------------- '''
#   '\a'               0x07                 Bell or alert
#   '\b'               0x08                 Backspace
#   '\cx'                                   Control-x
#   '\C-x'                                  Control-x
#   '\e'               0x1b                 Escape
#   '\f'               0x0c                 Formfeed
#   '\M-\C-x'                               Meta-Control-x
#   '\n'               0x0a                 Newline
#   '\nnn'                                    Octal notation, where n is in the range 0.7
#   '\r'               0x0d                 Carriage return
#   '\s'               0x20                 Space
#   '\t'               0x09                 Tab
#   '\v'               0x0b                 Vertical tab
#   '\x'                                    Character x
#   '\xnn'                                  Hexadecimal notation, where n is in the range 0.9, a.f, or A.F


'''-------------------- Double Quotes in Python Strings --------------------
You want to embed some text in double quotes as a part of string, the string itself should
be put in single quotes. To embed a single quoted text, string should be written in double
quotes.
Example:-'''
var = 'Welcome to "Python Tutorial" from TutorialsPoint'
print ("var:", var)
var = "Welcome to 'Python Tutorial' from TutorialsPoint"
print ("var:", var)

'''------------------ Built-in String Methods --------------------  
Python includes the following built-in methods to manipulate strings −
Sr.No.          Methods with Description
1                   capitalize()
                Capitalizes first letter of string.
2                   casefold()
                Converts all uppercase letters in string to lowercase. Similar to lower(), but works on
                UNICODE characters alos.
3                   center(width, fillchar)
                Returns a space-padded string with the original string centered to a total of width
                columns.
4                   count(str, beg= 0,end=len(string))
                Counts how many times str occurs in string or in a substring of string if starting index beg
                and ending index end are given.
5                   decode(encoding='UTF-8',errors='strict')
                Decodes the string using the codec registered for encoding. encoding defaults to the default
                string encoding.
6                   encode(encoding='UTF-8',errors='strict')
                Returns encoded string version of string; on error, default is to raise a ValueError unless
                errors is given with 'ignore' or 'replace'.
7                   endswith(suffix, beg=0, end=len(string))
                Determines if string or a substring of string (if starting index beg and ending index end are
                given) ends with suffix; returns true if so and false otherwise.
8                   expandtabs(tabsize=8)
                Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not
                provided.
9                   find(str, beg=0 end=len(string))
                Determine if str occurs in string or in a substring of string if starting index beg and
                ending index end are given returns index if found and -1 otherwise.
10                  format(*args, **kwargs)
                This method is used to format the current string value.
11                  format_map(mapping)
                This method is also use to format the current string the only difference is it uses a mapping object.
12                  index(str, beg=0, end=len(string))
                Same as find(), but raises an exception if str not found.
13                  isalnum()
                Returns true if string has at least 1 character and all characters are alphanumeric and false
                otherwise.
14                  isalpha()
                Returns true if string has at least 1 character
                and all characters are alphabetic and false
                otherwise.
15                  isascii()
                Returns True is all the characters in the string
                are from the ASCII character set.
16                  isdecimal()
                Returns true if a unicode string contains only decimal characters and false otherwise.
17                  isdigit()
                Returns true if string contains only digits and false otherwise.
18                  isidentifier()
                Checks whether the string is a valid Python identifier.
19                  islower()
                Returns true if string has at least 1 cased character and all cased characters are in
                lowercase and false otherwise.
20                  isnumeric()
                Returns true if a unicode string contains only numeric characters and false otherwise.
21                  isprintable()
                Checks whether all the characters in the string are printable.
22                  isspace()
                Returns true if string contains only whitespace characters and false otherwise.
23                  istitle()
                Returns true if string is properly "titlecased" and false otherwise.
24                  isupper()
                Returns true if string has at least one cased character and all cased characters are in
                uppercase and false otherwise.
25                  join(seq)
                Merges (concatenates) the string representations of elements in sequence seq
                into a string, with separator string.
26                  ljust(width[, fillchar])
                Returns a space-padded string with the original string left-justified to a total of width
                columns.
27                  lower()
                Converts all uppercase letters in string to
                lowercase.
28                  lstrip()
                Removes all leading white space in string.
29                  maketrans()
                Returns a translation table to be used in
                translate function.
30                  partition()
                Splits the string in three string tuple at the first occurrence of separator.
31                  removeprefix()
                Returns a string after removing the prefix string.
32                  removesuffix()
                Returns a string after removing the suffix string.
33                  replace(old, new [, max])
                Replaces all occurrences of old in string with new or at most max occurrences if max given.
34                  rfind(str, beg=0,end=len(string))
                Same as find(), but search backwards in string.
35                  rindex( str, beg=0, end=len(string))
                Same as index(), but search backwards in string.
36                  rjust(width,[, fillchar])
                Returns a space-padded string with the original string right-justified to a total of width
                columns.
37                  rpartition()
                Splits the string in three string tuple at the
                last occurrence of separator.
38                  rsplit()
                Splits the string from the end and returns a list of substrings.
39                  rstrip()
                Removes all trailing whitespace of string.
40                  split(str="", num=string.count(str))
                Splits string according to delimiter str (space if not provided) and returns list of substrings;
                split into at most num substrings if given.
41                  splitlines( num=string.count('\n'))
                Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs
                removed.
42                  startswith(str, beg=0,end=len(string))
                Determines if string or a substring of string (if
                starting index beg and ending index end are
                given) starts with substring str; returns true if
                so and false otherwise.
43                  strip([chars])
                Performs both lstrip() and rstrip() on string.
44                  swapcase()
                Inverts case for all letters in string.
45                  title()
                Returns "titlecased" version of string, that is, all words begin with uppercase and the rest
                are lowercase.
46                  translate(table, deletechars="")
                Translates string according to translation table str(256 chars), removing those in the del
                string.
47                  upper()
                Converts lowercase letters in string to uppercase.
48                  zfill (width)
                Returns original string leftpadded with zeros to
                a total of width characters; intended for
                numbers, zfill() retains any sign given (less
                one zero).
'''

'''------------------ Built-in Functions with Strings -----------------
Following are the built-in functions we can use with strings

Sr.No.          Function with Description
1                   len(list)
                Returns the length of the string.
2                   max(list)
                Returns the max alphabetical character from the string str.
3                   min(list)
                Returns the min alphabetical character from the string str.
'''

#------------------ String Operators -----------------
# 1. Concatenation
str1 = "Hello"
str2 = "World"  
str3 = str1 + " " + str2
print("Concatenated String: ", str3)
# 2. Repetition
str4 = "Python "* 3
print("Repeated String: ", str4)
# 3. Membership
str5 = "Programming"
print("g" in str5)  # True
print("z" not in str5)  # True
# 4. Slicing
str6 = "Hello, World!"
print("Sliced String: ", str6[0:5])  # Hello
# 5. Length
str7 = "Hello"
print("Length of String: ", len(str7))  # 5
# 6. Iteration
str8 = "Hi"
for char in str8:
    print(char)
# H
# i
# 7. Formatting
name = "Alice"  
age = 30
formatted_str = "Name: {}, Age: {}".format(name, age)
print("Formatted String: ", formatted_str)  # Name: Alice, Age: 30
# 8. Raw Strings
raw_str = r"C:\new_folder\test.txt"
print("Raw String: ", raw_str)  # C:\new_folder\test.txt
# 9. Multiline Strings
multi_str = """This is a
multiline
string."""
print("Multiline String: ", multi_str)
# This is a
# multiline
# string.   
# 10. String Methods
sample_str = " hello world "
print("Uppercase: ", sample_str.upper())  # " HELLO WORLD "
print("Stripped: ", sample_str.strip())    # "hello world"
print("Replaced: ", sample_str.replace("world", "Python"))  # " hello Python "
# 11. Joining Strings
str_list = ["Hello", "from", "Python"]
joined_str = " ".join(str_list)
print("Joined String: ", joined_str)  # "Hello from Python"
# 12. Splitting Strings
split_str = "apple,banana,cherry"
fruits = split_str.split(",")
print("Split Strings: ", fruits)  # ['apple', 'banana', 'cherry
# 13. Finding Substrings
main_str = "Hello, welcome to Python programming."
index = main_str.find("Python")
print("Index of 'Python': ", index)  # 18
# 14. Counting Substrings
count = main_str.count("o")
print("Count of 'o': ", count)  # 4
# 15. Checking String Start/End
print("Starts with 'Hello': ", main_str.startswith("Hello"))  # True
print("Ends with 'programming.': ", main_str.endswith("programming."))  # True
# 16. Capitalizing Strings
cap_str = "hello world"
print("Capitalized String: ", cap_str.capitalize())  # "Hello world"
# 17. Centering Strings
centered_str = "Hello".center(20, '*')
print("Centered String: ", centered_str)  # *******Hello********
# 18. Justifying Strings
left_justified = "Hello".ljust(20, '-')
print("Left Justified String: ", left_justified)  # Hello---------------
right_justified = "Hello".rjust(20, '-')
print("Right Justified String: ", right_justified)  # ---------------Hello      
# 19. Encoding Strings
encoded_str = "Hello".encode("utf-8")
print("Encoded String: ", encoded_str)  # b'Hello'
# 20. Decoding Strings
decoded_str = encoded_str.decode("utf-8")
print("Decoded String: ", decoded_str)  # Hello
# These examples demonstrate various string operations and methods available in Python.

#------------------ String Methods -----------------
# Here are some commonly used string methods in Python with examples:
sample_str = "  Hello, World! Welcome to Python programming.  "
print("Original String: '", sample_str, "'")
# 1. strip() - Removes leading and trailing whitespace
print("strip(): '", sample_str.strip(), "'")
# 2. lower() - Converts string to lowercase
print("lower(): '", sample_str.lower(), "'")
# 3. upper() - Converts string to uppercase
print("upper(): '", sample_str.upper(), "'")
# 4. replace() - Replaces occurrences of a substring with another substring
print("replace(): '", sample_str.replace("World", "Universe"), "'")
# 5. split() - Splits the string into a list of substrings based on a delimiter
print("split(): ", sample_str.split(","))
# 6. join() - Joins a list of strings into a single string with a specified delimiter
str_list = ["Hello", "from", "Python"]
print("join(): '", " ".join(str_list), "'")
# 7. find() - Returns the lowest index of the substring if found, otherwise -
print("find(): ", sample_str.find("Python"))
# 8. count() - Returns the number of occurrences of a substring
print("count(): ", sample_str.count("o"))
# 9. startswith() - Checks if the string starts with a specified substring
print("startswith(): ", sample_str.startswith("  Hello"))
# 10. endswith() - Checks if the string ends with a specified substring 
print("endswith(): ", sample_str.endswith("programming.  "))
# 11. capitalize() - Capitalizes the first character of the string
print("capitalize(): '", sample_str.capitalize(), "'")
# 12. title() - Converts the first character of each word to uppercase
print("title(): '", sample_str.title(), "'")
# 13. isalpha() - Checks if all characters in the string are alphabetic
print("isalpha(): ", sample_str.isalpha())
# 14. isdigit() - Checks if all characters in the string are digits
print("isdigit(): ", sample_str.isdigit())
# 15. isspace() - Checks if all characters in the string are whitespace
print("isspace(): ", sample_str.isspace())
# These methods provide a wide range of functionalities to manipulate and analyze strings in Python.
# Note: The output of each method is printed for demonstration purposes.

#------------------ String Formatting -----------------
# Here are some examples of string formatting in Python:
name = "Alice"
age = 30
# 1. Using the format() method
formatted_str1 = "My name is {} and I am {} years old.".format(name, age)
print("Using format(): ", formatted_str1)
# 2. Using f-strings (Python 3.6+)
formatted_str2 = f"My name is {name} and I am {age} years old."
print("Using f-strings: ", formatted_str2)
# 3. Using % operator   
formatted_str3 = "My name is %s and I am %d years old." % (name, age)
print("Using % operator: ", formatted_str3)
# 4. Formatting numbers
pi = 3.14159
formatted_str4 = "The value of pi is approximately {:.2f}.".format(pi)
print("Formatting numbers: ", formatted_str4)
formatted_str5 = f"The value of pi is approximately {pi:.2f}."
print("Formatting numbers with f-strings: ", formatted_str5)
# 5. Padding and alignment
formatted_str6 = "{:<10} | {:^10} | {:>10}".format("Left", "Center", "Right")
print("Padding and alignment: \n", formatted_str6)
formatted_str7 = f"{'Left':<10} | {'Center':^10} | {'Right':>10}"
print("Padding and alignment with f-strings: \n", formatted_str7)
# 6. Using dictionary for formatting
data = {"name": "Bob", "age": 25}
formatted_str8 = "My name is {name} and I am {age} years old.".format(**data)
print("Using dictionary for formatting: ", formatted_str8)
formatted_str9 = f"My name is {data['name']} and I am {data['age']} years old."
print("Using dictionary for formatting with f-strings: ", formatted_str9)
# These examples demonstrate various ways to format strings in Python, allowing for dynamic and readable output.
# Note: The output of each formatting method is printed for demonstration purposes.
#------------------ String Immutability -----------------
# In Python, strings are immutable, meaning once a string is created, it cannot be changed
original_str = "Hello, World!"
print("Original String: ", original_str)
# Attempting to change a character in the string will raise an error
try:
    original_str[0] = 'h'  # This will raise a TypeError
except TypeError as e:
    print("Error: ", e)
# To modify a string, you need to create a new string
modified_str = 'h' + original_str[1:]
print("Modified String: ", modified_str)
# Demonstrating that the original string remains unchanged
print("Original String after modification attempt: ", original_str)
# This shows that strings in Python are immutable and any modification results in a new string being created
# Note: The error message is printed for demonstration purposes.
#------------------ String Encoding and Decoding -----------------
# In Python, strings are Unicode by default. You can encode a string to bytes and decode

# bytes back to a string using the encode() and decode() methods.
# Example string
original_str = "Hello, World!"
print("Original String: ", original_str)
# Encoding the string to bytes using UTF-8 encoding
encoded_str = original_str.encode('utf-8')
print("Encoded String (bytes): ", encoded_str)
# Decoding the bytes back to a string using UTF-8 encoding
decoded_str = encoded_str.decode('utf-8')
print("Decoded String: ", decoded_str)
# Demonstrating that the decoded string is the same as the original string
print("Decoded String is same as Original: ", decoded_str == original_str)
# This shows how to encode and decode strings in Python using UTF-8 encoding.
# Note: The output of each step is printed for demonstration purposes.
#------------------ Raw Strings -----------------
# In Python, raw strings are prefixed with 'r' or 'R' and treat
# backslashes as literal characters, which is useful for regular expressions and file paths.
# Example of a normal string with escape characters
normal_str = "C:\\new_folder\\test.txt"
print("Normal String: ", normal_str)
# Example of a raw string
raw_str = r"C:\new_folder\test.txt"
print("Raw String: ", raw_str)
# Demonstrating that both strings are equivalent
print("Strings are equal: ", normal_str == raw_str)
# This shows how raw strings work in Python and how they differ from normal strings with escape characters
# Note: The output of each step is printed for demonstration purposes.

#------------------ Old-Style String Formatting -----------------
print ("My name is %s and weight is %d kg!" % ('Zara', 21))
''' Here is the list of complete set of symbols which can be used along with % −
Sr.No.      Format Symbol & Conversion
1                   %c
                character
2                   %s
                string conversion via str() prior to
                formatting
3                   %i
                signed decimal integer
4                   %d
                signed decimal integer
5                   %u
                unsigned decimal integer
6                   %o
                octal integer
7                   %x
                hexadecimal integer (lowercase letters)
8                   %X
                hexadecimal integer (UPPERcase letters)
9                   %e
                exponential notation (with lowercase 'e')
10                  %E
                exponential notation (with UPPERcase 'E')
11                  %f
                floating point real number
12                  %g
                the shorter of %f and %e
13                  %G
                the shorter of %f and %E

# Other supported symbols and functionality are listed in the following table

Sr.No.          Symbol & Functionality
1                   *       
                argument specifies width or precision
2                   -
                left justification
3                   +
                display the sign
4                   <sp>
                leave a blank space before a positive number
5                   #
                add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or
                'X' were used.
6                   0
                pad from left with zeros (instead of spaces)
7                   %
                '%%' leaves you with a single literal '%'
8                   (var)
                mapping variable (dictionary arguments)
9                   m.n.
                m is the minimum total width and
                n is the number of digits to
                display after the decimal point (if
                appl.)
'''


#---------------------------- Examples ------------------------------
'''Example 1
Python program to find number of vowels in a given string'''
mystr = "All animals are equal. Some are more equal"
vowels = "aeiou"
count=0
for x in mystr:
    if x.lower() in vowels: count+=1
print ("Number of Vowels:", count)

'''Example 2
Python program to convert a string with binary digits to integer.'''
mystr = '10101'
def strtoint(mystr):
    for x in mystr:
        if x not in '01': return "Error. String with non-binary characters"
    num = int(mystr, 2)
    return num
print ("binary:{} integer: {}".format(mystr,strtoint(mystr)))

'''Example 3
Python program to drop all digits from a string'''

digits = [str(x) for x in range(10)]
mystr = 'He12llo, Py00th55on!'
chars = []
for x in mystr:
    if x not in digits:
        chars.append(x)
newstr = ''.join(chars)
print (newstr)

'''
Exercise Programs to be done:- 
     Python program to sort the characters in a string
     Python program to remove duplicate characters from a string
     Python program to list unique characters with their count in a string
     Python program to find number of words in a string
     Python program to remove all non-alphabetic characters from a string
'''