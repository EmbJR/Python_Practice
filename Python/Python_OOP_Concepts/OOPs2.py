'''------------------------------- Python - Class Attributes -----------------------------
The properties or variables defined inside a class are called as Attributes. An attribute
provides information about the type of data a class contains. There are two types of
attributes in Python namely instance attribute and class attribute.

The instance attribute is defined within the constructor of a Python class and is unique to
each instance of the class. And, a class attribute is declared and initialized outside the
constructor of the class.'''

''' Class Attributes (Variables)
Class attributes are those variables that belong to a class and whose value is shared among
all the instances of that class. A class attribute remains the same for every instance of the
class.

Class attributes are defined in the class but outside any method. They cannot be initialized
inside __init__() constructor. They can be accessed by the name of the class in addition
to the object. In other words, a class attribute is available to the class as well as its object.
'''

'''Accessing Class Attributes
The object name followed by dot notation (.) is used to access class attributes.
Example
The below example demonstrates how to access the attributes of a Python class.'''
class Employee:
    name = "Bhavesh Aggarwal"
    age = "30"
# instance of the class
emp = Employee()
# accessing class attributes
print("Name of the Employee:", emp.name)
print("Age of the Employee:", emp.age)

''' Modifying Class Attributes
To modify the value of a class attribute, we simply need to assign a new value to it using
the class name followed by dot notation and attribute name. In the below example, we are 
initializing a class variable called empCount in Employee class. For each object declared, 
the __init__() method is automatically called. This method
initializes the instance variables as well as increments the empCount by 1.'''

class Employee:
    # class attribute
    empCount = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        # modifying class attribute
        Employee.empCount += 1
        print ("Name:", self.__name, ", Age: ", self.__age)
        # accessing class attribute
        print ("Employee Count:", Employee.empCount)
e1 = Employee("Bhavana", 24)
print()
e2 = Employee("Rajesh", 26)

'''Significance of Class Attributes
The class attributes are important because of the following reasons −
     They are used to define those properties of a class that should have the same value
        for every object of that class.
     Class attributes can be used to set default values for objects.
     This is also useful in creating singletons. They are objects that are instantiated only
        once and used in different parts of the code.'''

'''Built-In Class Attributes
Every Python class keeps the following built-in attributes and they can be accessed using
the dot operator like any other attribute −
     __dict__ − Dictionary containing the class's namespace.
     __doc__ − Class documentation string or none, if undefined.
     __name__ − Class name.
     __module__ − Module name in which the class is defined. This attribute is
        "__main__" in interactive mode.
     __bases__ − A possibly empty tuple containing the base classes, in the order of
        their occurrence in the base class list.'''

''' Access Built-In Class Attributes
To access built-in class attributes in Python, we use the class name followed by a dot (.)
and then attribute name.
Example
For the Employee class, we are trying to access all the built-in class attributes'''
class Employee:
    def __init__(self, name="Bhavana", age=24):
        self.name = name
        self.age = age
    def displayEmployee(self):
        print ("Name : ", self.name, ", age: ", self.age)
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )

''' Instance Attributes
As stated earlier, an instance attribute in Python is a variable that is specific to an
individual object of a class. It is defined inside the __init__() method.
The first parameter of this method is self and using this parameter the instance attributes
are defined.
Example
In the following code, we are illustrating the working of instance attributes.'''
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade
        print ("Name:", self.__name, ", Grade:", self.__grade)
# Creating instances
student1 = Student("Ram", "B")
student2 = Student("Shyam", "C")

''' Instance Attributes Vs Class Attributes
The below table shows the difference between instance attributes and class attributes
'''

''' Instance Attributes Vs Class Attributes
The below table shows the difference between instance attributes and class attributes

+------+---------------------------+---------------------------+
| SNo. | Instance Attribute        | Class Attribute           |
+------+---------------------------+---------------------------+
| 1    | It is defined directly    | It is defined inside the  |
|      | inside the __init__()     | class but outside the     |
|      | function.                 | __init__() function.      |
+------+---------------------------+---------------------------+
| 2    | Instance attribute is      | Class attributes can be   |
|      | accessed using the object | accessed by both class    |
|      | name followed by dot      | name and object name.     |
|      | notation.                 |                           |
+------+---------------------------+---------------------------+
| 3    | The value of this         | Its value is shared among |
|      | attribute cannot be       | other objects of the      |
|      | shared among other        | class.                    |
|      | objects.                  |                           |
+------+---------------------------+---------------------------+
| 4    | Changes made to the       | Changes made to the class |
|      | instance attribute affect | attribute affect all the  |
|      | only the object within    | objects of the given      |
|      | which it is defined.      | class.                    |
+------+---------------------------+---------------------------+
'''
'''-------------------------------- Python - Class Methods -------------------------------
Methods belongs to an object of a class and used to perform specific operations. We can
divide Python methods in three different categories, which are class method, instance
method and static method.

A Python class method is bound to the class and not to the instance of the class. It can
be called on the class itself, rather than on an instance of the class.

Most of us often get class methods confused with static methods. Always remember, while
both are called on the class, static methods do not have access to the "cls" parameter
and therefore it cannot modify the class state.

Unlike class method, the instance method can access the instance variables of the an
object. It can also access the class variable as it is common to all the objects.

Creating Class Methods in Python
There are two ways to create class methods in Python −
     Using classmethod() Function
     Using @classmethod Decorator'''

