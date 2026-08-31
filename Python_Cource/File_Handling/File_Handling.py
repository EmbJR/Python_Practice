'''----------------------------- Python - File Handling -------------------------
File Handling in Python
File handling in Python involves interacting with files on your computer to read data from
them or write data to them. Python provides several built-in functions and methods for
creating, opening, reading, writing, and closing files. 
This tutorial covers the basics of file handling in Python with examples.'''


''' Opening a File in Python
To perform any file operation, the first step is to open the file. Python's built-in open()
function is used to open files in various modes, such as reading, writing, and appending.
The syntax − file = open("filename", "mode")
                    
                    Where, filename is the name of the file to open and mode is the mode in which the file is
                    opened (e.g., 'r' for reading, 'w' for writing, 'a' for appending)'''

''' File Opening Modes
Following are the file opening modes −

#-------------------------------- [Python File Opening Modes] ----------------------------
Sr.No.           Mode                Description
----------------------------------------------------------------------
1                          r           Opens a file for reading only. The file pointer
                                    is placed at the beginning of the file. This is
                                    the default mode.
----------------------------------------------------------
2                          rb          Opens a file for reading only in binary format.
                                    The file pointer is placed at the beginning of
                                    the file. This is the default mode.
----------------------------------------------------------
3                          r+          Opens a file for both reading and writing.
                                    The file pointer is placed at the beginning
                                    of the file.
----------------------------------------------------------
4                          rb+         Opens a file for both reading and writing
                                    in binary format. The file pointer is placed
                                    at the beginning of the file.
----------------------------------------------------------
5                          w           Opens a file for writing only. Overwrites the
                                    file if the file exists. If the file does not
                                    exist, creates a new file for writing.
----------------------------------------------------------
6                          b           Opens the file in binary mode.
----------------------------------------------------------
7                          t           Opens the file in text mode (default).
----------------------------------------------------------
8                          +           Opens file for updating (reading and writing).
----------------------------------------------------------
9                          wb          Opens a file for writing only in binary format.
                                    Overwrites the file if the file exists. If the
                                    file does not exist, creates a new file for
                                    writing.
----------------------------------------------------------
10                         w+          Opens a file for both writing and reading.
                                    Overwrites the existing file if the file exists.
                                    If the file does not exist, creates a new file
                                    for reading and writing.
----------------------------------------------------------
11                         wb+         Opens a file for both writing and reading
                                    in binary format. Overwrites the existing file
                                    if the file exists. If the file does not exist,
                                    creates a new file for reading and writing.
----------------------------------------------------------
12                         a           Opens a file for appending. The file pointer
                                    is at the end of the file if the file exists.
                                    The file is in the append mode. If the file
                                    does not exist, it creates a new file for
                                    writing.
----------------------------------------------------------
13                         ab          Opens a file for appending in binary format.
                                    The file pointer is at the end of the file if
                                    the file exists. The file is in the append mode.
                                    If the file does not exist, it creates a new
                                    file for writing.
----------------------------------------------------------
14                         a+          Opens a file for both appending and reading.
                                    The file pointer is at the end of the file if
                                    the file exists. The file opens in the append
                                    mode. If the file does not exist, it creates
                                    a new file for reading and writing.
----------------------------------------------------------
15                         ab+         Opens a file for both appending and reading
                                    in binary format. The file pointer is at the
                                    end of the file if the file exists. The file
                                    opens in the append mode. If the file does
                                    not exist, it creates a new file for reading
                                    and writing.
----------------------------------------------------------
16                         x           Opens for exclusive creation, failing if the
                                    file already exists.
----------------------------------------------------------
Once a file is opened and you have one file object, you can get various information related
to that file.
Example 1
In the following example, we are opening a file in different modes'''
# Opening a file in read mode
file = open("example.txt", "r")
# Opening a file in write mode
file = open("example.txt", "w")
# Opening a file in append mode
file = open("example.txt", "a")
# Opening a file in binary read mode
file = open("example.txt", "rb")

''' Example 2
Here, we are opening a file named "foo.txt" in binary write mode ("wb"), printing its name,
whether it's closed, and its opening mode, and then closing the file'''
# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close()

''' Reading a File in Python
Reading a file in Python involves opening the file in a mode that allows for reading, and
then using various methods to extract the data from the file. Python provides several
methods to read data from a file −
     read() − Reads the entire file.
     readline() − Reads one line at a time.
     readlines − Reads all lines into a list.
To read a file, you need to open it in read mode. The default mode for the
open() function is read mode ('r'), but it's good practice to specify it
explicitly-
Example: Using read() method
In the following example, we are using the read() method to read the whole file into a
single string −'''

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
'''Example: Using readline() method
In here, we are using the readline() method to read one line at a time, making it memory
efficient for reading large files line by line'''
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

''' Example: Using readlines() method
Now, we are using the readlines() method to read the entire file and split it into a list
where each element is a line'''

with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines: 
        print(line, end='')

