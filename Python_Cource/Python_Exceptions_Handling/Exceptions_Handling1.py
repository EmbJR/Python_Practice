
'''------------------- Exception Handling in Python ---------------------
Exception handling in Python refers to managing runtime errors that may occur during the
execution of a program. In Python, exceptions are raised when errors or unexpected
situations arise during program execution, such as division by zero, trying to access a file
that does not exist, or attempting to perform an operation on incompatible data types.
Python provides two very important features to handle any unexpected error in your
Python programs and to add debugging capabilities in them −
     Exception Handling − This would be covered in this tutorial. Here is a list of
        standard Exceptions available in Python: Standard Exceptions.
     Assertions − This would be covered in Assertions in Python tutorial.'''

'''Assertions in Python
An assertion is a sanity-check that you can turn on or turn off when you are done with
your testing of the program.

The easiest way to think of an assertion is to liken it to a raise-if statement (or to be more
accurate, a raise-if-not statement). An expression is tested, and if the result comes up
false, an exception is raised.

Assertions are carried out by the assert statement, the newest keyword to
Python, introduced in version 1.5.

Programmers often place assertions at the start of a function to check for valid input, and
after a function call to check for valid output.'''

''' The assert Statement
When it encounters an assert statement, Python evaluates the accompanying expression,
which is hopefully true. If the expression is false, Python raises an AssertionError
exception.

The syntax for assert is −
    assert Expression[, Arguments]

If the assertion fails, Python uses ArgumentExpression as the argument for the
AssertionError. AssertionError exceptions can be caught and handled like any other
exception using the try-except statement, but if not handled, they will terminate the
program and produce a trace back.

Example
Here is a function that converts a temperature from degrees Kelvin to degrees Fahrenheit.
Since zero degrees Kelvin is as cold as it gets, the function bails out if it sees a negative
temperature'''

def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32
print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))

''' What is Exception?
An exception is an event, which occurs during the execution of a program and disrupts the
normal flow of the program's instructions.
An exception is a Python object that represents an error.

When a Python script raises an exception, it must either handle the exception immediately
otherwise it terminates and quits.'''

''' Handling an Exception in Python
If you have some suspicious code that may raise an exception, you can defend your
program by placing the suspicious code in a try: block. After the try: block, include an
except: statement, followed by a block of code which handles the problem as elegantly as
possible
     The try: block contains statements which are susceptible for exception
     If exception occurs, the program jumps to the except: block.
     If no exception in the try: block, the except: block is skipped.
Syntax
Here is the simple syntax of try...except...else blocks −
--------------------------------
try:
    You do your operations here
    ...
except ExceptionI:
    If there is ExceptionI, then execute this block.
except ExceptionII:
    If there is ExceptionII, then execute this block.
    ...
else:
    If there is no exception then execute this block.'''

''' Here are few important points about the above-mentioned syntax −
     A single try statement can have multiple except statements. This is useful when
        the try block contains statements that may throw different types of exceptions.
     You can also provide a generic except clause, which handles any exception.
     After the except clause(s), you can include an else clause. The code in the else
        block executes if the code in the try: block does not raise an exception.
     The else block is a good place for code that does not need the try: block's
        protection.
Example
This example opens a file, writes content in the file and comes out gracefully because there
is no problem at all'''
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
else:
    print ("Written content in the file successfully")
    fh.close()

''' However, change the mode parameter in open() function to "w". If the testfile is not
already present, the program encounters IOError in except block, and prints following

Example
This example tries to open a file where you do not have write permission, so it raises an
exception'''
try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
else:
    print ("Written content in the file successfully")

''' The except Clause with No Exceptions
You can also use the except statement with no exceptions defined as follows −
-------------------------------------
try:
    You do your operations here;
    ....
except:
    If there is any exception, then execute this block.
    ....
else:
    If there is no exception then execute this block.
-------------------------------------
This kind of a try-except statement catches all the exceptions that occur. Using this kind
of try-except statement is not considered a good programming practice though, because
it catches all exceptions but does not make the programmer identify the root cause of the
problem that may occur.'''