''' Using classmethod() Function
Python has a built-in function classmethod() which transforms an instance method to a
class method which can be called with the reference to the class only and not the object.
Syntax:- classmethod(instance_method)
Example:- 
In the Employee class, define a showcount() instance method with the "self" argument
(reference to calling object). It prints the value of empCount. Next, transform the method
to class method counter() that can be accessed through the class reference.'''
class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.empCount += 1
    def showcount(self):
        print (self.empCount)
    counter = classmethod(showcount)
e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e1.showcount()
Employee.counter()

''' Using @classmethod Decorator
Use of @classmethod() decorator is the prescribed way to define a class method as it is
more convenient than first declaring an instance method and then transforming it into a
class method.
Syntax:-
----------------
@classmethod
def method_name():
    # your code
---------------
Example
The class method acts as an alternate constructor. Define a newemployee() class method
with arguments required to construct a new object. It returns the constructed object,
something that the __init__() method does.'''
class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1
    @classmethod
    def showcount(cls):
        print (cls.empCount)
    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)
e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Anil", 21)
Employee.showcount()

''' Access Class Attributes in Class Method
Class attributes are those variables that belong to a class and whose value is shared among
all the instances of that class.

To access class attributes within a class method, use the cls parameter followed by dot (.)
notation and name of the attribute.

Example:-
In this example, we are accessing a class attribute in class method'''
class Cloth:
    # Class attribute
    price = 4000
    @classmethod
    def showPrice(cls):
        return cls.price
# Accessing class attribute
print(Cloth.showPrice())

''' Dynamically Add Class Method to a Class
The Python setattr() function is used to set an attribute dynamically. If you want to add a
class method to a class, pass the method name as a parameter value to setattr() function.
The following example shows how to add a class method dynamically to a Python class.'''
class Cloth:
    pass
    # class method
@classmethod
def brandName(cls):
    print("Name of the brand is Raymond")
# adding dynamically
setattr(Cloth, "brand_name", brandName)
newObj = Cloth()
newObj.brand_name()

''' Dynamically Delete Class Methods
The Python del operator is used to delete a class method dynamically. If you try to access
the deleted method, the code will raise AttributeError.

Example
In the below example, we are deleting the class method named "brandName" using del
operator'''
class Cloth:
    # class method
    @classmethod
    def brandName(cls):
        print("Name of the brand is Raymond")
# deleting dynamically
del Cloth.brandName
print("Method deleted")

'''-------------------------------------- Python - Static Methods -----------------------------------
What is Python Static Method?
In Python, a static method is a type of method that does not require any instance to be
called. It is very similar to the class method but the difference is that the static method
doesn't have a mandatory argument like reference to the object − self or reference to the
class − cls.

Static methods are used to access static fields of a given class. They cannot modify the
state of a class since they are bound to the class, not instance.

How to Create Static Method in Python?
There are two ways to create Python static methods −
     Using staticmethod() Function
     Using @staticmethod Decorator
'''
''' Using staticmethod() Function
Python's standard library function named staticmethod() is used to create a static method.
It accepts a method as an argument and converts it into a static method.
Syntax:- staticmethod(method)

Example:-
In the Employee class below, the showcount() method is converted into a static method.
This static method can now be called by its object or reference of class itself.'''
class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.empCount += 1
    # creating staticmethod
    def showcount():
        print (Employee.empCount)
        return
    counter = staticmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e1.counter()
Employee.counter()

''' Using @staticmethod Decorator
The second way to create a static method is by using the Python @staticmethod decorator.
When we use this decorator with a method it indicates to the Interpreter that the specified
method is static.

Syntax:- @staticmethod
-----------------------
def method_name():
    # your code
-----------------------
Example:- 
In the following example, we are creating a static method using the @staticmethod
decorator.'''
class Student:
    stdCount = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Student.stdCount += 1
    # creating staticmethod
    @staticmethod
    def showcount():
        print (Student.stdCount)
e1 = Student("Bhavana", 24)
e2 = Student("Rajesh", 26)
e3 = Student("John", 27)
print("Number of Students:")
Student.showcount()

''' Advantages of Static Method
There are several advantages of using static method, which includes −
     Since a static method cannot access class attributes, it can be used as a utility
        function to perform frequently re-used tasks.
     We can invoke this method using the class name. Hence, it eliminates the
        dependency on the instances.
     A static method is always predictable as its behavior remain unchanged regardless
        of the class state.
     We can declare a method as a static method to prevent overriding.'''

'''--------------------------------- Python - Constructors ----------------------------
Python constructor is an instance method in a class, that is automatically called whenever
a new object of the class is created. The constructor's role is to assign value to instance
variables as soon as the object is declared.

Python uses a special method called __init__() to initialize the instance variables for the
object, as soon as it is declared.'''

''' Creating a constructor in Python
The __init__() method acts as a constructor. It needs a mandatory argument named self,
which is the reference to the object.
------------
def __init__(self, parameters):
#initialize instance variables
-----------
The __init__() method as well as any instance method in a class has a mandatory
parameter, self. However, you can give any name to the first parameter, not necessarily
self'''