''' Writing to a File in Python
Writing to a file in Python involves opening the file in a mode that allows writing, and then
using various methods to add content to the file.
To write data to a file, use the write() or writelines() methods. When opening a file in write
mode ('w'), the file's existing content is erased.

Example: Using the write() method
In this example, we are using the write() method to write the string passed to it to the
file. If the file is opened in 'w' mode, it will overwrite any existing content. If the file is
opened in 'a' mode, it will append the string to the end of the file '''
with open("foo.txt", "w") as file:
    file.write("Hello, World!")
    print ("Content added Successfully!!")

''' Example: Using the writelines() method
In here, we are using the writelines() method to take a list of strings and writes each string
to the file. It is useful for writing multiple lines at once'''
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)
    print ("Content added Successfully!!")

''' Closing a File in Python
We can close a file in Python using the close() method. Closing a file is an essential step
in file handling to ensure that all resources used by the file are properly released. It is
important to close files after operations are completed to prevent data loss and free up
system resources.

Example
In this example, we open the file for writing, write data to the file, and then close the file
using the close() method'''
file = open("example.txt", "w")
file.write("This is an example.")
file.close()
print ("File closed successfully!!")

''' Using "with" Statement for Automatic File Closing
The with statement is a best practice in Python for file operations because it ensures that
the file is automatically closed when the block of code is exited, even if an exception
occurs.

Example
In this example, the file is automatically closed at the end of the with block, so there is no
need to call close() method explicitly'''

with open("example.txt", "w") as file:
    file.write("This is an example using the with statement.")
    print ("File closed successfully!!")

''' Handling Exceptions when closing a File
When performing file operations, it is important to handle potential exceptions to ensure
your program can manage errors gracefully.
In Python, we use a try-finally block to handle exceptions when closing a file. The "finally"
block ensures that the file is closed regardless of whether an error occurs in the try block'''

try:
    file = open("example.txt", "w")
    file.write("This is an example with exception handling.")
finally:
    file.close()
    print ("File closed successfully!!")
        
'''-------------------------------- Python - Write to File ------------------------------------
Writing to a file involves opening the file in a specific mode, writing data to it, and then
closing the file to ensure that all data is saved and resources are released. Python provides
a built-in function open() to handle file operations and various methods for writing data.'''


''' Opening a File for Writing
Opening a file for writing is the first step in performing write operations in Python. The
open() function is used to open files in different modes, each suited for specific use cases.
'''

''' The open() Function
The open() function in Python is used to open a file. It requires at least one argument, the
name of the file, and can take an optional second argument that specifies the mode in
which the file should be opened.'''

''' File Modes for Writing
Following are the main modes you can use to open a file for writing −
     w (Write mode) − Opens the file for writing. If the file exists, it truncates
        (empties) the file before writing. If the file does not exist, it creates a new file.
     a (Append Mode) − Data is written at the end of the file. If the file does not exist,
        it creates a new file.
     x (Exclusive Creation Mode) − Opens the file for exclusive creation. If the file
        already exists, the operation fails.
     b (Binary Mode) − When used with other modes, opens the file in binary mode.
     + (Update Mode) − Opens the file for updating (reading and writing).

Example: Opening a File in Write Mode
This mode is used when you want to write data to a file, starting from scratch each time
the file is opened'''
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()
print ("File opened successfully!!")

''' Example: Opening a File in Append Mode
This mode is used when you want to add data to the end of the file without altering its
existing contents'''

file = open("example.txt", "a")
file.write("Appending this line.\n")
file.close()
print ("File opened successfully!!")

''' Writing to a File Using write() Method
The write() method is used to write a single string to a file. This makes it suitable for
various text-based file operations.
The write() method takes a single argument: the string that you want to write to the file.
It writes the exact content of the string to the file without adding any additional characters,
such as newlines.

Example
In the following example, we are opening the file "example.txt" in write mode. We then
use the write() method to write a string to the file −'''
# Open a file in write mode
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
print ("File opened successfully!!")

''' Writing to a File Using writelines() Method
The writelines() method is used to write a list of strings to a file. Each string in the list is
written to the file sequentially without adding any newline characters automatically.

Example
In this example, we are creating a list of strings, lines, with each string ending in a newline
character. We then open a file "example.txt" in write mode and use the writelines() method
to write all the strings in the list to the file in one operation'''

# List of lines to write to the file
lines = ["First line\n", "Second line\n", "Third line\n"]
# Open a file in write mode
with open("example.txt", "w") as file:
    file.writelines(lines)
print ("File opened successfully!!")

''' Writing to a New File
Writing to a new file in Python involves creating a new file (or overwriting an existing one)
and writing the desired content to it. Here, we will explain the steps involved in writing to
a new file −
     Open the File − Use the open() function to create or open a file in write mode
        ("w" or "wb" for binary files).
     Write Data − Use the write() or writelines() method to write data to the file.
     Close the File − Ensure the file is properly closed after writing, generally using
        the "with" statement for automatic handling.
Example
In the example below, we create a "foo.txt" file and write given content in that file and
finally close that file'''

# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
# Close opened file
fo.close()

''' Writing to a New File in Binary Mode
By default, read/write operations on a file object are performed on text string data. If we
need to handle files of different types, such as media files (mp3), executables (exe), or
pictures (jpg), we must open the file in binary mode by adding the 'b' prefix to the
read/write mode.
Writing Binary Data to a File
To write binary data to a file, open the file in binary write mode ('wb'). The following
example demonstrates this'''

# Open a file in binary write mode
with open('test.bin', 'wb') as f:
    # Binary data
    data = b"Hello World"
f.write(data)

''' Converting Text Strings to Bytes
Conversion of a text string to bytes can be done using the encode() function. This is useful
when you need to write text data as binary data '''

# Open a file in binary write mode
with open('test.bin', 'wb') as f:
    # Convert text string to bytes
    data = "Hello World".encode('utf-8')
    f.write(data)

''' Writing to an Existing File
When an existing file is opened in write mode ('w'), its previous contents are erased.
Opening a file with write permission treats it as a new file. To add data to an existing file
without erasing its contents, you should open the file in append mode ('a').

Example
The following example demonstrates how to open a file in append mode and add new text
to it '''

# Open a file in append mode
fo = open("foo.txt", "a")
text = "TutorialsPoint has a fabulous Python tutorial"
fo.write(text)
# Close opened file
fo.close()

''' Writing to a File in Reading and Writing Modes
When a file is opened for writing using 'w' or 'a', it is not possible to perform write
operations at any earlier byte position in the file. The 'w+' mode, however, allows both
reading and writing operations without closing the file. The seek() function is used to move
the read/write pointer to any desired byte position within the file.
Using the seek() Method
The seek() method is used to set the position of the read/write pointer within the file. 

The syntax for the seek() method is as follows −
    fileObject.seek(offset[, whence])
Where,
     offset − This is the position of the read/write pointer within the file.
     whence − This is optional and defaults to 0 which means absolute file positioning,
        other values are 1 which means seek relative to the current position and 2 means
        seek relative to the file's end
    
Example
The following program demonstrates how to open a file in read-write mode ('w+'), write
some data, seek a specific position, and then overwrite part of the file's conten'''
# Open a file in read-write mode
fo = open("foo.txt", "w+")
# Write initial data to the file
fo.write("This is a rat race")
# Move the read/write pointer to the 10th byte
fo.seek(10, 0)
# Read 3 bytes from the current position
data = fo.read(3)
# Move the read/write pointer back to the 10th byte
fo.seek(10, 0)
# Overwrite the existing content with new text
fo.write('cat')
# Close the file
fo.close()

''' If we open the file in read mode (or seek to the starting position while in 'w+' mode) and
read the contents, it will show the following −
>> This is a cat race'''

'''-------------------------------------- Python - Read Files --------------------------------
Reading from a file involves opening the file, reading its contents, and then closing the file
to free up system resources. Python provides several methods to read from a file, each
suited for different use cases.'''

''' Opening a File for Reading
Opening a file is the first step in reading its contents. In Python, you use the open()
function to open a file. This function requires at least one argument, the filename, and
optionally a mode that specifies the purpose of opening the file.

To open a file for reading, you use the mode 'r'. This is the default mode, so you can omit
it if you only need to read from the file.

Reading a File using read() Method
The read() method is used to read the contents of a file in Python. It reads the entire
content of the file as a single string. This method is particularly useful when you need to
process the whole file at once.
Syntax:- file_object.read(size)
        Where,
         file_object is the file object returned by the open() function.
         size is the number of bytes to read from the file. This parameter is optional. If
            omitted or set to a negative value, the method reads until the end of the file.
Example
In the following example, we are opening the file "example.txt" in read mode. We then
use the read() method to read the entire content of the file'''
# Open the file in read mode
file = open('example.txt', 'r')
# Read the entire content of the file
content = file.read()
# Print the content
print(content)
# Close the file
file.close()
''' After executing the above code, we get the following output −
>> welcome to Tutorialspoint.'''

''' Reading a File Using readline() Method
The readline() method is used to read one line from a file at a time. This method is useful
when you need to process a file line by line, especially for large files where reading the
entire content at once is not practical.
Syntax Following is the basic syntax of the readline() method in Python −
    file_object.readline(size)
Where,
     file_object is the file object returned by the open() function.
     size is an optional parameter specifying the maximum number of bytes to read
        from the line. If omitted or set to a negative value, the method reads until the end
        of the line
Example
In the example below, we are opening the file "example.txt" in read mode. We then use
the readline() method to read the first line of the file'''
# Open the file in read mode
file = open('example.txt', 'r')
# Read the first line of the file
line = file.readline()
# Print the line
print(line)
# Close the file
file.close()
''' Following is the output of the above code −
>> welcome to Tutorialspoint.'''

