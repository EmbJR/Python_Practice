''' Nested try Block in Python
In a Python program, if there is another try-except construct either inside either a try
block or inside its except block, it is known as a nested-try block. This is needed when
different blocks like outer and inner may cause different errors. To handle them, we need
nested try blocks.

We start with an example having a single "try − except − finally" construct. If the
statements inside try encounter exception, it is handled by except block. With or without
exception occurred, the finally block is always executed.

Example 1
Here, the try block has "division by 0" situation, hence the except block comes into play.
It is equipped to handle the generic exception with Exception class.'''

a=10
b=0
try:
    print (a/b)
except Exception:
    print ("General Exception")
finally:
    print ("inside outer finally block")

''' Example 2
Let us now see how to nest the try constructs. We put another "try − except − finally"
blocks inside the existing try block. The except keyword for inner try now handles generic
Exception, while we ask the except block of outer try to handle ZeroDivisionError.
Since exception doesn't occur in the inner try block, its corresponding generic Except isn't
called. The division by 0 situation is handled by outer except clause.  '''
a=10
b=0
try:
    print (a/b)
    try:
        print ("This is inner try block")
    except Exception:
        print ("General exception")
    finally:
        print ("inside inner finally block")
except ZeroDivisionError:
    print ("Division by 0")
finally:
    print ("inside outer finally block") 

''' Example 3
Now we reverse the situation. Out of the nested try blocks, the outer one doesn't have
any exception raised, but the statement causing division by 0 is inside inner try, and hence
the exception handled by inner except block. Obviously, the except part corresponding to
outer try: will not be called upon.'''
a=10
b=0
try:
    print ("This is outer try block")
    try:
        print (a/b)
    except ZeroDivisionError:
        print ("Division by 0")
    finally:
        print ("inside inner finally block")
except Exception:
    print ("General Exception")
finally:
    print ("inside outer finally block")  

''' In the end, let us discuss another situation which may occur in case of nested blocks.
While there isn't any exception in the outer try:, there isn't a suitable except block to
handle the one inside the inner try: block.

Example 4
In the following example, the inner try: faces "division by 0", but its corresponding except:
is looking for KeyError instead of ZeroDivisionError. Hence, the exception object is passed
on to the except: block of the subsequent except statement matching with outer try:
statement. There, the zeroDivisionError exception is trapped and handled.'''   
a=10
b=0
try:
    print ("This is outer try block")
    try:
        print (a/b)
    except KeyError:
        print ("Key Error")
    finally:
        print ("inside inner finally block")
except ZeroDivisionError:
    print ("Division by 0")
finally:
    print ("inside outer finally block")  