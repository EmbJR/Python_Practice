'''----------------------------- Python - Reflection ------------------------
In object-oriented programming, reflection refers to the ability to extract information
about any object in use. You can get to know the type of object, whether it is a subclass
of any other class, its attributes, and much more. Python's standard library has several
functions that reflect on different properties of an object. Reflection is also sometimes
called introspect.'''

'''Reflection Functions in Python
Following is the list of reflection functions in Python −
     type() Function
     isinstance() Function
     issubclass() Function
     callable() Function
     getattr() Function
     setattr() Function
     hasattr() Function
     dir() Function'''

''' The type() Function
We have used this function many times. It tells you which class an object belongs to.
Example
Following statements print the respective class of different built-in data type objects'''
print (type(10))
print (type(2.56))
print (type(2+3j))
print (type("Hello World"))
print (type([1,2,3]))
print (type({1:'one', 2:'two'}))

''' The isinstance() Function
This is another built-in function in Python which ascertains if an object is an instance of
the given class.
Syntax:- isinstance(obj, class)

This function always returns a Boolean value, true if the object is indeed belongs to the
given class and false if not

Example:-
Following statements return True − '''

print (isinstance(10, int))
print (isinstance(2.56, float))
print (isinstance(2+3j, complex))
print (isinstance("Hello World", str))
'''below functions should return false'''
print (isinstance([1,2,3], tuple))
print (isinstance({1:'one', 2:'two'}, set))

''' The issubclass() Function
This function checks whether a class is a subclass of another class. Pertains to classes, not
their instances.
As mentioned earlier, all Python classes are from the subclass of the object class. Hence,
output of following print statements is True for all'''
class test:
    pass
print (issubclass(int, object))
print (issubclass(str, object))
print (issubclass(test, object))

''' The callable() Function
An object is callable if it invokes a certain process. A Python function, which performs a
certain process, is a callable object. Hence callable(function) returns True. Any function,
built-in, user-defined, or method is callable. Objects of built-in data types such as int, str,
etc., are not callable
Example '''
def test():
    pass
print (callable("Hello"))
print (callable(abs))
print (callable(list.clear([1,2])))
print (callable(test))
''' A string object is not callable. But abs is a function which is callable. The pop method of
list is callable, but clear() is actually call to the function and not a function object, hence
not a callable'''

''' A class instance is callable if it has a __call__() method. In the example below, the test
class includes __call__() method. Hence, its object can be used as if we are calling
function. Hence, it is callable;
Examplke:- '''
class test:
    def __init__(self):
        pass
    def __call__(self):
        print ("Hello")
obj = test()
obj()
print ("obj is callable?", callable(obj))

''' The getattr() Function
The getattr() built-in function retrieves the value of the named attribute of object.
Example'''
class test:
    def __init__(self):
        self.name = "Manav"
obj = test()
print (getattr(obj, "name"))

''' The setattr() Function
The setattr() built-in function adds a new attribute to the object and assigns it a value. It
can also change the value of an existing attribute.
In the example below, the object of test class has a single attribute − name. We use
setattr() to add age attribute and to modify the value of name attribute.'''

class test:
    def __init__(self):
        self.name = "Manav"
obj = test()
setattr(obj, "age", 20)
setattr(obj, "name", "Madhav")
print (obj.name, obj.age)

''' The hasattr() Function
This built-in function returns True if the given attribute is available to the object argument,
and false if not. We use the same test class and check if it has a certain attribute or not.'''
class test:
    def __init__(self):
        self.name = "Manav"
obj = test()
print (hasattr(obj, "age"))
print (hasattr(obj, "name"))

''' The dir() Function
If this built-in function is called without an argument, it returns the names in the current
scope. For any object as an argument, it returns a list of the attributes of the given object
and attributes reachable from it.
     For a module object − the function returns the module's attributes.
     For a class object − the function returns its attributes, and recursively the
        attributes of its bases.
     For any other object − its attributes, its class's attributes, and recursively the
        attributes of its class's base classes.
Example
print ("dir(int):", dir(int))
print ("dir(dict):", dir(dict))'''