''' Reading a File Using readlines() Method
The readlines() method reads all the lines from a file and returns them as a list of strings.
Each string in the list represents a single line from the file, including the newline character
at the end of each line.
This method is particularly useful when you need to process or analyse all lines of a file at
once.

Syntax Following is the basic syntax of the readlines() method in Python −
    file_object.readlines(hint)
Where,
     file_object is the file object returned by the open() function.
     hint is an optional parameter that specifies the number of bytes to read. If
        specified, it reads lines up to the specified bytes, not necessarily reading the entire
        file.
Example
In this example, we are opening the file "example.txt" in read mode. We then use the
readlines() method to read all the lines from the file and return them as a list of strings −'''
# Open the file in read mode
file = open('example.txt', 'r')
# Read all lines from the file
lines = file.readlines()
# Print the lines
for line in lines:
print(line, end='')
# Close the file
file.close()
'''Output of the above code is as shown below −
>> welcome to Tutorialspoint.
>> Hi Surya.
>> How are you?.'''

''' Using "with" Statement
The "with" statement in Python is used for exception handling. When dealing with files,
using the "with" statement ensures that the file is properly closed after reading, even if an
exception occurs.
When you use a with statement to open a file, the file is automatically closed
at the end of the block, even if an error occurs within the block.
Example
Following is a simple example of using the with statement to open, read, and print the
contents of a file'''
# Using the with statement to open a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

''' Reading/Writing to a Binary File
Assuming that the test.bin file has already been written in binary mode'''
# Open the file in binary write mode
with open('test.bin', 'wb') as f:
    data = b"Hello World"
    f.write(data)
'''Example
To read a binary file, we need to open it in 'rb' mode. The returned value of the read()
method is then decoded before printing'''
# Open the file in binary read mode
with open('test.bin', 'rb') as f:
    data = f.read()
    print(data.decode(encoding='utf-8'))

''' Reading Integer Data from a File
To write integer data to a binary file, the integer object should be converted to bytes using
the to_bytes() method.
Writing an Integer to a Binary File
Following is an example on how to write an integer to a binary file'''

# Convert the integer to bytes and write to a binary file
n = 25
data = n.to_bytes(8, 'big')
with open('test.bin', 'wb') as f:
    f.write(data)

''' Reading an Integer from a Binary File
To read back the integer data from the binary file, convert the output of the read() function
back to an integer using the from_bytes() method'''
# Read the binary data from the file and convert it back to an integer
with open('test.bin', 'rb') as f:
    data = f.read()
    n = int.from_bytes(data, 'big')
    print(n)

''' Reading Float Data from a File
For handling floating-point data in binary files, we need to use the struct module from
Python's standard library. This module helps convert between Python values and C structs
represented as Python bytes objects.

Writing a Float to a Binary File
To write floating-point data to a binary file, we use the struct.pack() method to convert
the float into a bytes object'''
import struct
# Define a floating-point number
x = 23.50
# Pack the float into a binary format
data = struct.pack('f', x)
# Open the file in binary write mode and write the packed data
with open('test.bin', 'wb') as f:
    f.write(data)

''' Reading Float Numbers from a Binary File
To read floating-point data from a binary file, we use the struct.unpack() method to
convert the bytes object back into a float'''

import struct
# Open the file in binary read mode
with open('test.bin', 'rb') as f:
    # Read the binary data from the file
    data = f.read()
    # Unpack the binary data to retrieve the float
    x = struct.unpack('f', data)[0]
    # Print the float value
    print(x)

''' Reading and Writing to a File Using "r+" Mode
When a file is opened for reading (with 'r' or 'rb'), writing data is not possible unless the
file is closed and reopened in a different mode. 
To perform both read and write operations simultaneously, we add the '+' character to the mode 
parameter. Using 'w+' or 'r+' mode enables using both write() and read() methods without closing 
the file.
The File object also supports the seek() function, which allows repositioning the read/write
pointer to any desired byte position within the file.
Example
The following program opens a file in 'r+' mode (read-write mode), seeks a certain position
in the file, and reads data from that position
'''

# Open the file in read-write mode
with open("foo.txt", "r+") as fo:
    # Move the read/write pointer to the 10th byte position
    fo.seek(10, 0)
    # Read 3 bytes from the current position
    data = fo.read(3)
    # Print the read data
    print(data)
''' After executing the above code, we get the following output −
>> rat'''

''' Reading and Writing to a File Simultaneously in Python
When a file is opened for writing (with 'w' or 'a'), it is not possible to read from it, and
attempting to do so will throw an UnsupportedOperation error.

Similarly, when a file is opened for reading (with 'r' or 'rb'), writing to it is not allowed. To
switch between reading and writing, you would typically need to close the file and reopen
it in the desired mode.

To perform both read and write operations simultaneously, you can add the '+' character
to the mode parameter. Using 'w+' or 'r+' mode enables both write() and read() methods
without needing to close the file.

Additionally, the File object supports the seek() function, which allows you to reposition
the read/write pointer to any desired byte position within the file.

Example
In this example, we open the file in 'r+' mode and write data to the file. The seek(0)
method repositions the pointer to the beginning of the file −'''