''' Types of Constructor in Python
Python has two types of constructor −
     Default Constructor
     Parameterized Constructor

Default Constructor in Python
The Python constructor which does not accept any parameter other than self is called as
default constructor.

Example:- 
Let us define the constructor in the Employee class to initialize name and age as instance
variables. We can then access these attributes through its object.'''
class Employee:
    'Common base class for all employees'
    def __init__(self):
        self.name = "Bhavana"
        self.age = 24
e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))

''' For the above Employee class, each object we declare will have same value for its instance
variables name and age. To declare objects with varying attributes instead of the default,
define arguments for the __init__() method.
'''

''' Parameterized Constructor
If a constructor is defined with multiple parameters along with self is called as
parameterized constructor.
Example:- 
In this example, the __init__() constructor has two formal arguments. We declare
Employee objects with different values'''
class Employee:
    'Common base class for all employees'
    def __init__(self, name, age):
        self.name = name
        self.age = age
e1 = Employee("Bhavana", 24)
e2 = Employee("Bharat", 25)
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))

''' You can also assign default values to the formal arguments in the constructor so that the
object can be instantiated with or without passing parameters
Example:-'''
class Employee:
    'Common base class for all employees'
    def __init__(self, name="Bhavana", age=24):
        self.name = name
        self.age = age
e1 = Employee()
e2 = Employee("Bharat", 25)
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))

''' Python - Instance Methods
In addition to the __init__() constructor, there may be one or more instance methods
defined in a class..

Example
In the following example a displayEmployee() method has been defined as an instance
method.'''

class Employee:
    def __init__(self, name="Bhavana", age=24):
        self.name = name
        self.age = age
    def displayEmployee(self):
        print ("Name : ", self.name, ", age: ", self.age)
e1 = Employee()
e2 = Employee("Bharat", 25)
e1.displayEmployee()
e2.displayEmployee()

''' You can add, remove, or modify attributes of classes and objects at any time −
Example:- 
# Add a 'salary' attribute
emp1.salary = 7000
# Modify 'name' attribute
emp1.name = 'xyz'
# Delete 'salary' attribute
del emp1.salary'''

'''Python Multiple Constructors
As mentioned earlier, we define the __init__() method to create a constructor. However,
unlike other programming languages like C++ and Java, Python does not allow multiple
constructors.

If you try to create multiple constructors, Python will not throw an error, but it will only
consider the last __init__() method in your class. Its previous definition will be overridden
by the last one.

But, there is a way to achieve similar functionality in Python. We can overload constructors
based on the type or number of arguments passed to the __init__() method. This will allow a 
single constructor method to handle various initialization scenarios based on the arguments 
provided.
Example:- 
The following example shows how to achieve functionality similar to multiple constructors'''
class Student:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.age = args[1]
            self.gender = args[2]
st1 = Student("Shrey")
print("Name:", st1.name)
st2 = Student("Ram", 25)
print(f"Name: {st2.name} and Age: {st2.age}")
st3 = Student("Shyam", 26, "M")
print(f"Name: {st3.name}, Age: {st3.age} and Gender: {st3.gender}")

'''-------------------------------------- Python - Access Modifiers ----------------------------
The Python access modifiers are used to restrict access to class members (i.e., variables
and methods) from outside the class. There are three types of access modifiers namely
public, protected, and private.
     Public members − A class member is said to be public if it can be accessed from
        anywhere in the program.
     Protected members − They are accessible from within the class as well as by
        classes derived from that class.
     Private members − They can be accessed from within the class only.

Usually, methods are defined as public and instance variable are private. This arrangement
of private instance variables and public methods ensures implementation of principle of
encapsulation.'''

'''Access Modifiers in Python
Unlike C++ and Java, Python does not use the Public, Protected and Private keywords to
specify the type of access modifiers. By default, all the variables and methods in a Python
class are public.

Example:-
Here, we have Employee class with instance variables name and age. An object of this
class has these two attributes. They can be directly accessed from outside the class,
because they are public.'''

class Employee:
    'Common base class for all employees'
    def __init__(self, name="Bhavana", age=24):
        self.name = name
        self.age = age
e1 = Employee()
e2 = Employee("Bharat", 25)
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))

''' Python doesn't enforce restrictions on accessing any instance variable or method.
However, Python prescribes a convention of prefixing name of variable/method with single
or double underscore to emulate behavior of protected and private access modifiers.
To indicate that an instance variable is private, prefix it with double underscore (such as
"__age").

To imply that a certain instance variable is protected, prefix it with single underscore (such
as "_salary").

Another Example:- 
Let us modify the Employee class. Add another instance variable salary. Make age private
and salary as protected by prefixing double and single underscores respectively.'''
class Employee:
    def __init__(self, name, age, salary):
        self.name = name # public variable
        self.__age = age # private variable
        self._salary = salary # protected variable
    def displayEmployee(self):
        print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)
e1=Employee("Bhavana", 24, 10000)
print (e1.name)
print (e1._salary)
print (e1.__age) # Python displays AttributeError because __age is private, and not available for use outside
                 # the class.
''' Name Mangling
Python doesn't block access to private data, it just leaves for the wisdom of the
programmer, not to write any code that access it from outside the class. You can still
access the private members by Python's name mangling technique.

Name mangling is the process of changing name of a member with double underscore to
the form object._class__variable. If so required, it can still be accessed from outside the
class, but the practice should be refrained.

In our example, the private instance variable "__name" is mangled by changing it to the
format:- obj._class__privatevar

So, to access the value of "__age" instance variable of "e1" object, change it to
"e1._Employee__age".

Change the print() statement in the above program to −
print (e1._Employee__age)
It now prints 24, the age of e1.'''
print (e1._Employee__age)

