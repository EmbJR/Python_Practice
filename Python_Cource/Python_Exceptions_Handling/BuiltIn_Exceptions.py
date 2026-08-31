'''----------------------------- Python - Built-in Exceptions ---------------------------
Built-in exceptions are pre-defined error classes in Python that handle errors and
exceptional conditions in programs. They are derived from the base class "BaseException"
and are part of the standard library.

Standard Built-in Exceptions in Python
Here is a list of Standard Exceptions available in Python −

Sr.No.    Exception Name           Description
1         Exception                Base class for all exceptions
2         StopIteration            Raised when the next() method of an iterator does not point to any object
3         SystemExit               Raised by the sys.exit() function
4         StandardError            Base class for all built-in exceptions except StopIteration and SystemExit
5         ArithmeticError          Base class for all errors that occur for numeric calculation
6         OverflowError            Raised when a calculation exceeds maximum limit for a numeric type
7         FloatingPointError       Raised when a floating point calculation fails
8         ZeroDivisionError        Raised when division or modulo by zero takes place for all numeric types
9         AssertionError           Raised in case of failure of the Assert statement
10        AttributeError           Raised in case of failure of attribute reference or assignment
11        EOFError                 Raised when there is no input from either the raw_input() or input() function and the end of file is reached
12        ImportError              Raised when an import statement fails
13        KeyboardInterrupt        Raised when the user interrupts program execution, usually by pressing Ctrl+C
14        LookupError              Base class for all lookup errors
15        IndexError               Raised when an index is not found in a sequence
16        KeyError                 Raised when the specified key is not found in the dictionary
17        NameError                Raised when an identifier is not found in the local or global namespace
18        UnboundLocalError        Raised when trying to access a local variable in a function or method but no value has been assigned to it
19        EnvironmentError         Base class for all exceptions that occur outside the Python environment
20        IOError                  Raised when an input/output operation fails, such as the print statement or the open() function when trying to open a file that does not exist
21        OSError                  Raised for operating system-related errors
22        SyntaxError              Raised when there is an error in Python syntax
23        IndentationError         Raised when indentation is not specified properly
24        SystemError              Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit
25        SystemExit               Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit
26        TypeError                Raised when an operation or function is attempted that is invalid for the specified data type
27        ValueError               Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified
28        RuntimeError             Raised when a generated error does not fall into any category
29        NotImplementedError      Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented
'''
# 1. Exception
# Base class for all exceptions.
try:
    raise Exception("This is a generic exception")
except Exception as e:
    print(f"Caught Exception: {e}")

# 2. StopIteration
# Raised by the next() method of an iterator to signal that there are no further items.
my_iter = iter([1, 2])
print(next(my_iter))
print(next(my_iter))
try:
    print(next(my_iter))
except StopIteration:
    print("Caught StopIteration: No more items")

# 3. SystemExit
# Raised by the sys.exit() function.
import sys
try:
    sys.exit("Exiting the program")
except SystemExit as e:
    print(f"Caught SystemExit: {e}")

# 4. StandardError
# Python 3 Note: StandardError does not exist in Python 3. 
# It was the base class for all built-in exceptions except StopIteration, SystemExit, and Warning.
# In Python 3, Exception serves this purpose.
# Example using Exception (Python 3 equivalent):
try:
    # This raises a TypeError, which inherits from Exception (formerly StandardError in Py2)
    "2" + 2
except Exception as e:
    print(f"Caught Exception (StandardError equivalent): {e}")

# 5. ArithmeticError
# Base class for errors raised for numeric calculations (OverflowError, ZeroDivisionError, FloatingPointError).
try:
    # This raises a ZeroDivisionError, which inherits from ArithmeticError
    x = 10 / 0
except ArithmeticError as e:
    print(f"Caught ArithmeticError: {e}")

# 6. OverflowError
# Raised when the result of an arithmetic operation is too large to be represented.
# Note: In standard Python, integers have arbitrary precision, so this usually happens with floats.
try:
    import math
    print(math.exp(1000))
