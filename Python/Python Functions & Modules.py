
#---------------- Python Function --------------
'''
Syntax to Define a Python Function

def function_name( parameters ):
    "function_docstring"
    function_suite
    return [expression]
'''

'''
Pass by Reference vs Value
In programming languages like C and C++, there are two main ways to pass variables to
a function, which are Call by Value and Call by Reference (also known as pass by reference
and pass by value). However, the way we pass variables to functions in Python differs
from others.
     call by value − When a variable is passed to a function while calling, the value of
    actual arguments is copied to the variables representing the formal arguments.
    Thus, any changes in formal arguments does not get reflected in the actual
    argument. This way of passing variable is known as call by value.
     call by reference − In this way of passing variable, a reference to the object in
    memory is passed. Both the formal arguments and the actual arguments (variables
    in the calling code) refer to the same object. Hence, any changes in formal
    arguments does get reflected in the actual argument.

Python uses pass by reference mechanism. As variable in Python is a label or reference to
the object in the memory, both the variables used as actual argument as well as formal
arguments really refer to the same object in the memory. We can verify this fact by
checking the id() of the passed variable before and after passing.
Example
In the following example, we are checking the id() of a variable.
'''
def testfunction(arg):
    print ("ID inside the function:", id(arg))
var = "Hello"
print ("ID before passing:", id(var))
testfunction(var)
'''
The behavior also depends on whether the passed object is mutable or immutable. Python
numeric object is immutable. When a numeric object is passed, and the function changes
the value of the formal argument, it actually creates a new object in the memory, leaving
the original variable unchanged
Example
'''
print("\nExample with immutable object:--------------")
def testfunction(arg):
    print ("ID inside the function:", id(arg))
    arg = arg + 1
    print ("new object after increment", arg, id(arg))
var=10
print ("ID before passing:", id(var))
testfunction(var)
print ("value after function call", var)

'''
Let us now pass a mutable object (such as a list or dictionary) to a function. It is also
passed by reference, as the id() of list before and after passing is same. However, if we
modify the list inside the function, its global representation also reflects the change.
Example
Here we pass a list, append a new item, and see the contents of original list object, which
we will find has changed
'''
print("\nExample with mutable object:--------------")
def testfunction(arg):
    print ("Inside function:",arg)
    print ("ID inside the function:", id(arg))
    arg=arg.append(100)

var=[10, 20, 30, 40]
print ("ID before passing:", id(var))
testfunction(var)
print ("list after function call", var)

#---------------- Types of Python Function Arguments
'''
Based on how the arguments are declared while defining a Python function, they are
classified into the following categories −
     Positional or Required Arguments
     Keyword Arguments
     Default Arguments
     Positional-only Arguments
     Keyword-only arguments
     Arbitrary or Variable-length Arguments
'''

'''------------------------ Positional or Required Arguments ------------------------
Required arguments are the ones passed to a function in correct positional order. Here,
the number of arguments in the function call should match exactly with the function
definition, otherwise the code gives a syntax error.
Example
In the code below, we call the function printme() without any parameters which will give
error.
'''
# Function definition is here
def printme( str ):
    "This prints a passed string into this function"
    print (str)
    return;
# Now you can call printme function
# printme() # This will give error
printme("Hello World!")

'''------------------------ Keyword Arguments ------------------------
Keyword arguments are related to the function calls. When we use keyword arguments in a
function call, the caller identifies the arguments by the parameter name. This allows us to
'''
# Function definition is here
def printinfo( name, age ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return;
# Now you can call printinfo function
printinfo( age=50, name="miki" )

''' Unlike positional arguments, the order of keyword arguments does not matter. However, 
the positional arguments must be before the keyword arguments while using
mixed calling.
Example:-'''
def division(num, den):
    quotient = num/den
    print ("num:{} den:{} quotient:{}".format(num, den, quotient))
# division(num = 5, 10) this statement will raise the error
division(10, den = 5)   # This is the correct way

'''------------------------ Default Arguments ------------------------
A default argument is an argument that assumes a default value if a value is not
provided in the function call for that argument.
Example'''
# Function definition is here
def printinfo( name, age = 35 ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return;
# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )

'''------------------------ Positional-only arguments ------------------------
Those arguments that can only be specified by their position in the function call is called
as Positional-only arguments. They are defined by placing a "/" in the function's parameter
list after all positional-only parameters. This feature was introduced with the release of
Python 3.8.
'''
def posFun(x, y, /, z):
    print(x + y + z)
print("Evaluating positional-only arguments: ")
#postFun(x=33, y=22, z=11) # This will raise the error
posFun(33, 22, z=11)

'''------------------------ Keyword-only arguments ------------------------
Those arguments that must be specified by their name while calling the function is known
as Keyword-only arguments. They are defined by placing an asterisk ("*") in the function's
parameter list before any keyword-only parameters. This type of argument can only be
passed to a function as a keyword argument, not a positional argument.

Example:- 
In the code below, we have defined a function with three keyword-only arguments. To call
this method, we need to pass keyword arguments, otherwise, we will encounter an error.
'''

def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)
print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5)

