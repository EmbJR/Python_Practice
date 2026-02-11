''' OOP stands for Object-oriented programming paradigm. It is defined as a programming
model that uses the concept of objects which refers to real-world entities with state and
behavior. This chapter helps you become an expert in using object-oriented programming
support in Python language.

Python is a programming language that supports object-oriented programming. This
makes it simple to create and use classes and objects. If you do not have any prior
experience with object-oriented programming, you are at the right place. Let's start by
discussing a small introduction of Object-Oriented Programming (OOP) to help you.
'''
'''
Procedural Oriented Approach
Early programming languages developed in 50s and 60s are recognized as procedural (or
procedure oriented) languages.

A computer program describes procedure of performing certain task by writing a series of
instructions in a logical order. Logic of a more complex program is broken down into
smaller but independent and reusable blocks of statements called functions.

Every function is written in such a way that it can interface with other functions in the
program. Data belonging to a function can be easily shared with other in the form of
arguments, and called function can return its result back to calling function.

Prominent problems related to procedural approach are as follows −
     Its top-down approach makes the program difficult to maintain.
     It uses a lot of global data items, which is undesired. Too many global data items
        would increase memory overhead.
     It gives more importance to process and doesn't consider data of same importance
        and takes it for granted, thereby it moves freely through the program.
     Movement of data across functions is unrestricted. In real-life scenario where there
        is unambiguous association of a function with data it is expected to process.'''

''' Python - OOP Concepts
In the real world, we deal with and process objects, such as student, employee, invoice,
car, etc. Objects are not only data and not only functions, but combination of both. Each
real-world object has attributes and behavior associated with it.
Attributes
     Name, class, subjects, marks, etc., of student
     Name, designation, department, salary, etc., of employee
     Invoice number, customer, product code and name, price and quantity, etc., in an
        invoice
     Registration number, owner, company, brand, horsepower, speed, etc., of car

Each attribute will have a value associated with it. Attribute is equivalent to data.
Behavior
Processing attributes associated with an object.
     Compute percentage of student's marks
     Calculate incentives payable to employee
     Apply GST to invoice value
     Measure speed of ca.

Behavior is equivalent to function. In real life, attributes and behavior are not independent
of each other, rather they co-exist.

The most important feature of object-oriented approach is defining attributes and their
functionality as a single unit called class. It serves as a blueprint for all objects having
similar attributes and behavior.

In OOP, class defines what are the attributes its object has, and how is its behavior. Object,
on the other hand, is an instance of the class.'''

''' Principles of OOPs Concepts
Object-oriented programming paradigm is characterized by the following principles −
 Class
 Object
 Encapsulation
 Inheritance
 Polymorphism
'''

''' Class & Object
A class is a user-defined prototype for an object that defines a set of attributes that
characterize any object of the class. The attributes are data members (class variables and
instance variables) and methods, accessed via dot notation.

An object refers to an instance of a certain class. For example, an object named obj that
belongs to a class Circle is an instance of that class. A unique instance of a data structure
that is defined by its class. An object comprises both data members (class variables and
instance variables) and methods.

Example
The below example illustrates how to create a class and its object in Python.'''

# defining class
class Smartphone:
    # constructor
    def __init__(self, device, brand):
        self.device = device
        self.brand = brand
    # method of the class
    def description(self):
        return f"{self.device} of {self.brand} supports Android 14"
# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung")
print(phoneObj.description())

''' Encapsulation
Data members of class are available for processing to functions defined within the class
only. Functions of class on the other hand are accessible from outside class context. So
object data is hidden from environment that is external to class. Class function (also called
method) encapsulates object data so that unwarranted access to it is prevented.

Example
In this example, we are using the concept of encapsulation to set the price of desktop.'''
class Desktop:
    def __init__(self):
        self.__max_price = 25000
    def sell(self):
        return f"Selling Price: {self.__max_price}"
    def set_max_price(self, price):
        if price > self.__max_price:
            self.__max_price = price
# Object
desktopObj = Desktop()
print(desktopObj.sell())
# modifying the price directly
desktopObj.__max_price = 35000
print(desktopObj.sell())
# modifying the price using setter function
desktopObj.set_max_price(35000)
print(desktopObj.sell())

''' Inheritance
A software modelling approach of OOP enables extending capability of an existing class to
build new class instead of building from scratch. In OOP terminology, existing class is
called base or parent class, while new class is called child or sub class.

Child class inherits data definitions and methods from parent class. This facilitates reuse
of features already available. Child class can add few more definitions or redefine a base
class function.
Syntax:- Derived classes are declared much like their parent class; however, a list of base classes
to inherit from is given after the class name
    class SubClassName (ParentClass1[, ParentClass2, ...]):
        'Optional class documentation string'
        class_suite
Example
The following example demonstrates the concept of Inheritance in Python −'''