''' The except Clause with Multiple Exceptions
You can also use the same except statement to handle multiple exceptions as follows −
-------------------------------------
try:
    You do your operations here;
    ....
except(Exception1[, Exception2[,...ExceptionN]]]):
    If there is any exception from the given exception list,
    then execute this block.
    ....
else:
    If there is no exception then execute this block.
-------------------------------------'''

''' The try-finally Clause
You can use a finally: block along with a try: block. The code in the finally block executes,
whether the try-block raised an exception or not. The syntax of the try-finally statement
is this
-------------------------------------
try:
    You do your operations here;
    ....
    Due to any exception, this may be skipped.
finally:
    This would always be executed.
    ....
-------------------------------------    
You cannot use else clause as well along with a finally clause.
Example:-'''
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print ("Error: can\'t find file or read data")

''' If you do not have permission to open the file in writing mode, then will produce the
following result −
>> Error: can't find file or read data
Same example can be written more cleanly as follows'''
try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print ("Going to close the file")
        fh.close()
except IOError:
    print ("Error: can\'t find file or read data")

''' When an exception is thrown in the try block, the execution immediately passes to the
finally block. After all the statements in the finally block are executed, the exception is
raised again and is handled in the except statements if present in the next higher layer of
the try-except statement.'''

'''Argument of an Exception
An exception can have an argument, which is a value that gives additional information
about the problem. The contents of the argument vary by exception. You capture an
exception's argument by supplying a variable in the except clause as follows
-------------------------------------
try:
    You do your operations here;
    ....
except ExceptionType, Argument:
    You can print value of Argument here...

If you write the code to handle a single exception, you can have a variable that follows
the name of the exception in the except statement. If you are trapping multiple exceptions,
you can have a variable that follows the tuple of the exception.

This variable receives the value of the exception mostly containing the cause of the
exception. The variable can receive a single value or multiple values in the form of a tuple.
This tuple usually contains the error string, the error number, and an error location.

Example
Following is an example for a single exception'''
# Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")

''' Raising Exceptions
You can raise exceptions in several ways by using the raise statement. The general syntax
for the raise statement is as follows.
Syntax:- raise [Exception [, args [, traceback]]]

Here, Exception is the type of exception (for example, NameError) and argument is a value
for the exception argument. The argument is optional; if not supplied, the exception
argument is None.

The final argument, trace back, is also optional (and rarely used in practice), and if
present, is the traceback object used for the exception.

Example:- 
An exception can be a string, a class or an object. Most of the exceptions that the Python
core raises are classes, with an argument that is an instance of the class. Defining new
exceptions is quite easy and can be done as follows'''
def functionName( level ):
    if level < 1:
        raise ("Invalid level!", level)
# The code below to this would not be executed
# if we raise the exception
''' Note: In order to catch an exception, an "except" clause must refer to the same exception
thrown either as a class object or simple string. For example, to capture above exception,
we must write the except clause as follows
---------------------------------
try:
    Business Logic here...
except "Invalid level!":
    Exception handling here...
else:
    Rest of the code here...
---------------------------------
'''

''' User-Defined Exceptions
Python also allows you to create your own exceptions by deriving classes from the standard
built-in exceptions.

Here is an example related to RuntimeError. Here, a class is created that is subclassed
from RuntimeError. This is useful when you need to display more specific information when
an exception is caught.

In the try block, the user-defined exception is raised and caught in the except block. The
variable e is used to create an instance of the class Networkerror.
------------
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
-----------
So once you defined above class, you can raise the exception as follows −
------------
try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print (e.args)
------------'''

