
'''Python's standard library comes bundled with a large number of modules. They are called
built-in modules. Most of these built-in modules are written in C (as the reference
implementation of Python is in C), and pre-compiled into the library. These modules come
with useful functionality like system-specific OS management, disk IO, networking, etc.'''

''' Here is a select list of built-in modules −
Sr.No.      Name & Brief Description
1           "os"
            This module provides a unified interface to a
            number of operating system functions.
2           "string"
            This module contains a number of functions
            for string processing
3           "re"  
            This module provides a set of powerful
            regular expression facilities. Regular
            expression (RegEx), allows powerful string
            search and matching for a pattern in a string
4           "math"
            This module implements a number of mathematical operations for floating point numbers. These functions are generally thin
            wrappers around the platform C library functions.
5           "cmath"
            This module contains a number of mathematical operations for complex
            numbers.
6           "datetime"
            This module provides functions to deal with dates and the time within a day. It wraps the
            C runtime library.
7           "gc"
            This module provides an interface to the built-in garbage collector.
8           "asyncio"
            This module defines functionality required for asynchronous processing
9           "collections"
            This module provides advanced Container datatypes.
10          "functools"
            This module has Higher-order functions and operations on callable objects. Useful in
            functional programming
11          "operator"
            Functions corresponding to the standard operators.
12          "pickle"
            Convert Python objects to streams of bytes and back.
13          "socket"
            Low-level networking interface.
14          "sqlite3"
            A DB-API 2.0 implementation using SQLite 3.x.
15          "statistics"
            Mathematical statistics functions
16          "typing"
            Support for type hints
17          "venv"
            Creation of virtual environments.
18          "json"
            Encode and decode the JSON format.
19          "wsgiref"
            WSGI Utilities and Reference Implementation.
20          "unittest"
            Unit testing framework for Python.
21          "random"
            Generate pseudo-random numbers
22          "sys"
            Provides functions that acts strongly with the interpreter.
23          "requests"
            It simplifies HTTP requests by offering a user-friendly interface for sending and
            handling responses. Provides functions that acts strongly with the interpreter.
23          "requests"
            It simplifies HTTP requests by offering a user-friendly interface for sending and
            handling responses.
'''
import mymodule
mymodule.SayHello("Alice")

print(dir(mymodule))

print ("sum:",mymodule.sum(10,20))
print ("average:",mymodule.average(10,20))
print ("power:",mymodule.power(10, 2))

'''------------------ The from ... import Statement ------------------
The import statement will load all the resources of the module in the current namespace.
It is possible to import specific objects from a module by using this syntax. 

For example−
Out of three functions in mymodule, only two are imported in following executable script
example.py'''

from mymodule import sum, average

print ("sum:",sum(10,20))

'''--------------------------- The from...import * Statement ---------------------------
It is also possible to import all the names from a module into the current namespace by
using the following import statement
Example:-
from modname import *
'''

'''----------- The import ... as Statement -------------------
You can assign an alias name to the imported module
Example:-
from modulename as alias
'''

'''-------------------- Locating Modules --------------------
When you import a module, the Python interpreter searches for the module in the following
sequences −
     The current directory.
     If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.
     If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.
The module search path is stored in the system module sys as the sys.path variable. The
sys.path variable contains the current directory, PYTHONPATH, and the installation-
dependent default'''

'''-------------------- Module Attributes --------------------
In Python, a module is an object of module class, and hence it is characterized by
attributes.
Following are the module attributes −
     __file__ returns the physical name of the module.
     __package__ returns the package to which the module belongs.
     __doc__ returns the docstring at the top of the module if any.
     __dict__ returns the entire scope of the module
     __name__ returns the name of the module
Example:-
'''
print ("__file__ attribute:", mymodule.__file__)
print ("__doc__ attribute:", mymodule.__doc__)
print ("__name__ attribute:", mymodule.__name__)

'''-------------------- The dir( ) Function --------------------
The dir() built-in function returns a sorted list of strings containing the names defined by
a module.
The list contains the names of all the modules, variables and functions that are defined in
a module. Following is a simple example'''
# Import built-in module math
import math
content = dir(math)
print (content)

'''------------------ The reload() Function ------------------
Sometimes you may need to reload a module, especially when working with the interactive
interpreter session of Python.
We can import the module and call its function from Python prompt as follows −
"mymodule.sum(10,20)"
However, suppose you need to modify the sum() function. Even if you edit the test.py file and save it, the function loaded in the memory won't
update. You need to reload it, using reload() function in imp module as shown below −
Example:-
'''
import importlib
mymodule = importlib.reload(mymodule)
print(mymodule.sum(10,20))

'''------------------ Packages in Python ------------------
A package is a hierarchical file directory structure that defines a single Python application
environment that consists of modules, subpackages and, sub-subpackages, and so on.
Consider a file Pots.py available in Phone directory. This file has following line of source
code −
    def Pots():
    print "I'm Pots Phone"
Similar way, we have another two files having different functions with the same name as
above −
     Phone/Isdn.py file having function Isdn()
     Phone/G3.py file having function G3()
Now, create one more file __init__.py in Phone directory −
     Phone/__init__.py
To make all of your functions available when you've imported Phone, you need to put
explicit import statements in __init__.py as follows −
    from Pots import Pots
    from Isdn import Isdn
    from G3 import G3
After you add these lines to __init__.py, you have all of these classes available when you
import the Phone package.
Example:-
# Now import your Phone Package.
import Phone

Phone.Pots()
Phone.Isdn()
Phone.G3()
'''