''' Python Property Object
Python's standard library has a built-in property() function. It returns a property object.
It acts as an interface to the instance variables of a Python class.

The encapsulation principle of object-oriented programming requires that the instance
variables should have a restricted private access. Python doesn't have efficient mechanism
for the purpose. The property() function provides an alternative.

The property() function uses the getter, setter and delete methods defined in a class to
define a property object for the class.
Syntax:- property(fget=None, fset=None, fdel=None, doc=None)
Parameters
     fget − an instance method that retrieves value of an instance variable.
     fset − an instance method that assigns value to an instance variable.
     fdel − an instance method that removes an instance variable
     fdoc − Documentation string for the property.
The function uses getter and setter methods to return the property object.'''

''' Getters and Setter Methods
A getter method retrieves the value of an instance variable, usually named as
get_varname, whereas the setter method assigns value to an instance variable − named
as set_varname.

Example:- 
Let us define getter methods get_name() and get_age(), and setters set_name() and
set_age() in the Employee class.'''
class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
        return
    def set_age(self, age):
        self.__age=age
e1=Employee("Bhavana", 24)
print ("Name:", e1.get_name(), "age:", e1.get_age())
e1.set_name("Archana")
e1.set_age(21)
print ("Name:", e1.get_name(), "age:", e1.get_age())

''' The getter and setter methods can retrieve or assign value to instance variables. The
property() function uses them to add property objects as class attributes.

The name property is defined as −
    name = property(get_name, set_name, "name")
Similarly, you can add the age property −
    age = property(get_age, set_age, "age")

The advantage of the property object is that you can use to retrieve the value of its
associated instance variable, as well as assign value.

For example,
----------
print (e1.name) displays value of e1.__name
e1.name = "Archana" assigns value to e1.__age
---------
Example:-
The complete program with property objects and their use is given below −'''

class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
        return
    def set_age(self, age):
        self.__age=age
        return
name = property(get_name, set_name, "name")
age = property(get_age, set_age, "age")
e1=Employee("Bhavana", 24)
print ("Name:", e1.name, "age:", e1.age)
e1.name = "Archana"
e1.age = 23
print ("Name:", e1.name, "age:", e1.age)

'''----------------------------- Python - Inheritance -----------------------------
What is Inheritance in Python?
Inheritance is one of the most important features of object-oriented programming
languages like Python. It is used to inherit the properties and behaviors of one class to
another.
'''

'''Creating a Parent Class
The class whose attributes and methods are inherited is called as parent class. It is defined
just like other classes i.e. using the class keyword.
Syntax:- 
        class ParentClassName:
            {class body}
'''            

'''
Creating a Child Class
Classes that inherit from base classes are declared similarly to their parent class, however,
we need to provide the name of parent classes within the parentheses.
Syntax:- 
    class SubClassName (ParentClass1[, ParentClass2, ...]):
        {sub class body}
'''

''' Types of Inheritance
In Python, inheritance can be divided in five different categories −
     Single Inheritance
     Multiple Inheritance
     Multilevel Inheritance
     Hierarchical Inheritance
     Hybrid Inheritance'''

''' Python - Single Inheritance
This is the simplest form of inheritance where a child class inherits attributes and methods
from only one parent class.
Example
The below example shows single inheritance concept in Python'''
# parent class
class Parent:
    def parentMethod(self):
        print ("Calling parent method")
    # child class

class Child(Parent):
    def childMethod(self):
        print ("Calling child method")

# instance of child
c = Child()
# calling method of child class
c.childMethod()
# calling method of parent class
c.parentMethod()

''' Python - Multiple Inheritance
Multiple inheritance in Python allows you to construct a class based on more than one
parent classes. The child class thus inherits the attributes and method from all parents.
The child can override methods inherited from any parent.
Syntax
------------------------
class parent1:
#statements
class parent2:
#statements
class child(parent1, parent2):
#statements
-----------------------

Example:- 
Python's standard library has a built-in divmod() function that returns a two-item tuple.
First number is the division of two arguments, the second is the mod value of the two
operands.

This example tries to emulate the divmod() function. We define two classes division and
modulus, and then have a div_mod class that inherits them.'''

class division:
    def __init__(self, a,b):        
        self.n=a
        self.d=b
        print("Parant Divide initiallized")
    def divide(self):
        return self.n/self.d
class modulus:
    def __init__(self, a,b):
        self.n=a
        self.d=b
        print("Parant Modulo initiallized")
    def mod_divide(self):
        return self.n%self.d
class div_mod(division,modulus):
    def __init__(self, a,b):
        self.n=a
        self.d=b
        print("Child initiallized")
    def div_and_mod(self):
        divval=division.divide(self)
        modval=modulus.mod_divide(self)
        return (divval, modval)

x=div_mod(10,3)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())

''' Method Resolution Order (MRO)
The term method resolution order is related to multiple inheritance in Python. In Python,
inheritance may be spread over more than one levels. Let us say A is the parent of B, and
B the parent for C. The class C can override the inherited method or its object may invoke
it as defined in its parent. So, how does Python find the appropriate method to call.

Each Python class has a mro() method that returns the hierarchical order that Python uses
to resolve the method to be called. The resolution order starts from bottom of inheritance
order to top.

In our previous example, the div_mod class inherits division and modulus classes. So, the
mro method returns the order as follows 

[<class '__main__.div_mod'>, <class '__main__.division'>, <class
'__main__.modulus'>, <class 'object'>]'''