#!/usr/bin/python
# define parent class
class Parent:
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")
    def parentMethod(self):
        print ("Calling parent method")
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)
# define child class
class Child(Parent):
    def __init__(self):
        print ("Calling child constructor")
    def childMethod(self):
        print ("Calling child method")
# instance of child
c = Child()
# child calls its method
c.childMethod()
# calls parent's method
c.parentMethod()
# again call parent's method
c.setAttr(200)
# again call parent's method
c.getAttr()

''' Similar way, you can drive a class from multiple parent classes as follow syntax:- 
    class A: # define your class A
    .....
    class B: # define your class B
    .....
    class C(A, B): # subclass of A and B
    .....'''

''' You can use issubclass() or isinstance() functions to check a relationships of two classes
and instances.
     The issubclass(sub, sup) boolean function returns true if the given subclass sub
        is indeed a subclass of the superclass sup.
     The isinstance(obj, Class) boolean function returns true if obj is an instance of
        class Class or is an instance of a subclass of Class
'''

''' Polymorphism
Polymorphism is a Greek word meaning having multiple forms. In OOP, polymorphism
occurs when each sub class provides its own implementation of an abstract method in
base class.

You can always override your parent class methods. One reason for overriding parent's
methods is because you may want special or different functionality in your subclass

Example
In this example, we are overriding the parent's method.'''
# define parent class
class Parent:
    def myMethod(self):  # Define a method named myMethod that takes self as parameter
        print ("Calling parent method")  # Print the string "Calling parent method" to console
    # define child class
class Child(Parent):
    def myMethod(self):
        print ("Calling child method")
# instance of child
c = Child()
# child calls overridden method
c.myMethod()

''' Base Overloading Methods in Python
Following table lists some generic functionality that you can override in your own classes

Table 1: Base Overloading Methods in Python
+------+--------------------------+--------------------------------------+
| Sr. | Method                   | Description & Sample Call            |
| No. |                          |                                      |
+------+--------------------------+--------------------------------------+
| 1    | __init__(self [,args...])| Constructor (with any optional        |
|      |                          | arguments)                           |
|      |                          | Sample Call: obj = className(args)   |
+------+--------------------------+--------------------------------------+
| 2    | __del__(self)            | Destructor, deletes an object        |
|      |                          | Sample Call: del obj                 |
+------+--------------------------+--------------------------------------+
| 3    | __repr__(self)           | Evaluable string representation      |
|      |                          | Sample Call: repr(obj)               |
+------+--------------------------+--------------------------------------+
| 4    | __str__(self)            | Printable string representation      |
|      |                          | Sample Call: str(obj)                |
+------+--------------------------+--------------------------------------+
| 5    | __cmp__(self, x)         | Object comparison                    |
|      |                          | Sample Call: cmp(obj, x)             |
+------+--------------------------+--------------------------------------+
'''

''' Overloading Operators in Python
Suppose you have created a Vector class to represent two-dimensional vectors, what
happens when you use the plus operator to add them? Most likely Python will yell at you.

You could, however, define the __add__ method in your class to perform vector addition
and then the plus operator would behave as per expectation −
Example:-'''
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
'''When the above code is executed, it produces the following result −
>> Vector(7,8)'''

'''----------------------------- Python - Classes and Objects -----------------------------
Python is an object-oriented programming language, which means that it is based on
principle of OOP concept. The entities used within a Python program is an object of one or
another class. For instance, numbers, strings, lists, dictionaries, and other similar entities
of a program are objects of the corresponding built-in class.

In Python, a class named Object is the base or parent class for all the classes, built-in as
well as user defined.'''

''' What is a Class in Python?
In Python, a class is a user defined entity (data type) that defines the type of data an
object can contain and the actions it can perform. It is used as a template for creating
objects. For instance, if we want to define a class for Smartphone in a Python program,
we can use the type of data like RAM, ROM, screen-size and actions like call and message.
'''
'''Creating Classes in Python
The class keyword is used to create a new class in Python. The name of the class
immediately follows the keyword class followed by a colon as shown below
-----------------
class ClassName:
    'Optional class documentation string'
    class_suite
---------------
     The class has a documentation string, which can be accessed via
        ClassName.__doc__.
     The class_suite consists of all the component statements defining class members,
        data attributes and functions.
Example
Following is the example of a simple Python class'''
class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary
''' 
     The variable empCount is a class variable whose value is shared among all
        instances of this class. This can be accessed as Employee.empCount from inside
        the class or outside the class.
     The first method __init__() is a special method, which is called class constructor
        or initialization method that Python calls when you create a new instance of this
        class.
     You declare other class methods like normal functions with the exception that the
        first argument to each method is self. Python adds the self argument to the list for
        you; you do not need to include it when you call the methods.'''

''' What is an Object?
An object is referred to as an instance of a given Python class. Each object has its own
attributes and methods, which are defined by its class.
When a class is created, it only describes the structure of objects. The memory is allocated
when an object is instantiated from a class.'''