# Open the file in read-write mode
with open("foo.txt", "r+") as fo:
    # Write data to the file
    fo.write("This is a rat race")
    # Rewind the pointer to the beginning of the file
    fo.seek(0)
    # Read data from the file
    data = fo.read()
    print(data)

''' Reading a File from Specific Offset
We can set the he file's current position at the specified offset using the seek() method.
     If the file is opened for appending using either 'a' or 'a+', any seek() operations
        will be undone at the next write.
     If the file is opened only for writing in append mode using 'a', this method is
        essentially a no-op, but it remains useful for files opened in append mode with
        reading enabled (mode 'a+').
     If the file is opened in text mode using 't', only offsets returned by tell() are legal.
        Use of other offsets causes undefined behavior.
Note that not all file objects are seekable. For example, on Windows, files opened in text

Example:- The following example demonstrates how to use the seek() method to perform
simultaneous read/write operations on a file. The file is opened in w+ mode (read-write
mode), some data is added, and then the file is read and modified at a specific position'''

# Open a file in read-write mode
fo = open("foo.txt", "w+")
# Write initial data to the file
fo.write("This is a rat race")
# Seek to a specific position in the file
fo.seek(10, 0)
# Read a few bytes from the current position
data = fo.read(3)
print("Data read from position 10:", data)
# Seek back to the same position
fo.seek(10, 0)
# Overwrite the earlier contents with new text
fo.write("cat")
# Rewind to the beginning of the file
fo.seek(0, 0)
# Read the entire file content
data = fo.read()
print("Updated file content:", data)
# Close the file
fo.close()

''' Following is the output of the above code −
>> Data read from position 10: rat
>> Updated file content: This is a cat race'''

'''-------------------------------------------------------- Python - Renaming and Deleting Files ----------------------------------------
> Renaming and Deleting Files in Python
In Python, you can rename and delete files using built-in functions from the os module.
These operations are important when managing files within a file system. In this tutorial,
we will explore how to perform these actions step-by-step.

> Renaming Files in Python
To rename a file in Python, you can use the os.rename() function. This function takes two
arguments: the current filename and the new filename.
Syntax:- Following is the basic syntax of the rename() function in Python −
    os.rename(current_file_name, new_file_name)
Parameters
     current_file_name − It is the current name of the file you want to rename.
     new_file_name − It is the new name you want to assign to the file.
Example:- 
Following is an example to rename an existing file "oldfile.txt" to "newfile.txt" using the
rename() function'''
import os
# Current file name
current_name = "oldfile.txt"
# New file name
new_name = "newfile.txt"
# Rename the file
os.rename(current_name, new_name)
print(f"File '{current_name}' renamed to '{new_name}' successfully.")
'''Following is the output of the above code −
>> File 'oldfile.txt' renamed to 'newfile.txt' successfully.'''

''' Deleting Files in Python
You can delete a file in Python using the os.remove() function. This function deletes a file
specified by its filename.
Syntax:- Following is the basic syntax of the remove() function in Python −
    os.remove(file_name)
Parameters
    This function accepts the name of the file as a parameter which needs to be deleted.
Example
Following is an example to delete an existing file "file_to_delete.txt" using the remove()
function −'''
import os
# File to be deleted
file_to_delete = "file_to_delete.txt"
# Delete the file
os.remove(file_to_delete)
print(f"File '{file_to_delete}' deleted successfully.")
''' After executing the above code, we get the following output −
File 'file_to_delete.txt' deleted successfully.'''

'''--------------------------------------------- Python - Directories ------------------------------
Directories in Python
In Python, directories, commonly known as folders in operating systems, are locations on
the file system used to store files and other directories. They serve as a way to group and
manage files hierarchically.

Python provides several modules, primarily os and os.path, along with shutil, that allows
you to perform various operations on directories.

These operations include creating new directories, navigating through existing directories,
listing directory contents, changing the current working directory, and removing
directories.'''

''' Checking if a Directory Exists
Before performing operations on a directory, you often need to check if it exists. We can
check if a directory exists or not using the os.path.exists() function in Python.
This function accepts a single argument, which is a string representing a path in the
filesystem. This argument can be −
     Relative path − A path relative to the current working directory.
     Absolute path − A complete path starting from the root directory.
Example
In this example, we check whether the given directory path exists using the
os.path.exists() function −'''

import os
directory_path = "D:\\Test\\MyFolder\\"
if os.path.exists(directory_path):
    print(f"The directory '{directory_path}' exists.")
else:
    print(f"The directory '{directory_path}' does not exist.")
''' Following is the output of the above code −
The directory 'D:\\Test\\MyFolder\\' exists.'''