''' The built-in print() function is an example of keyword-only arguments. You can give list of
expressions to be printed in the parentheses. The printed values are separated by a white
space by default. You can specify any other separation character instead using "sep"
argument
Example:- print ("Hello", "World", sep="-")'''


'''------------------------ Arbitrary or Variable-length Arguments
You may need to process a function for more arguments than you specified while defining
the function. These arguments are called variable-length arguments and are not named in
the function definition, unlike required and default arguments

Example:-
'''
# Function definition is here
def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return;
# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

'''
Arbitrary Keyword Arguments (**kwargs)
If a variable in the argument list has two asterisks prefixed to it, the function can accept
arbitrary number of keyword arguments. The variable becomes a dictionary of
keyword:value pairs.

Example:- 
The following code is an example of a function with arbitrary keyword arguments. The
addr() function has an argument **kwargs which is able to accept any number of address
elements like name, city, phno, pin, etc. Inside the function kwargs dictionary of kw:value
pairs is traversed using items() method
'''
print("########################################")
def addr(**kwargs):
    for k, v in kwargs.items():
        print ("{}:{}".format(k,v))

print("Two keyword arguments:")
addr(Name="Jaydeep", City="Ahmedabad")

print("Pass 4 keyword arguments:")
addr(Name="Ansh", City="Baroda", Phone="1234567890", Pin="390001")
print("########################################")
'''
Alternative to the above example
'''
print("########################################")

'''
below is the alternate example of how to pass the dictionary as keyword without using **
'''
def addr(kwargs):
    for k, v in kwargs.items():
        print ("{}:{}".format(k,v))

print("Two keyword arguments:")

dict = {"Name": "Jaydeep", "City": "Ahmedabad"}
addr(dict)

print("Pass 4 keyword arguments:")
addr({"Name": "Ansh", "City": "Baroda", "Phone": "1234567890", "Pin": "390001"})

print("########################################")

''' Another alternate example '''
def process(name, age):
    print ("{}:{}".format(name, age))

my_dict = {'name': 'John', 'age': 30}
process(**my_dict)  # Unpacks into keyword arguments'''

print("########################################")
#-----------------------------------------------------------------
'''
Order of Python Function Arguments
A function can have arguments of any of the types defined above. However, the arguments
must be declared in the following order −
     The argument list begins with the positional-only args, followed by the slash (/) symbol.
     It is followed by regular positional args that may or may not be called as keyword arguments.
     Then there may be one or more args with default values.
     Next, arbitrary positional arguments represented by a variable prefixed with single asterisk, that is treated as tuple. It is the next.
     If the function has any keyword-only arguments, put an asterisk before their names start. Some of the keyword-only arguments may have a default value.
     Last in the bracket is argument with two asterisks ** to accept arbitrary number of keyword arguments.
The following diagram shows the order of formal arguments
Example:- 
def function(pos_only1, pos_only2, /, pos_or_kwd, default_arg=5, *var_pos_args, kwd_only1, kwd_only2=10, **var_kwd_args):
    pass
'''


''' The Anonymous Functions
The functions are called anonymous when they are not declared in the standard manner
by using the def keyword. Instead, they are defined using the lambda keyword.
     Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.
     An anonymous function cannot be a direct call to print because lambda requires an expression
     Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.
     Although it appears that lambda is a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is by passing function
stack allocation during invocation for performance reasons.

Example:-
'''
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;
# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

'''------------------------ Deffault arguments -------------------------
Example of Default Arguments
The following example shows use of Python default arguments. Here, the second call to
the function will not pass value to "city" argument, hence its default value "Hyderabad"
will be used.'''
# Function definition
def showinfo( name, city = "Hyderabad" ):
    "This prints a passed info into this function"
    print ("Name:", name)
    print ("City:", city)
    return
# Now call showinfo function
showinfo(name = "Ansh", city = "Delhi")
showinfo(name = "Shrey")

