'''Python User Input Functions
Python provides us with two built-in functions to read the input from the keyboard.
    > The input () Function
    > The raw_input () Function
Python interpreter works in interactive and scripted mode. While the interactive mode is
good for quick evaluations, it is less productive. For repeated execution of same set of
instructions, scripted mode should be used

Following is the syntax of Python's standard library input() function.
var = input()
'''

name = input("Enter your name : ")
city = input("Enter your city : ")
print ("Hello My name is", name)
print ("I am from ", city)

'''
The raw_input() Function
The raw_input() function works similar to input() function. Here only point is that this
function was available in Python 2.7, and it has been renamed to input() in Python 3.6
'''

'''
width = input("Enter width : ")
height = input("Enter height : ")
area = width*height        # This will give error.
'''
w = input("Enter width : ")
width = int(w)
h = input("Enter height : ")
height = int(h)
area = width*height        # This will give error.
print ("Area of rectangle = ", area)
'''
Python Tutorial 154 Why do you get a TypeError here? The reason is, Python always read the user input as a
string. Hence, width="20" and height="30" are the strings and obviously you cannot
perform multiplication of two strings.
To overcome this problem, we shall use int(), another built-in function from Python's
standard library. It converts a string object to an integer.
'''