''' Creating a Directory
You create a new directory in Python using the os.makedirs() function. This function
>> creates intermediate directories if they do not exist.

The os.makedirs() function accepts a "path" you want to create as an argument. It
optionally accepts a "mode" argument that specifies the permissions o set for the newly
created directories. It is an integer, represented in octal format (e.g., 0o755). If not
specified, the default permissions are used based on your system's umask.
Example
In the following example, we are creating a new directory using the os.makedirs() function'''
import os
new_directory = "new_dir.txt"
try:
    os.makedirs(new_directory)
    print(f"Directory '{new_directory}' created successfully.")
except OSError as e:
    print(f"Error: Failed to create directory '{new_directory}'. {e}")

''' After executing the above code, we get the following output −
>> Directory 'new_dir.txt' created successfully.'''

''' The mkdir() Method
You can use the mkdir() method of the os module to create directories in the current
directory. You need to supply an argument to this method, which contains the name of
the directory to be created.
Following is the syntax of the mkdir() method in Python
    os.mkdir("newdir")
Example
    Following is an example to create a directory test in the current directory −'''
import os
# Create a directory "test"
os.mkdir("test")
print ("Directory created successfully")

''' Get Current Working Directory
To retrieve the current working directory in Python, you can use the os.getcwd() function.
This function returns a string representing the current working directory where the Python
script is executing.
Syntax
Following is the basic syntax of the getcwd() function in Python −
    os.getcwd()
Example:- 
Following is an example to display the current working directory using the getcwd()
function −'''
import os
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

''' Listing Files and Directories
You can list the contents of a directory using the os.listdir() function. This function returns
a list of all files and directories within the specified directory path.
Example
In the example below, we are listing the contents of the specified directory path using the
listdir() function'''
import os
directory_path = r"D:\MyFolder\Pictures"
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except OSError as e:
    print(f"Error: Failed to list contents of directory '{directory_path}'. {e}")
''' Output of the above code is as shown below −
>> Contents of 'D:\MyFolder\Pictures':
>> Camera Roll
>> desktop.ini
>> Saved Pictures
>> Screenshots'''

''' Changing the Current Working Directory
You can change the current directory using the chdir() method. This method takes an
argument, which is the name of the directory that you want to make the current directory.
Syntax
Following is the syntax of the chdir() method in Python −
    os.chdir("newdir")
Example
Following is an example to change the current directory to Desktop using the chdir()
method    '''
import os
new_directory = r"D:\MyFolder\Pictures"
try:
    os.chdir(new_directory)
    print(f"Current working directory changed to '{new_directory}'.")
except OSError as e:
    print(f"Error: Failed to change working directory to '{new_directory}'. {e}")
''' We get the output as shown below −
>> Current working directory changed to 'D:\MyFolder\Pictures'.''' 

''' Removing a Directory
You can remove an empty directory in Python using the os.rmdir() method. If the directory
contains files or other directories, you can use shutil.rmtree() method to delete it
recursively.
Syntax:- Following is the basic syntax to delete a directory in Python −
    os.rmdir(directory_path)
    # or
    shutil.rmtree(directory_path)
Example
In the following example, we remove an empty directory using the os.rmdir() method'''
import os
directory_path = r"D:\MyFolder\new_dir"
try:
    os.rmdir(directory_path)
    print(f"Directory '{directory_path}' successfully removed.")
except OSError as e:
    print(f"Error: Failed to remove directory '{directory_path}'. {e}")
''' It will produce the following output −
>> Directory 'D:\MyFolder\new_dir' successfully removed.'''

'''------------------------------------------- Python - File Methods ---------------------------------
A file object is created using open() function. The file class defines the following methods
with which different file IO operations can be done. The methods can be used with any file
like object such as byte stream or network stream.

Sr.No.    Methods & Description
----------------------------------------------------------------------
1         file.close()
          Close the file. A closed file cannot be read or written any more.
----------------------------------------------------------------------
2         file.flush()
          Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.
----------------------------------------------------------------------
3         file.fileno()
          Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.
----------------------------------------------------------------------
4         file.isatty()
          Returns True if the file is connected to a tty(-like) device, else False.
----------------------------------------------------------------------
5         file.next()
          Returns the next line from the file each time it is being called.
----------------------------------------------------------------------
6         file.read([size])
          Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes).
----------------------------------------------------------------------
7         file.readline([size])
          Reads one entire line from the file. A trailing newline character is kept in the string.
----------------------------------------------------------------------
8         file.readlines([sizehint])
          Reads until EOF using readline() and return a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.
----------------------------------------------------------------------
9         file.seek(offset[, whence])
          Sets the file's current position
----------------------------------------------------------------------
10        file.tell()
          Returns the file's current position
----------------------------------------------------------------------
11        file.truncate([size])
          Truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.
----------------------------------------------------------------------
12        file.write(str)
          Writes a string to the file. There is no return value.
----------------------------------------------------------------------
13        file.writelines(sequence)
          Writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings.
----------------------------------------------------------------------
'''

