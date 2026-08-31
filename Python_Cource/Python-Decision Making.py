def weekday(n):
    match n:
        case 0: return "Monday"
        case 1: return "Tuesday"
        case 2: return "Wednesday"
        case 3: return "Thursday"
        case 4: return "Friday"
        case 5: return "Saturday"
        case 6: return "Sunday"
        case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))

#-----------------------------------------------------------------------
def access(user):
    match user:
        case "admin" | "manager": return "Full access"
        case "Guest": return "Limited access"
        case _: return "No access"
print (access("manager"))
print (access("Guest"))
print (access("Ravi"))
#-----------------------------------------------------------------------
# List as the Argument in Match Case Statement
'''
Since Python can match the expression against any literal, you can use a list as a case
value. Moreover, for variable number of items in the list, they can be parsed to a sequence
with "*" operator.
Example
In this code, we use list as argument in match case statement
'''
def greeting(details):
    match details:
        case [time, name]:
            return f'Good {time} {name}!'
        case [time, *names]:
            msg=''
            for name in names:
                msg+=f'Good {time} {name}!\n'
            return msg
print (greeting(["Morning", "Ravi"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "Kajal", "Praveen", "Lata"]))

#-----------------------------------------------------------------------
# Using "if" in "Case" Clause
'''
Normally Python matches an expression against literal cases. However, it allows you to
include if statement in the case clause for conditional computation of match variable.
Example
In the following example, the function argument is a list of amount and duration, and the
intereset is to be calculated for amount less than or more than 10000. The condition is
included in the case clause.
'''
def intr(details):
    match details:
        case [amt, duration] if amt<10000:
            return amt*10*duration/100
        case [amt, duration] if amt>=10000:
            return amt*15*duration/100
print ("Interest = ", intr([5000,5]))
print ("Interest = ", intr([15000,3]))

#--------- Python Loop Control Statements ---------------
''''
Let us go through the loop control statements briefly
Sr.No.  Control Statement & Description
1       break statement
        Terminates the loop statement and transfers execution to the
        statement immediately following the loop.
2       continue statement
        Causes the loop to skip the remainder of its body and immediately
        retest its condition prior to reiterating.
3       pass statement
        The pass statement in Python is used when a statement is required
        syntactically but you do not want any command or code to
        execute.
'''

#----------- Python - For Loops ---------------
'''
for iterating_var in sequence:
statement(s)

Here, the iterating_var is a variable to which the value of each sequence item will be
assigned during each iteration. Statements represents the block of code that you want to
execute repeatedly

Example
The following example compares each character and displays if it is not a vowel ('a', 'e',
'i', 'o', 'u').
'''
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
    if char not in 'aeiou':
        print (char, end='')

''' For loop with Tuple'''
numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
    total += num
    print ("Total =", total)

''' For loop with List'''
numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
    if num%2 == 0:
        print (num)

''' Python for Loop with Range Objects
 Syntax
The range() function has the following syntax- 
range(start, stop, step)
Where,
     Start − Starting value of the range. Optional. Default is 0
     Stop − The range goes upto stop-1
     Step − Integers in the range increment by the step value. The default is 1.
'''       
for num in range(5):
    print (num, end=' ')
print()
for num in range(10, 20):
    print (num, end=' ')
print()
for num in range(1, 10, 2):
    print (num, end=' ')

''' for Loop with Dictionaries'''
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
    print (x,":",numbers[x])
''' The items(), keys() and values() methods of dict class return the view objects dict_items,
dict_keys and dict_values respectively. These objects are iterators, and hence we can run
a for loop over them.
Example
'''
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.items():
    print (x)

'''The following example illustrates the combination of an else statement with a for
statement that searches for prime numbers from 10 to 20.'''
#For loop to iterate between 10 to 20
for num in range(10, 20):
    #For loop to iterate on the factors
    for i in range(2,num):
        #If statement to determine the first factor
        if num%i == 0:
            #To calculate the second factor
            j=num/i
            print ("%d equals %d * %d" % (num,i,j))
            #To move to the next number
            break
        else:
            print (num, "is a prime number")
        break