'''Python - Multilevel Inheritance
In multilevel inheritance, a class is derived from another derived class. Multiple layers of
inheritance exist here. We can imagine it as a grandparent-parent-child relationship.
Example
In the following example, we are illustrating the working of multilevel inheritance.'''

# parent class
class Universe:
    def universeMethod(self):
        print ("I am in the Universe")
# child class
class Earth(Universe):
    def earthMethod(self):
        print ("I am on Earth")
# another child class
class India(Earth):
    def indianMethod(self):
        print ("I am in India")
# creating instance
person = India()
# method calls
person.universeMethod()
person.earthMethod()
person.indianMethod()

''' Python - Hierarchical Inheritance
This type of inheritance contains multiple derived classes that are inherited from a single
base class. This is similar to the hierarchy within an organization.
Example
The following example illustrates hierarchical inheritance. Here, we have defined two child
classes of Manager class'''
# parent class
class Manager:
    def managerMethod(self):
        print ("I am the Manager")
# child class
class Employee1(Manager):
    def employee1Method(self):
        print ("I am Employee one")
# second child class
class Employee2(Manager):
    def employee2Method(self):
        print ("I am Employee two")
# creating instances
emp1 = Employee1()
emp2 = Employee2()
# method calls
emp1.managerMethod()
emp1.employee1Method()
emp2.managerMethod()
emp2.employee2Method()

''' Python - Hybrid Inheritance
Combination of two or more types of inheritance is called as Hybrid Inheritance. For
instance, it could be a mix of single and multiple inheritance.
Example
In this example, we have combined single and multiple inheritance to form a hybrid
inheritance of classes.'''
# parent class
class CEO:
    def ceoMethod(self):
        print ("I am the CEO")
class Manager(CEO):
    def managerMethod(self):
        print ("I am the Manager")
class Employee1(Manager):
    def employee1Method(self):
        print ("I am Employee one")
class Employee2(Manager, CEO):
    def employee2Method(self):
        print ("I am Employee two")
# creating instances
emp = Employee2()
# method calls
emp.managerMethod()
emp.ceoMethod()
emp.employee2Method()

''' The super() function
In Python, super() function allows you to access methods and attributes of the parent
class from within a child class.
Example
In the following example, we create a parent class and access its constructor from a
subclass using the super() function.'''
# parent class
class ParentDemo:
    def __init__(self, msg):
        self.message = msg
    def showMessage(self):
        print(self.message)
# child class
class ChildDemo(ParentDemo):
    def __init__(self, msg):
        # use of super function
        super().__init__(msg)
# creating instance
obj = ChildDemo("Welcome to Tutorialspoint!!")
obj.showMessage()

'''-------------------------------- Python - Polymorphism ------------------------------
What is Polymorphism in Python?
The term polymorphism refers to a function or method taking different forms in different
contexts. Since Python is a dynamically typed language, polymorphism in Python is very
easily implemented.

If a method in a parent class is overridden with different business logic in its different child
classes, the base class method is a polymorphic method.'''

'''Ways of implementing Polymorphism in Python
There are four ways to implement polymorphism in Python −
     Duck Typing
     Operator Overloading
     Method Overriding
     Method Overloading'''

''' Duck Typing in Python
Duck typing is a concept where the type or class of an object is less important than the
methods it defines. Using this concept, you can call any method on an object without
checking its type, as long as the method exists.
This term is defined by a very famous quote that states: Suppose there is a bird that walks
like a duck, swims like a duck, looks like a duck, and quacks like a duck then it probably
is a duck.

Example:-
In the code given below, we are practically demonstrating the concept of duck typing.'''

class Duck:
    def sound(self):
        return "Quack, quack!"
class AnotherBird:
    def sound(self):
        return "I'm similar to a duck!"
def makeSound(duck):
    print(duck.sound())
# creating instances
duck = Duck()
anotherBird = AnotherBird()
# calling methods
makeSound(duck)
makeSound(anotherBird)

'''Method Overriding in Python
In method overriding, a method defined inside a subclass has the same name as a method
in its superclass but implements a different functionality.

Example:- 
As an example of polymorphism given below, we have shape which is an abstract class. It
is used as parent by two classes circle and rectangle. Both classes override parent's draw()
method in different ways'''

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract method"
        return
class circle(shape):
    def draw(self):
        super().draw()
        print ("Draw a circle")
        return
class rectangle(shape):
    def draw(self):
        super().draw()
        print ("Draw a rectangle")
        return
shapes = [circle(), rectangle()]
for shp in shapes:
    shp.draw()

'''The variable shp first refers to circle object and calls draw() method from circle class. In
next iteration, it refers to rectangle object and calls draw() method from rectangle class.
Hence draw() method in shape class is polymorphic.'''

''' Overloading Operators in Python
Suppose you have created a Vector class to represent two-dimensional vectors.
Example:- Please see previos topics for the example which covered.'''

''' Method Overloading in Python
When a class contains two or more methods with the same name but different number of
parameters then this scenario can be termed as method overloading.
Python does not allow overloading of methods by default
This topic covered previously
Example:-'''
def add(*nums):
    return sum(nums)