'''---------------------------------------------------- Python OS File/Directory Methods ----------------------------------
The OS module of Python provides a wide range of useful methods to manage files and
directories. These are the built-in methods that help in interacting with operating systems.
Most of the useful methods are listed here

Sr.No. Methods & Description
1 os.access(path, mode) - Use the real uid/gid to test for access to path.
2 os.chdir(path) - Change the current working directory to path
3 os.chflags(path, flags) - Set the flags of path to the numeric flags.
4 os.chmod(path, mode) - Change the mode of path to the numeric mode.
5 os.chown(path, uid, gid) - Change the owner and group id of path to the numeric uid and gid.
6 os.chroot(path) - Change the root directory of the current process to path.
7 os.close(fd) - Close file descriptor fd.
8 os.closerange(fd_low, fd_high) - Close all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring errors.
9 os.dup(fd) - Return a duplicate of file descriptor fd.
10 os.dup2(fd, fd2) - Duplicate file descriptor fd to fd2, closing the latter first if necessary.
11 os.fchdir(fd) - Change the current working directory to the directory represented by the file descriptor fd.
12 os.fchmod(fd, mode) - Change the mode of the file given by fd to the numeric mode.
13 os.fchown(fd, uid, gid) - Change the owner and group id of the file given by fd to the numeric uid and gid.
14 os.fdatasync(fd) - Force write of file with filedescriptor fd to disk.
15 os.fdopen(fd[, mode[, bufsize]]) - Return an open file object connected to the file descriptor fd.
16 os.fpathconf(fd, name) - Return system configuration information relevant to an open file. name specifies the configuration value to retrieve.
17 os.fstat(fd) - Return status for file descriptor fd, like stat().
18 os.fstatvfs(fd) - Return information about the filesystem containing the file associated with file descriptor fd, like statvfs().
19 os.fsync(fd) - Force write of file with filedescriptor fd to disk.
20 os.ftruncate(fd, length) - Truncate the file corresponding to file descriptor fd, so that it is at most length bytes in size.
21 os.getcwd() - Return a string representing the current working directory.
22 os.getcwdu() - Return a Unicode object representing the current working directory.
23 os.isatty(fd) - Return True if the file descriptor fd is open and connected to a tty(-like) device, else False.
24 os.lchflags(path, flags) - Set the flags of path to the numeric flags, like chflags(), but do not follow symbolic links.
25 os.lchmod(path, mode) - Change the mode of path to the numeric mode.
26 os.lchown(path, uid, gid) - Change the owner and group id of path to the numeric uid and gid. This function will not follow symbolic links.
27 os.link(src, dst) - Create a hard link pointing to src named dst.
28 os.listdir(path) - Return a list containing the names of the entries in the directory given by path.
29 os.lseek(fd, pos, how) - Set the current position of file descriptor fd to position pos, modified by how.
30 os.lstat(path) - Like stat(), but do not follow symbolic links.
31 os.major(device) - Extract the device major number from a raw device number.
32 os.makedev(major, minor) - Compose a raw device number from the major and minor device numbers.
33 os.makedirs(path[, mode]) - Recursive directory creation function.
34 os.minor(device) - Extract the device minor number from a raw device number.
35 os.mkdir(path[, mode]) - Create a directory named path with numeric mode mode.
36 os.mkfifo(path[, mode]) - Create a FIFO (a named pipe) named path with numeric mode mode. The default mode is 0666 (octal).
37 os.mknod(filename[, mode=0600, device]) - Create a filesystem node (file, device special file or named pipe) named filename.
38 os.open(file, flags[, mode]) - Open the file file and set various flags according to flags and possibly its mode according to mode.
39 os.openpty() - Open a new pseudo-terminal pair. Return a pair of file descriptors (master, slave) for the pty and the tty, respectively.
40 os.pathconf(path, name) - Return system configuration information relevant to a named file.
41 os.pipe() - Create a pipe. Return a pair of file descriptors (r, w) usable for reading and writing, respectively.
42 os.popen(command[, mode[, bufsize]]) - Open a pipe to or from command.
43 os.read(fd, n) - Read at most n bytes from file descriptor fd. Return a string containing the bytes read. If the end of the file referred to by fd has been reached, an empty string is returned.
44 os.readlink(path) - Return a string representing the path to which the symbolic link points.
45 os.remove(path) - Remove the file path.
46 os.removedirs(path) - Remove directories recursively.
47 os.rename(src, dst) - Rename the file or directory src to dst.
48 os.renames(old, new) - Recursive directory or file renaming function.
49 os.rmdir(path) - Remove the directory path
50 os.stat(path) - Perform a stat system call on the given path.
51 os.stat_float_times([newvalue]) - Determine whether stat_result represents time stamps as float objects.
52 os.statvfs(path) - Perform a statvfs system call on the given path.
53 os.symlink(src, dst) - Create a symbolic link pointing to src named dst.
54 os.tcgetpgrp(fd) - Return the process group associated with the terminal given by fd (an open file descriptor as returned by open()).
55 os.tcsetpgrp(fd, pg) - Set the process group associated with the terminal given by fd (an open file descriptor as returned by open()) to pg.
56 os.tempnam([dir[, prefix]]) - Return a unique path name that is reasonable for creating a temporary file.
57 os.tmpfile() - Return a new file object opened in update mode (w+b).
58 os.tmpnam() - Return a unique path name that is reasonable for creating a temporary file.
59 os.ttyname(fd) - Return a string which specifies the terminal device associated with file descriptor fd. If fd is not associated with a terminal device, an exception is raised.
60 os.unlink(path) - Remove the file path.
61 os.utime(path, times) - Set the access and modified times of the file specified by path.
62 os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) - Generate the file names in a directory tree by walking the tree either top-down or bottom-up.
63 os.write(fd, str) - Write the string str to file descriptor fd. Return the number of bytes actually written.
'''