'''For Example:- Vehicle is the class name and Car, Bus and SUV are its objects.
'''
'''Creating Objects of Classes in Python
To create instances of a class, you call the class using class name and pass in whatever
arguments its __init__ method accepts.
----------------------
# This would create first object of Employee class
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)
--------------------'''

''' Accessing Attributes of Objects in Python
You access the object's attributes using the dot operator with object. Class variable would
be accessed using class name as follows
----------------------------
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
------------------------
Now, putting all the concepts together −'''
class Employee:
    "Common base class for all employees"
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)
# This would create first object of Employee class
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

''' You can add, remove, or modify attributes of classes and objects at any time
like below'''
# Add an 'age' attribute
emp1.age = 7
# Modify 'age' attribute
emp2.age = 8
# Delete 'age' attribute
del emp1.age

''' Instead of using the normal statements to access attributes, you can also use the following
functions −
     getattr(obj, name[, default]) − to access the attribute of object.
     hasattr(obj,name) − to check if an attribute exists or not.
     setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it
        would be created.
     delattr(obj, name) − to delete an attribute.'''

# Returns true if 'age' attribute exists
hasattr(emp1, 'age')
# Returns value of 'age' attribute
getattr(emp1, 'age')
# Set attribute 'age' at 8
setattr(emp1, 'age', 8)
# Delete attribute 'age'
delattr(emp1, 'age')

''' Built-In Class Attributes in Python
Every Python class keeps following built-in attributes and they can be accessed using dot
operator like any other attribute

Table 2: Built-In Class Attributes in Python
+------+--------------------------+--------------------------------------+
| Sr. | Attribute                | Description                          |
| No. |                          |                                      |
+------+--------------------------+--------------------------------------+
| 1    | __dict__                 | Dictionary containing the class's    |
|      |                          | namespace.                           |
+------+--------------------------+--------------------------------------+
| 2    | __doc__                  | Class documentation string or none,  |
|      |                          | if undefined.                        |
+------+--------------------------+--------------------------------------+
| 3    | __name__                 | Class name                           |
+------+--------------------------+--------------------------------------+
| 4    | __module__               | Module name in which the class is    |
|      |                          | defined. This attribute is           |
|      |                          | "__main__" in interactive mode.      |
+------+--------------------------+--------------------------------------+
| 5    | __bases__                | A possibly empty tuple containing    |
|      |                          | the base classes, in the order of    |
|      |                          | their occurrence in the base class   |
|      |                          | list.                                |
+------+--------------------------+--------------------------------------+
'''

''' 
Example
For the above Employee class, let us try to access its attributes'''
class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

''' Built-in Class of Python datatypes
As mentioned earlier, Python follows object-oriented programming paradigm. Entities like
strings, lists and data types belongs to one or another built-in class.
If we want to see which data type belongs to which built-in class, we can use the Python
type() function. This function accepts a data type and returns its corresponding class.
Example
The below example demonstrates how to check built-in class of a given data type.'''
num = 20
print (type(num))
num1 = 55.50
print (type(num1))
s = "TutorialsPoint"
print (type(s))
dct = {'a':1,'b':2,'c':3}
print (type(dct))
def SayHello():
    print ("Hello World")
    return
print (type(SayHello))

''' Garbage Collection(Destroying Objects) in Python
Python deletes unwanted objects (built-in types or class instances) automatically to free
the memory space. The process by which Python periodically reclaims blocks of memory
that no longer are in use is termed Garbage Collection.

Python's garbage collector runs during program execution and is triggered when an
object's reference count reaches zero. An object's reference count changes as the number
of aliases that point to it changes.

An object's reference count increases when it is assigned a new name or placed in a
container (list, tuple, or dictionary). The object's reference count decreases when it's
deleted with del, its reference is reassigned, or its reference goes out of scope. When an
object's reference count reaches zero, Python collects it automatically.'''
# Create object <40>
a = 40
# Increase ref. count of <40>
b = a
# Increase ref. count of <40>
c = [b]
# Decrease ref. count of <40>
del a
# Decrease ref. count of <40>
b = 100
# Decrease ref. count of <40>
c[0] = -1

'''You normally will not notice when the garbage collector destroys an unused instance and
reclaims its space. But a class can implement the special method __del__(), called a
destructor, that is invoked when the instance is about to be destroyed. This method might
be used to clean up any non-memory resources used by an instance.
Example
The __del__() destructor prints the class name of an instance that is about to be destroyed
as shown in the below code block'''

class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
# prints the ids of the obejcts
print (id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3

''' Data Hiding in Python
An object's attributes may or may not be visible outside the class definition. You need to
name attributes with a double underscore prefix, and those attributes then are not be
directly visible to outsiders.'''

class JustCounter:
    __secretCount = 0
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)
counter = JustCounter()
counter.count()
counter.count()
print(counter.__secretCount)
''' Python protects those members by internally changing the name to include the class name.
You can access such attributes as object._className__attrName. If you would replace
your last line, then it works for you'''
print(counter._JustCounter__secretCount)