# Call the function with different number of parameters
result1 = add(10, 25)
result2 = add(10, 25, 35)
print(result1)
print(result2)

'''------------------------------------ Python - Method Overriding -----------------------------
Method Overriding in Python
The Python method overriding refers to defining a method in a subclass with the same
name as a method in its superclass. In this case, the Python interpreter determines which
method to call at runtime based on the actual object being referred to.

You can always override your parent class methods. One reason for overriding parent's
methods is that you may want special or different functionality in your subclass.

Example:-
In the code below, we are overriding a method named myMethod of Parent class.'''
# define parent class
class Parent:
    def myMethod(self):
        print ('Calling parent method')
# define child class
class Child(Parent):
    def myMethod(self):
        print ('Calling child method')
# instance of child
c = Child()
# child calls overridden method
c.myMethod()

'''To understand Method Overriding in Python, let us take another example. We use following
Employee class as parent class'''
class Employee:
    def __init__(self,nm, sal):
        self.name=nm
        self.salary=sal
def getName(self):
    return self.name
def getSalary(self):
    return self.salary

''' Next, we define a SalesOfficer class that uses Employee as parent class. It inherits the
instance variables name and salary from the parent. Additionally, the child class has one
more instance variable incentive.

We shall use built-in function super() that returns reference of the parent class and call
the parent constructor within the child constructor __init__() method.'''
class SalesOfficer(Employee):
    def __init__(self,nm, sal, inc):
        super().__init__(nm,sal)
        self.incnt=inc
def getSalary(self):
    return self.salary+self.incnt

''' The getSalary() method is overridden to add the incentive to salary.
Example:- 
Declare the object of parent and child classes and see the effect of overriding. Complete
code is below −''' 
class Employee:
    def __init__(self,nm, sal):
        self.name=nm
        self.salary=sal
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
class SalesOfficer(Employee):
    def __init__(self,nm, sal, inc):
        super().__init__(nm,sal)
        self.incnt=inc
    def getSalary(self):
        return self.salary+self.incnt