'''----------------------------------------- Python OS.Path Methods --------------------------------------
The os.path is another Python module, which also provides a big range of useful methods
to manipulate files and directories. Most of the useful methods are listed here

Sr.No.    Methods with Description
----------------------------------------------------------------------
1         os.path.abspath(path)
          Returns a normalized absolutized version of the pathname path.
----------------------------------------------------------------------
2         os.path.basename(path)
          Returns the base name of pathname path.
----------------------------------------------------------------------
3         os.path.commonprefix(list)
          Returns the longest path prefix (taken character-by-character) that is a prefix of all paths in list.
----------------------------------------------------------------------
4         os.path.dirname(path)
          Returns the directory name of pathname path.
----------------------------------------------------------------------
5         os.path.exists(path)
          Returns True if path refers to an existing path. Returns False for broken symbolic links.
----------------------------------------------------------------------
6         os.path.lexists(path)
          Returns True if path refers to an existing path. Returns True for broken symbolic links.
----------------------------------------------------------------------
7         os.path.expanduser(path)
          On Unix and Windows, returns the argument with an initial component of ~ or ~user replaced by that user's home directory.
----------------------------------------------------------------------
8         os.path.expandvars(path)
          Returns the argument with environment variables expanded.
----------------------------------------------------------------------
9         os.path.getatime(path)
          Returns the time of last access of path.
----------------------------------------------------------------------
10        os.path.getmtime(path)
          Returns the time of last modification of path.
----------------------------------------------------------------------
11        os.path.getctime(path)
          Returns the system's ctime, which on some systems (like Unix) is the time of the last change, and, on others (like Windows), is the creation time for path.
----------------------------------------------------------------------
12        os.path.getsize(path)
          Returns the size, in bytes, of path.
----------------------------------------------------------------------
13        os.path.isabs(path)
          Returns True if path is an absolute pathname.
----------------------------------------------------------------------
14        os.path.isfile(path)
          Returns True if path is an existing regular file.
----------------------------------------------------------------------
15        os.path.isdir(path)
          Returns True if path is an existing directory.
----------------------------------------------------------------------
16        os.path.islink(path)
          Returns True if path refers to a directory entry that is a symbolic link.
----------------------------------------------------------------------
17        os.path.ismount(path)
          Returns True if pathname path is a mount point: a point in a file system where a different file system has been mounted.
----------------------------------------------------------------------
18        os.path.join(path1[, path2[, ...]])
          Joins one or more path components intelligently.
----------------------------------------------------------------------
19        os.path.normcase(path)
          Normalizes the case of a pathname.
----------------------------------------------------------------------
20        os.path.normpath(path)
          Normalizes a pathname.
----------------------------------------------------------------------
21        os.path.realpath(path)
          Returns the canonical path of the specified filename, eliminating any symbolic links encountered in the path.
----------------------------------------------------------------------
22        os.path.relpath(path[, start])
          Returns a relative filepath to path either from the current directory or from an optional start point.
----------------------------------------------------------------------
23        os.path.samefile(path1, path2)
          Returns True if both pathname arguments refer to the same file or directory.
----------------------------------------------------------------------
24        os.path.sameopenfile(fp1, fp2)
          Returns True if the file descriptors fp1 and fp2 refer to the same file.
----------------------------------------------------------------------
25        os.path.samestat(stat1, stat2)
          Returns True if the stat tuples stat1 and stat2 refer to the same file.
----------------------------------------------------------------------
26        os.path.split(path)
          Splits the pathname path into a pair, (head, tail) where tail is the last pathname component and head is everything leading up to that.
----------------------------------------------------------------------
27        os.path.splitdrive(path)
          Splits the pathname path into a pair (drive, tail) where drive is either a drive specification or the empty string.
----------------------------------------------------------------------
28        os.path.splitext(path)
          Splits the pathname path into a pair (root, ext) such that root + ext == path, and ext is empty or begins with a period and contains at most one period.
----------------------------------------------------------------------
29        os.path.walk(path, visit, arg)
          Calls the function visit with arguments (arg, dirname, names) for each directory in the directory tree rooted at path (including path itself, if it is a directory).
----------------------------------------------------------------------
'''