'''------------------------ Mutable Objects as Default Argument -------------------------
Python evaluates default arguments once when the function is defined, not each time the
function is called. Therefore, if you use a mutable default argument and modify it within
the given function, the same values are referenced in the subsequent function calls

Example:-
'''
def fcn(nums, numericlist = []):
    numericlist.append(nums + 1)
    print(numericlist)
# function calls
fcn(66)
fcn(68)
fcn(70)


# General Example1:-
'''A function may be defined in such a way that it has some keyword-only and some
positional-only arguments. Here, x is a required positional-only argument, y is a regular
positional argument, and z is a keyword-only argument.
'''
def myfunction(x, /, y, *, z):
    print (x, y, z)
myfunction(10, y=20, z=30)
myfunction(10, 20, z=30)

# General Example 2 (Arbitrary Arguments):
def add(*arg):
    s = 0
    for x in arg:
        s += x
    return s
result = add(10, 20, 30)
print("Sum is:", result)
result = add(5, 15, 30, 45, 60)
print("Sum is:", result)

# General Example 3(Arbitrary and positional args):
'''
The following example has avg() function. Assume that a student can take any number of
tests. First test is mandatory. He can take as many tests as he likes to better his score.
The function calculates the average of marks in first test and his maximum score in the
rest of tests.

The function has two arguments, first is the required argument and second to hold any
number of values.
'''
def avg(firsttest, *resttest):
    avg = (firsttest + max(resttest)) / 2
    print("Average score is:", avg)
    return avg
result = avg(40,30,50,25)
print("Returned value is:", result)

#General Example 4:
'''
Imagine a case where science and maths are mandatory subjects, in addition to which
student may choose any number of elective subjects.
The following code defines a percent() function where marks in science and marks are
stored in required arguments, and the marks in variable number of elective subjects in
**optional argument.'''

def persent(maths, science, **optional):
    print("Maths", maths)
    print("Science", science)
    TotalMS = maths + science
    for k, v in optional.items():
        TotalMS += v
    return (TotalMS / 2 + len(optional))

result = persent(maths=90, science=80, Eng=70, Hist=60, Geo=75)
print("Percentage is:", result)

#--------------------- Function Annotations ----------------------
'''
The function annotation feature of Python enables you to add additional explanatory
metadata about the arguments declared in a function definition, and also the return data
types. They are not considered by Python interpreter while executing the function. Python
IDEs use them for providing a detailed documentation to the programmer.

Remember that Python is a dynamically typed language, and doesn't enforce any type
checking at runtime. Hence annotating the arguments with data types doesn't have any
effect while calling the function. Even if non-integer arguments are given, Python doesn't
detect any error

Example:-
'''

def myfunction(a: int, b: int):
    c = a+b
    return c
print (myfunction(10,20))
print (myfunction("Hello ", "Python"))

'''
Function Annotations with Return Type
Annotations are ignored at runtime, but are helpful for the IDEs and static type checker
libraries such as mypy.
You can give annotation for the return data type as well. After the parentheses and before
the colon symbol, put an arrow (->) followed by the annotation.

Example:-
In this example, we are providing annotation for return type
'''
def myfunction(a: int, b: int) -> int:
    c = a+b
    return c
print(myfunction(56,88))
print(myfunction.__annotations__)

'''---------------------- Function Annotations with Expression ----------------------
As using the data type as annotation is ignored at runtime, you can put any expression
which acts as the metadata for the arguments. Hence, function may have any arbitrary
expression as annotation
Example:-'''
def total(x : 'marks in Physics', y: 'marks in chemistry'):
    return x+y
print(total(86, 88))
print(total.__annotations__)

''' ---------------- Function Annotations with Default Arguments -----------------
If you want to specify a default argument along with the annotation, you need to put it
after the annotation expression.

Example 1:-
The following example demonstrates how to provide annotation for default arguments of
a function'''
def myfunction(a: "physics", b:"Maths" = 20) -> int:
    c = a+b
    return c
print (myfunction(10))
''' The function in Python is also an object, and one of its attributes is __annotations__. You
can check with dir() function'''
print (dir(myfunction))

''' You may have arbitrary positional and/or arbitrary keyword arguments for a function.
Annotations can be given for them also
Example 2:-
def myfunction(*args: "arbitrary args", **kwargs: "arbitrary keyword args") -> int:
    pass
print (myfunction.__annotations__)
'''

''' In case you need to provide more than one annotation expressions to a function argument,
give it in the form of a dictionary object in front of the argument itself
Example 3:-'''
def myfunction(a: {"type": "int", "range": "0-100"}, b: {"type": "int", "range": "0-100"} ) -> int:
    c = a + b
    return c
print (myfunction(10, 20))
print (myfunction.__annotations__)