''' Standard Exceptions
Here is a list of Standard Exceptions available in Python

Sr.No.  Exception Name            Description
------  ------------------------- --------------------------------------------------
1       Exception                 Base class for all exceptions
2       StopIteration             Raised when the next() method of an iterator does not point to any object
3       SystemExit                Raised by the sys.exit() function
4       StandardError             Base class for all built-in exceptions except StopIteration and SystemExit
5       ArithmeticError           Base class for all errors that occur for numeric calculation
6       OverflowError             Raised when a calculation exceeds maximum limit for a numeric type
7       FloatingPointError        Raised when a floating point calculation fails
8       ZeroDivisionError         Raised when division or modulo by zero takes place for all numeric types
9       AssertionError            Raised in case of failure of the Assert statement
10      AttributeError            Raised in case of failure of attribute reference or assignment
11      EOFError                  Raised when there is no input from either the raw_input() or input() function and the end of file is reached
12      ImportError               Raised when an import statement fails
13      KeyboardInterrupt         Raised when the user interrupts program execution, usually by pressing Ctrl+c
14      LookupError               Base class for all lookup errors
15      IndexError                Raised when an index is not found in a sequence
16      KeyError                  Raised when the specified key is not found in the dictionary
17      NameError                 Raised when an identifier is not found in the local or global namespace
18      UnboundLocalError         Raised when trying to access a local variable in a function or method but no value has been assigned to it
19      EnvironmentError          Base class for all exceptions that occur outside the Python environment
20      IOError                   Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist
21      OSError                   Raised for operating system-related errors
22      SyntaxError               Raised when there is an error in Python syntax
23      IndentationError          Raised when indentation is not specified properly
24      SystemError               Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit
25      SystemExit                Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit
26      TypeError                 Raised when an operation or function is attempted that is invalid for the specified data type
27      ValueError                Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified
28      RuntimeError              Raised when a generated error does not fall into any category
29      NotImplementedError       Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented
'''


'''------------------------------------- Python - The try-except Block -------------------------------
Python Try-Except Block
In Python, the try-except block is used to handle exceptions and errors gracefully, ensuring
that your program can continue running even when something goes wrong. This tutorial
will cover the basics of using the try-except block, its syntax, and best practices.

Exception handling allows you to manage errors in your code by capturing
exceptions and taking appropriate actions instead of letting the program crash.
An exception is an error that occurs during the execution of a program, and
handling these exceptions ensures your program can respond to unexpected
situations.

Syntax
Following is the basic syntax of the try-except block in Python −
-----------------
try:
    # Code that might cause an exception
    risky_code()
except SomeException as e:
    # Code that runs if an exception occurs
    handle_exception(e)
-----------------
Example:- 
In this example, if you enter a non-numeric value, a ValueError will be raised. If you enter
zero, a ZeroDivisionError will be raised. The except blocks handle these exceptions and
prints appropriate error messages'''
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
except ValueError as e:
    print("Error: Invalid input. Please enter a valid number.")

''' Handling Multiple Exceptions
In Python, you can handle multiple exceptions using multiple except blocks within a single
try-except statement. This allows your code to respond differently to different types of
errors that may occur during execution.
Syntax
Following is the basic syntax for handling multiple exceptions in Python'''
try:
    # Code that might raise exceptions
    risky_code()
except FirstExceptionType:
    # Handle the first type of exception
    handle_first_exception()
except SecondExceptionType:
    # Handle the second type of exception
    handle_second_exception()
# Add more except blocks as needed for other exception types

''' Example:- 
In the following example −
     If you enter zero as the divisor, a "ZeroDivisionError" will be raised, and the
        corresponding except ZeroDivisionError block will handle it by printing an error
        message.
     If you enter a non-numeric input for either the dividend or the divisor, a
        "ValueError" will be raised, and the except ValueError block will handle it by printing
        a different error message.'''
try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    result = dividend / divisor
    print(f"Result of division: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")

'''Using Else Clause with Try-Except Block
In Python, the else clause can be used in conjunction with the try-except block to specify
code that should run only if no exceptions occur in the try block. This provides a way to differentiate between the main code that may raise exceptions and additional code that
should only execute under normal conditions.
Syntax
Following is the basic syntax of the else clause in Python
---------------------
try:
    # Code that might raise exceptions
    risky_code()
except SomeExceptionType:
    # Handle the exception
    handle_exception()
else:
    # Code that runs if no exceptions occurred
    no_exceptions_code()
---------------------
Example:- '''
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"Result of division: {result}")

''' The Finally Clause
The finally clause provides a mechanism to guarantee that specific code will be executed,
regardless of whether an exception is raised or not. This is useful for performing cleanup
actions such as closing files or network connections, releasing locks, or freeing up
resources.
Example
In this example −
     If the file "example.txt" exists, its content is read and printed, and the else block
        confirms the successful operation.
     If the file is not found (FileNotFoundError), an appropriate error message is printed
        in the except block.
     The finally block ensures that the file is closed (file.close()) regardless of whether
        the file operation succeeds or an exception occurs.'''

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
else:
    print("File read operation successful.")
