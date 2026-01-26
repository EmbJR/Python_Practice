#---------- Nonlocal Variables -----------------
'''
The Python variables that are not defined in either local or global scope are called nonlocal
variables. They are used in nested functions.

Example
The following example demonstrates the how nonlocal variables works.
'''
def yourfunction():
    a = 5
    b = 6
    # nested function
    def myfunction():
        # nonlocal function
        nonlocal a
        nonlocal b
        a = 10
        b = 20
        print("variable a:", a)
        print("variable b:", b)
        return a+b
    print (myfunction())
yourfunction()

'''--------------- Namespace and Scope of Python Variables ----------------
A namespace is a collection of identifiers, such as variable names, function names, class
names, etc. In Python, namespace is used to manage the scope of variables and to prevent
naming conflicts.
Python provides the following types of namespaces −
     Built-in namespace contains built-in functions and built-in exceptions. They are loaded in the memory as soon as Python interpreter is loaded and remain till the
        interpreter is running.
     Global namespace contains any names defined in the main program. These names remain in memory till the program is running.
     Local namespace contains names defined inside a function. They are available till the function is running.
'''
'''---------------- Python globals() Function ----------------
Python's standard library includes a built-in function globals(). It returns a dictionary of
symbols currently available in global namespace.'''
print("------------------------ Python globals() Function ----------------")
print(globals())

'''---------------- Python locals() Function ----------------
Python locals() Function
Python's standard library includes a built-in function called locals(). It returns a dictionary
of symbols currently available in the local namespace of the function.

Example:-'''
name = 'TutorialsPoint'
marks = 50
result = True
def myfunction():
    a = 10
    b = 20
    c = a+b
    print("Global functions:\n")
    print ("globals():\n\n", globals())
    print("Local functions:\n")
    print ("locals():\n\n", locals())

    ''' Since both globals() and locals() functions return dictionary, you can access value of a
    variable from respective namespace with dictionary get() method or index operator
    '''
    print (globals()['name']) # displays TutorialsPoint
    print (locals().get('a')) # displays 10
    return c
myfunction()

'''----------------- Namespace Conflict in Python -----------------
If a variable of same name is present in global as well as local scope, Python interpreter
gives priority to the one in local namespace

If you try to manipulate value of a global variable from inside a function, Python raises
UnboundLocalError as shown in example below

Example:-
marks = 50
def myfunction():
    marks = marks + 20
    print (marks)
myfunction()
# prints global value
print (marks)
'''
''' To modify a global variable, you can either update it with a dictionary syntax, or use the
global keyword to refer it before modifying
Example:-
'''
var1 = 50 # this is a global variable
var2 = 60 # this is a global variable
def myfunction():
    "Change values of global variables"
    globals()['var1'] = globals()['var1']+10
    global var2
    var2 = var2 + 20
myfunction()
print ("var1:",var1, "var2:",var2) #shows global variables with changed values

'''
     Python makes educated guesses on whether variables are local or global. It
    assumes that any variable assigned a value in a function is local.

     In order to assign a value to a global variable within a function, you must first use
    the global statement.

     The statement global VarName tells Python that VarName is a global variable.
    Python stops searching the local namespace for the variable.

Example:- For example, we define a variable Money in the global namespace. Within the function
Money, we assign Money a value, therefore Python assumes Money as a local variable.
However, we accessed the value of the local variable Money before setting it, so an
UnboundLocalError is the result. Uncommenting the global statement fixes the problem.  
'''

Money = 2000
def AddMoney():
    # Uncomment the following line to fix the code:
    global Money    # Tell Python to use the global variable Money
    Money = Money + 1
print (Money)
AddMoney()
print (Money)
