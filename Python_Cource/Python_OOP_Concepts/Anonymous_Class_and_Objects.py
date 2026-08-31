'''---------------------------- 140. Python - Anonymous Class and Objects ------------------------------
Python's built-in type() function returns the class that an object belongs to. In Python, a
class, both a built-in class or a user-defined class are objects of type class.
Example:- '''
class myclass:
    def __init__(self):
        self.myvar=10
        return
obj = myclass()
print ('class of int', type(int))
print ('class of list', type(list))
print ('class of dict', type(dict))
print ('class of myclass', type(myclass))
print ('class of obj', type(obj))

''' The type() has a three argument version as follows −
Syntax:-  newclass=type(name, bases, dict)
Using above syntax, a class can be dynamically created. Three arguments of type function
are −
     name − name of the class which becomes __name__ attribute of new class
     bases − tuple consisting of parent classes. Can be blank if not a derived class
     dict − dictionary forming namespace of the new class containing attributes and
    methods and their values.'''

''' Create an Anonymous Class
We can create an anonymous class with the above version of type() function. The name
argument is a null string, second argument is a tuple of the object class (note that each
class in Python is inherited from object class). We add certain instance variables as the
third argument dictionary. We keep it empty for now.
anon=type('', (object, ), {})'''

''' Create an Anonymous Object
To create an object of this anonymous class −
-------------------------
obj = anon()
print ("type of obj:", type(obj))
-------------------------
The result shows that the object is of anonymous class
type of obj: <class '__main__.'>'''

''' Anonymous Class and Object Example
We can also add instance variables and instance methods dynamically. Take a look at this
example:- '''
def getA(self):
    return self.a
obj = type('',(object,),{'a':5,'b':6,'c':7,'getA':getA,'getB':lambda self :
self.b})()
print (obj.getA(), obj.getB())