finally:
    if 'file' in locals():
        file.close()
    print("File operation is complete.")

'''----------------------------- Python - The try-finally Block ---------------------
Python Try-Finally Block
In Python, the try-finally block is used to ensure that certain code executes, regardless of
whether an exception is raised or not. Unlike the try-except block, which handles
exceptions, the try-finally block focuses on cleanup operations that must occur, ensuring
resources are properly released and critical tasks are completed.
Syntax
The syntax of the try-finally statement is as follows
--------------------
try:
    # Code that might raise exceptions
    risky_code()
finally:
    # Code that always runs, regardless of exceptions
    cleanup_code()
------------------'''

''' In Python, when using exception handling with try blocks, you have the option
to include either except clauses to catch specific exceptions or a finally
clause to ensure certain cleanup operations are executed, but not both
together.

Example
Let us consider an example where we want to open a file in write mode ("w"), writes some
content to it, and ensures the file is closed regardless of success or failure using a finally
block'''
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print ("Error: can\'t find file or read data")
    fh.close()

'''------------------------------- Python - Raising Exceptions ---------------------
Raising Exceptions in Python
In Python, you can raise exceptions explicitly using the raise statement. Raising exceptions
allows you to indicate that an error has occurred and to control the flow of your program
by handling these exceptions appropriately

In Python, you can raise built-in exceptions like ValueError or TypeError to indicate
common error conditions. Additionally, you can create and raise custom exceptions.'''

''' Raising Built-in Exceptions
You can raise any built-in exception by creating an instance of the exception class and
using the raise statement. 
Syntax:- raise Exception("This is a general exception")

Example:- 
Here is an example where we raise a ValueError when a function receives an invalid
argumen'''
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
try:
    result = divide(10, 0)
except ValueError as e:
    print(e)

''' Raising Custom Exceptions
In addition to built-in exceptions, you can define and raise your own custom exceptions
by creating a new exception class that inherits from the base Exception class or any of its
subclasses'''
class MyCustomError(Exception):
    pass
def risky_function():
    raise MyCustomError("Something went wrong in risky_function")
try:
    risky_function()
except MyCustomError as e:
    print(e)

''' Creating Custom Exceptions
Custom exceptions is useful for handling specific error conditions that are unique to your
application, providing more precise error reporting and control.

To create a custom exception in Python, you define a new class that inherits from the
built-in Exception class or any other appropriate built-in exception class. This custom
exception class can have additional attributes and methods to provide more detailed
context about the error condition.
Example
In this example −
     We define a custom exception class "InvalidAgeError" that inherits from
        "Exception".
     The __init__() method initializes the exception with the invalid age and a default
        error message.
     The set_age() function raises "InvalidAgeError" if the provided age is outside the
        valid range'''
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 18 and 100"):
        self.age = age
        self.message = message
        super().__init__(self.message)
def set_age(age):
    if age < 18 or age > 100:
        raise InvalidAgeError(age)
    print(f"Age is set to {age}")
try:
    set_age(150)
except InvalidAgeError as e:
    print(f"Invalid age: {e.age}. {e.message}")

''' Re-Raising Exceptions
Sometimes, you may need to catch an exception, perform specific actions (such as logging,
cleanup, or providing additional context), and then re-raise the same exception to be
handled further up the call stack

This is useful when you want to ensure certain actions are taken when an exception occurs,
but still allow the exception to propagate for higher-level handling.

To re-raise an exception in Python, you use the "raise" statement without specifying an
exception, which will re-raise the last exception that was active in the current scope.

Example
In the following example −
     The process_file() function attempts to open and read a file.
     If the file is not found, it prints an error message and re-raises the
        "FileNotFoundError" exception.
     The exception is then caught and handled at a higher level in the call stack.'''
def process_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            # Process data
    except FileNotFoundError as e:
        print(f"File not found: {filename}")
        # Re-raise the exception
        raise
try:
    process_file("nonexistentfile.txt")
except FileNotFoundError as e:
    print("Handling the exception at a higher level")