e1=Employee("Rajesh", 9000)
print ("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer('Kiran', 10000, 1000)
print ("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))

''' Base Overridable Methods
The following table lists some generic functionality of the object class, which is the parent
class for all Python classes. You can override these methods in your own class'''

''' Base Overridable Methods
The following table lists some generic functionality of the object class, which is the parent
class for all Python classes. You can override these methods in your own class

+------+---------------------------+-------------------------------------------+
| Sr.No | Method                    | Description & Sample Call                 |
+------+---------------------------+-------------------------------------------+
| 1    | __init__(self [,args...]) | Constructor (with any optional arguments) |
|      |                           | Sample Call: obj = className(args)       |
+------+---------------------------+-------------------------------------------+
| 2    | __del__(self)             | Destructor, deletes an object              |
|      |                           | Sample Call: del obj                      |
+------+---------------------------+-------------------------------------------+
| 3    | __repr__(self)            | Evaluatable string representation         |
|      |                           | Sample Call: repr(obj)                    |
+------+---------------------------+-------------------------------------------+
| 4    | __str__(self)             | Printable string representation            |
|      |                           | Sample Call: str(obj)                     |
+------+---------------------------+-------------------------------------------+
'''


'''-------------------------------- Python - Method Overloading -------------------------
Unlike other programming languages like Java, C++, and C#, Python does not support
the feature of method overloading by default. However, there are alternative ways to
achieve it.
Example
If you define a method multiple times as shown in the below code, the last definition will
override the previous ones. Therefore, this way of achieving method overloading in Python
generates error.'''
class example:
    def add(self, a, b):
        x = a+b
        return x
    def add(self, a, b, c):
        x = a+b+c
        return x
obj = example()
print (obj.add(10,20,30))
print (obj.add(10,20))      # this will throgh error as The output tells you that Python considers only the latest definition of add() method,
                            # discarding the earlier definitions.

''' The first call to add() method with three arguments is successful. However, calling add()
method with two arguments as defined in the class fails.

To overcome this issue, you can use the following approaches to achieve method overloading in Python:
Example:- '''
class example:
    def add(self, a = None, b = None, c = None):
        x=0
        if a !=None and b != None and c != None:
            x = a+b+c
        elif a !=None and b != None and c == None:
            x = a+b
        return x
obj = example()
print (obj.add(10,20,30))
print (obj.add(10,20))

''' With this workaround, we are able to incorporate method overloading in Python class.'''

'''Implement Method Overloading Using MultipleDispatch
Python's standard library doesn't have any other provision for implementing method
overloading. However, we can use a dispatch function from a third-party module named
MultipleDispatch for this purpose.
First, you need to install the Multipledispatch module using the following command −
    "pip install multipledispatch"

This module has a @dispatch decorator. It takes the number of arguments to be passed
to the method to be overloaded. Define multiple copies of add() method with @dispatch
decorator as below −

Example:-
In this example, we are using multipledispatch to overload a method in Python'''
from multipledispatch import dispatch
class example:
    @dispatch(int, int)
    def add(self, a, b):
        x = a+b
        return x
    @dispatch(int, int, int)
    def add(self, a, b, c):
        x = a+b+c
        return x
obj = example()
print (obj.add(10,20,30))
print (obj.add(10,20))

'''------------------------------ Python - Dynamic Binding ---------------------------
In object-oriented programming, the concept of dynamic binding is closely related to
polymorphism. In Python, dynamic binding is the process of resolving a method or
attribute at runtime, instead of at compile time.

According to the polymorphism feature, different objects respond differently to the same
method call based on their implementations. This behavior is achieved through method
overriding, where a subclass provides its implementation of a method defined in its
superclass.

The Python interpreter determines which is the appropriate method or attribute to invoke
based on the object's type or class hierarchy at runtime. This means that the specific
method or attribute to be called is determined dynamically, based on the actual type of
the object.

Example:- 
The following example illustrates dynamic binding in Python'''
class shape:
    def draw(self):
        print ("draw method")
        return
class circle(shape):
    def draw(self):
        print ("Draw a circle")
        return
class rectangle(shape):
    def draw(self):
        print ("Draw a rectangle")
        return
shapes = [circle(), rectangle()]
for shp in shapes:
    shp.draw()

''' As you can see, the draw() method is bound dynamically to the corresponding
implementation based on the object's type. This is how dynamic binding is implemented
in Python.'''

'''Duck Typing
Another concept closely related to dynamic binding is duck typing. Whether an object is
suitable for a particular use is determined by the presence of certain methods or attributes,
rather than its type. This allows for greater flexibility and code reuse in Python.

Duck typing allows objects of different types to be used interchangeably as long as they
have the required methods or attributes. The goal is to promote flexibility and code reuse.
It is a broader concept that emphasizes object behavior and interface rather than formal
types.

previously we have covered the example of duck typing

In duck typing, the focus is on the object's behavior rather than its explicit type,
allowing different types of objects to be used interchangeably as long as they exhibit the
required behavior.'''

'''------------------------------ Python - Dynamic Typing -------------------------------
One of the standout features of Python language is that it is a dynamically typed language.
The compiler-based languages C/C++, Java, etc. are statically typed. Let us try to
understand the difference between static typing and dynamic typing.

In a statically typed language, each variable and its data type must be declared before
assigning it a value. Any other type of value is not acceptable to the compiler, and it raises
a compile-time error.

Let us take the following snippet of a Java program
public class MyClass {
    public static void main(String args[]) {
        int var;
        var="Hello";
        System.out.println("Value of var = " + var);
    }
}
Here, var is declared as an integer variable. When we try to assign it a string value, the
compiler gives the following error message −

/MyClass.java:4: error: incompatible types: String cannot be converted to int
x="Hello";
^
1 error
'''

''' Why Python is Called Dynamically Typed?
A variable in Python is only a label, or reference to the object stored in the memory, and
not a named memory location. Hence, the prior declaration of type is not needed. Because
it's just a label, it can be put on another object, which may be of any type.

In Java, the type of the variable decides what it can store and what not. In Python, it is
the other way around. Here, the type of data (i.e. object) decides the type of the variable.
To begin with, let us store a string in the variable in check its type
Example:- 
----------------------
>>> var="Hello"
>>> print ("id of var is ", id(var))
id of var is 2822590451184
>>> print ("type of var is ", type(var))
type of var is <class 'str'>
---------------------
So, var is of string type. However, it is not permanently bound. It's just a label; and can
be assigned to any other type of object, say a float, which will be stored with a different
id()
Example:- 
--------------------
>>> var=25.50
>>> print ("id of var is ", id(var))
id of var is 2822589562256
>>> print ("type of var is ", type(var))
type of var is <class 'float'>
---------------------
or a tuple. The var label now sits on a different object.
>> var=(10,20,30)
We can see that the type of var changes every time it refers to a new object. That's why
Python is a dynamically typed language.

Dynamic typing feature of Python makes it flexible compared to C/C++ and Java.
However, it is prone to runtime errors, so the programmer has to be careful.
'''

'''------------------------------------ Python - Abstraction -------------------------
Abstraction is one of the important principles of object-oriented programming. It refers to
a programming approach by which only the relevant data about an object is exposed,
hiding all the other details. This approach helps in reducing the complexity and increasing
the efficiency of application development.'''

''' Types of Python Abstraction
There are two types of abstraction. One is data abstraction, wherein the original data
entity is hidden via a data structure that can internally work through the hidden data
entities. Another type is called process abstraction. It refers to hiding the underlying
implementation details of a process.
'''

'''Python Abstract Class
In object-oriented programming terminology, a class is said to be an abstract class if it
cannot be instantiated, that is you can have an object of an abstract class. You can
however use it as a base or parent class for constructing other classes.
'''

'''Create an Abstract Class
To create an abstract class in Python, it must inherit the ABC class that is defined in the
ABC module. This module is available in Python's standard library. Moreover, the class
must have at least one abstract method. Again, an abstract method is the one which
cannot be called but can be overridden. You need to decorate it with @abstractmethod
decorator.
Example: Create an Abstract Class
'''
from abc import ABC, abstractmethod
class demo(ABC):
    @abstractmethod
    def method1(self):
        print ("abstract method")
        return
    def method2(self):
        print ("concrete method")

''' The demo class inherits ABC class. There is a method1() which is an abstract method.
Note that the class may have other non-abstract (concrete) methods.
If you try to declare an object of demo class (obj = demo()), Python raises TypeErro'''

''' The demo class here may be used as parent for another class. However, the child class
must override the abstract method in parent class. If not, Python throws this error −
TypeError: Can't instantiate abstract class concreteclass with abstract method
method1

Abstract Method Overriding
Hence, the child class with the abstract method overridden is given in the following
example'''
from abc import ABC, abstractmethod
class democlass(ABC):
    @abstractmethod
    def method1(self):
        print ("abstract method")
        return
    def method2(self):
        print ("concrete method")
class concreteclass(democlass):
    def method1(self):
        super().method1()
        return
obj = concreteclass()
obj.method1()
obj.method2()

'''----------------------------------------- Python - Encapsulation ----------------------------
Encapsulation is the process of bundling attributes and methods within a single unit

According to the principle of data encapsulation, the data members that describe an object
are hidden from the environment external to the class. They can only be accessed through
the methods within the same class. Methods themselves on the other hand are accessible
from outside class context. Hence, object data is said to be encapsulated by the methods.
In this way, encapsulation prevents direct access to the object data.'''

''' Implementing Encapsulation in Python
Languages such as C++ and Java use access modifiers to restrict access to class members
(i.e., variables and methods). These languages have keywords public, protected, and
private to specify the type of access.

Unlike these languages, Python has no provision to specify the type of access that a class
member may have. By default, all the variables and methods in a Python class are public,
as demonstrated by the following example.

Example 1
Here, we have an Employee class with instance variables, name and age. An object of this
class has these two attributes. They can be directly accessed from outside the class,
because they are public.'''

class Student:
    def __init__(self, name="Rajaram", marks=50):
        self.name = name
        self.marks = marks

s1 = Student()
s2 = Student("Bharat", 25)
print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))