#----------- Python for-else Loops ---------------
'''
Python supports an optional else block to be associated with a for loop. If a else block is
used with a for loop, it is executed only when the for loop terminates normally.
The for loop terminates normally when it completes all its iterations without encountering
a break statement, which allows us to exit the loop when a certain condition is met.

Following is the syntax of for loop with optional else block −
for variable_name in iterable:
#stmts in the loop
.
.
.
else:
#stmts in else clause
.
.
'''
''' Example : 
The following example illustrates the combination of an else statement with a for
statement in Python. Till the count is less than 5, the iteration count is printed. As it
becomes 5, the print statement in else block is executed, before the control is passed to
the next statement in the main program.'''
for count in range(6):
    print ("Iteration no. {}".format(count))
else:
    print ("for loop over. Now in else block")
print ("End of for loop")
''' In case of forceful termination (by using break statement) of the loop, else statement is
overlooked by the interpreter and hence its execution is skipped.'''
for i in ['T','P']:
    print(i)
    break
else:
    # Loop else statement
    # terminated after 1st iteration due to break statement in for loop
    print("Loop-else statement successfully executed")

''' Example :
Creating a function to check whether the list item is a positive or a negative number'''
def positive_or_negative():
    # traversing in a list
    for i in [5,6,7]:
        # checking whether the list element is greater than 0
        if i>=0:
            # printing positive number if it is greater than or equal to 0
            print ("Positive number")
        else:
            # Else printing Negative number and breaking the loop
            print ("Negative number")
            break
    # Else statement of the for loop
    else:
        # Statement inside the else block
        print ("Loop-else Executed")
        # Calling the above-created function
positive_or_negative()

#-------------- Python - While Loops ---------------
'''
Example 1
The following example illustrates the working of while loop. Here, the iteration run till value
of count will become 5
'''
while count<5:
    count+=1
    print ("Iteration no. {}".format(count))
print ("End of while loop")

'''
Example 2
Here is another example of using the while loop. For each iteration, the program asks for
user input and keeps repeating till the user inputs a non-numeric string. The isnumeric()
function returns true if input is an integer, false otherwise.
'''
var = '0'
while var.isnumeric() == True:
    var = "test"
    if var.isnumeric() == True:
        print ("Your input", var)
print ("End of while loop")

''' while-else Loop '''
count=0
while count<5:
    count+=1
    print ("Iteration no. {}".format(count))
else:
    print ("While loop over. Now in else block")
print ("End of while loop")

#------------- continue Statement ---------------
'''
Example:
'''
for letter in 'Python':
    if letter == 'h':
        continue
    print ('Current Letter :', letter)
print ("Good bye!")

'''
Example: Checking Prime Factors
Following code uses continue statement to find the prime factors of a given number. To
find prime factors, we need to successively divide the given number starting with 2,
increment the divisor and continue the same process till the input reduces to 1.
'''
num = 60
print ("Prime factors for: ", num)
d=2
while num > 1:
    if num%d==0:
        print (d)
        num=num/d
        continue
    d=d+1

#------------- Python - pass Statement and Ellipses (...) Statement---------------
'''
Python pass statement is used when a statement is required syntactically but you do not
want any command or code to execute. It is a null which means nothing happens when it
executes. This is also useful in places where piece of code will be added later, but a
placeholder is required to ensure the program runs without errors.

Example of pass Statement
The following code shows how you can use the pass statement in Python
'''
for letter in 'Python':
    if letter == 'h':
        pass
        print ('This is pass block')
    print ('Current Letter :', letter)
print ("Good bye!")
'''
This is simple enough to create an infinite loop using pass statement in Python
Example
'''
val = 30
if val > 10:
    while True: 
        pass
# Type Ctrl-C to stop

'''
Using Ellipses (...) as pass Statement Alternative
Python 3.X allows ellipses (coded as three consecutive dots ...) to be used in place of pass
statement. Both serve as placeholders for code that are going to be written later.
Example
'''

def func1():
    # Alternative to pass
    ...
# Works on same line too
def func2(): ...
# Does nothing if called
func1()
func2()