except OverflowError as e:
    print(f"Caught OverflowError: {e}")

# 7. FloatingPointError
# Raised when a floating point calculation fails.
# Requires the 'fpectl' module or specific hardware conditions, rarely seen in standard usage.
# We can simulate it or explain it's rare.
# However, division by zero for floats raises ZeroDivisionError in Python, not FloatingPointError typically.
# For demonstration purposes, we acknowledge it exists but is hard to trigger without specific flags.
print("FloatingPointError is rarely raised in standard Python without specific fpectl settings.")

# 8. ZeroDivisionError
# Raised when division or modulo by zero takes place.
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}")

# 9. AssertionError
# Raised when an assert statement fails.
try:
    x = 10
    assert x > 20, "x is not greater than 20"
except AssertionError as e:
    print(f"Caught AssertionError: {e}")

# 10. AttributeError
# Raised when an attribute reference or assignment fails.
try:
    x = 10
    x.append(5)
except AttributeError as e:
    print(f"Caught AttributeError: {e}")

# 11. EOFError
# Raised when input() hits an end-of-file condition (EOF).
# To simulate this without actual user input, we can mock it or use a string stream.
import io
import sys
sys.stdin = io.StringIO("") # Simulate immediate EOF
try:
    data = input("Enter something: ")
except EOFError:
    print("Caught EOFError: No input detected (End of File)")
finally:
    sys.stdin = sys.__stdin__ # Reset stdin

# 12. ImportError
# Raised when an import statement fails.
try:
    import nonexistent_module
except ImportError as e:
    print(f"Caught ImportError: {e}")

# 13. KeyboardInterrupt
# Raised when the user interrupts program execution (e.g., pressing Ctrl+C).
# Note: This cannot be easily demonstrated in a script block as it requires external interaction.
# The code structure to catch it looks like this:
try:
    # In a real terminal, you would press Ctrl+C here
    pass 
except KeyboardInterrupt:
    print("Caught KeyboardInterrupt: Program interrupted by user")

# 14. LookupError
# Base class for IndexError and KeyError.
try:
    # This raises an IndexError, which inherits from LookupError
    my_list = [1, 2, 3]
    print(my_list[5])
except LookupError as e:
    print(f"Caught LookupError: {e}")

# 15. IndexError
# Raised when an index is not found in a sequence.
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"Caught IndexError: {e}")

# 16. KeyError
# Raised when a key is not found in a dictionary.
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"Caught KeyError: {e}")

# 17. NameError
# Raised when a local or global name is not found.
try:
    print(undefined_variable)
except NameError as e:
    print(f"Caught NameError: {e}")

# 18. UnboundLocalError
# Raised when a reference is made to a local variable that has not been assigned a value.
def test_function():
    try:
        print(x) # Python treats x as local because of the assignment later
        x = 10
    except UnboundLocalError as e:
        print(f"Caught UnboundLocalError: {e}")

test_function()

# 19. EnvironmentError
# Python 3 Note: EnvironmentError is an alias for OSError in Python 3.
# It is the base class for errors that occur outside the Python environment (I/O, OS errors).
try:
    # This raises FileNotFoundError (subclass of OSError/EnvironmentError)
    f = open("nonexistent_file.txt", "r")
except EnvironmentError as e:
    print(f"Caught EnvironmentError (OSError): {e}")

# 20. IOError
# Python 3 Note: In Python 3, IOError is merged into OSError.
# It is an alias for OSError.
try:
    f = open("nonexistent_file.txt", "r")
except IOError as e:
    print(f"Caught IOError: {e}")

# 21. OSError
# Raised for operating system-related errors (e.g., file not found, permission denied).
try:
    f = open("/root/nonexistent_file.txt", "r")
except OSError as e:
    print(f"Caught OSError: {e}")

# 22. SyntaxError
# Raised when there is an error in Python syntax.
# This is usually caught by the parser before execution, so we use exec() to trigger it dynamically.
try:
    exec("print 'Hello World'") # Invalid syntax in Python 3
