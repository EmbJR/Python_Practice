'''----------------------------- Python - Syntax Errors --------------------------
Python Syntax Errors
In Python, syntax errors are among the most common errors encountered by
programmers, especially those who are new to the language. This tutorial will help you
understand what syntax errors are, how to identify them, and how to fix them.'''

''' What is a Syntax Error?
A syntax error in Python (or any programming language) is an error that occurs when the
code does not follow the syntax rules of the language. Syntax errors are detected by the
interpreter or compiler at the time of parsing the code, and they prevent the code from
being executed.'''

''' Common Causes of Syntax Errors
Following are the common causes of syntax errors −
     Missing colons (:) after control flow statements (e.g., if, for, while)
     Incorrect indentation − Python uses indentation to define the structure of code
        blocks. Incorrect indentation can lead to syntax errors
     Misspelled keywords or incorrect use of keywords
     Unmatched parentheses, brackets, or braces − Python requires that all opening
        parentheses (, square brackets [, and curly braces { have corresponding closing
        characters ), ], and }    '''

''' How to Identify Syntax Errors?
Identifying syntax errors in Python can sometimes be easy, especially when you get a
clear error message from the interpreter. However, other times, it can be a bit tricky. Here
are several ways to help you identify and resolve syntax errors effectively −'''

''' Reading Error Messages
When you run a Python script, the interpreter will stop execution and display an error
message if it encounters a syntax error. Understanding how to read these error messages
is very important.
Example Error Message
-----------------------------------
File "script.py", line 1
print("Hello, World!"
^
SyntaxError: EOL while scanning string literal
----------------------------------

This error message can be broken down into parts −
     File "script.py": Indicates the file where the error occurred.
     line 1: Indicates the line number in the file where the interpreter detected the
        error.
     print("Hello, World!": Shows the line of code with the error.
     ^: Points to the location in the line where the error was detected.'''