''' In Python, prefixing name of a variable/method
with a single or double underscore to emulate the behavior of protected and private access
modifiers.
If a variable is prefixed by a double underscore (such as "__age"), the instance variable
is private. Similarly if a variable name is prefixed with a single underscore (such as
"_salary"), it becomes a private variable.

Example 2
Let us modify the Student class. Add another instance variable salary. Make name private
and marks as private by prefixing double underscores to them'''
class Student:
    def __init__(self, name="Rajaram", marks=50):
        self.__name = name
        self.__marks = marks
def studentdata(self):
    print ("Name: {} marks: {}".format(self.__name, self.__marks))
s1 = Student()
s2 = Student("Bharat", 25)
s1.studentdata()
s2.studentdata()
print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
print ("Name: {} marks: {}".format(s2.__name, s2.__marks))

''' What is Name Mangling?
Python doesn't block access to private data entirely. It just leaves it to the wisdom of the
programmer, not to write any code that accesses it from outside the class. You can still
access the private members by Python's name mangling technique.

In our example above , the private instance variable "__name" is mangled by changing it to the
format:- 
    obj._class__privatevar
which is 
    "print (s1._Student__marks)"
'''

'''------------------------------------------ Python - Interfaces -------------------------
In software engineering, an interface is a software architectural pattern. It is similar to a
class but its methods just have prototype signature definition without any executable code
or implementation body. The required functionality must be implemented by the methods
of any class that inherits the interface.
The method defined without any executable code is known as abstract method'''

''' Interfaces in Python
In languages like Java and Go, there is keyword called interface which is used to define
an interface. Python doesn't have it or any similar keyword. It uses abstract base classes
(in short ABC module) and @abstractmethod decorator to create interfaces.

NOTE: In Python, abstract classes are also created using ABC module.

An abstract class and interface appear similar in Python. The only difference in two is that
the abstract class may have some non-abstract methods, while all methods in interface
must be abstract, and the implementing class must override all the abstract methods.'''

''' Rules for implementing Python Interfaces
We need to consider the following points while creating and implementing interfaces in
Python −
     Methods defined inside an interface must be abstract.
     Creating object of an interface is not allowed.
     A class implementing an interface needs to define all the methods of that interface.
     In case, a class is not implementing all the methods defined inside the interface,
        the class must be declared abstract. '''

''' Ways to implement Interfaces in Python
We can create and implement interfaces in two ways −
     Formal Interface
     Informal Interface
'''

''' Formal Interface
Formal interfaces in Python are implemented using abstract base class (ABC). To use this
class, you need to import it from the abc module.

Example
In this example, we are creating a formal interface with two abstract methods'''

from abc import ABC, abstractmethod
# creating interface
class demoInterface(ABC):
    @abstractmethod
    def method1(self):
        print ("Abstract method1")
        return
    @abstractmethod
    def method2(self):
        print ("Abstract method1")
        return
''' Let us provide a class that implements both the abstract methods'''    
# class implementing the above interface
class concreteclass(demoInterface):
    def method1(self):
        print ("This is method1")
        return
    def method2(self):
        print ("This is method2")
        return
# creating instance
obj = concreteclass()
# method call
obj.method1()
obj.method2()

''' Informal Interface
In Python, the informal interface refers to a class with methods that can be overridden.
However, the compiler cannot strictly enforce the implementation of all the provided
methods. This type of interface works on the principle of duck typing. It allows us to call any method
on an object without checking its type, as long as the method exists.

Example
In the below example, we are demonstrating the concept of informal interface'''

class demoInterface:
    def displayMsg(self):
        pass
class newClass(demoInterface):
    def displayMsg(self):
        print ("This is my message")
# creating instance
obj = newClass()
# method call
obj.displayMsg()