except SyntaxError as e:
    print(f"Caught SyntaxError: {e}")

# 23. IndentationError
# Raised when indentation is not specified properly (subclass of SyntaxError).
try:
    exec("if True:\nprint('Indented incorrectly')")
except IndentationError as e:
    print(f"Caught IndentationError: {e}")

# 24. SystemError
# Raised when the interpreter finds an internal problem.
# This is very rare and usually indicates a bug in the Python interpreter itself.
# It is difficult to reproduce reliably in a script.
print("SystemError is rare and indicates an internal interpreter issue.")

# 25. SystemExit (Duplicate of 3)
# See example #3.

# 26. TypeError
# Raised when an operation or function is applied to an object of inappropriate type.
try:
    x = "10" + 5
except TypeError as e:
    print(f"Caught TypeError: {e}")

# 27. ValueError
# Raised when a function gets an argument of correct type but inappropriate value.
try:
    x = int("abc")
except ValueError as e:
    print(f"Caught ValueError: {e}")

# 28. RuntimeError
# Raised when an error does not fall into any specific category.
try:
    # In older Python versions, recursion limits raised this directly or as a specific RecursionError
    # RecursionError is a subclass of RuntimeError introduced in Python 3.5
    def recurse():
        recurse()
    recurse()
except RuntimeError as e:
    print(f"Caught RuntimeError: {e}")

# 29. NotImplementedError
# Raised when an abstract method that needs to be implemented in an inherited class is not implemented.
class BaseClass:
    def do_something(self):
        raise NotImplementedError("Subclasses must implement this method")

class SubClass(BaseClass):
    pass

try:
    obj = SubClass()
    obj.do_something()
except NotImplementedError as e:
    print(f"Caught NotImplementedError: {e}")


''' -------------------------- Hierarchy of Built-in Exceptions ---------------
The exceptions in Python are organized in a hierarchical structure, with "BaseException"
at the top. Here is a simplified hierarchy −

 BaseException
    o SystemExit
    o KeyboardInterrupt
 Exception
    o ArithmeticError
         FloatingPointError
         OverflowError
         ZeroDivisionError
 AttributeError
 EOFError
 ImportError
 LookupError
    o IndexError
    o KeyError
 MemoryError
 NameError
    o UnboundLocalError
 OSError
    o FileNotFoundError
 TypeError
 ValueError
 ---(Many others)---'''

''' How to Use Built-in Exceptions
As we already know that built-in exceptions in Python are pre-defined classes that handle
specific error conditions. Now, here is a detailed guide on how to use them effectively in
your Python programs −
Handling Exceptions with try-except Blocks
The primary way to handle exceptions in Python is using "try-except" blocks. This allows
you to catch and respond to exceptions that may occur during the execution of your code.
Example
In the following example, the code that may raise an exception is placed inside the "try"
block. The "except" block catches the specified exception "ZeroDivisionError" and handles
it'''
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")

''' Handling Multiple Exceptions
You can handle multiple exceptions by specifying them in a tuple within the "except" block
as shown in the example below'''
try:
    result = int('abc')
except (ValueError, TypeError) as e:
    print(f"Caught a ValueError or TypeError: {e}")

''' Using "else" and "finally" Blocks
The "else" block is executed if the code block in the "try" clause does not raise an exception'''
try:
    number = int(input("Enter a number: "))
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    print(f"You entered: {number}")

'''The "finally" block is always executed, regardless of whether an exception occurred or not.
It's typically used for clean-up actions, such as closing files or releasing resources'''
try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
finally:
    file.close()
    print("File closed.")

''' Explicitly Raising Built-in Exceptions
In Python, you can raise built-in exceptions to indicate errors or exceptional conditions in
your code. This allows you to handle specific error scenarios and provide informative error
messages to users or developers debugging your application.

Syntax:- raise ExceptionClassName("Error message")

Example
In this example, the "divide" function attempts to divide two numbers "a" and "b". If "b"
is zero, it raises a "ZeroDivisionError" with a custom message'''

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")