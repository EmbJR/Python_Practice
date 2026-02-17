'''In Python, multithreading allows you to run multiple threads concurrently within a single
process, which is also known as thread-based parallelism. This means a program can
perform multiple tasks at the same time, enhancing its efficiency and responsiveness.

Multithreading in Python is especially useful for multiple I/O-bound operations, rather than
for tasks that require heavy computation.

Generally, a computer program sequentially executes the instructions, from start to the
end. Whereas, Multithreading divides the main task into more than one sub-task and
executes them in an overlapping manner'''

'''Comparison with Processes
An operating system is capable of handling multiple processes concurrently. It allocates a
separate memory space to each process so that one process cannot access or write
anything in other's space.

On the other hand, a thread can be considered a lightweight sub-process in a single
program that shares the memory space allocated to it, facilitating easier communication
and data sharing. As they are lightweight and do not require much memory overhead;
they are cheaper than processes'''

''' A process always starts with a single thread (main thread). As and when required, a new
thread can be started and sub task is delegated to it. Now the two threads are working in
an overlapping manner. When the task assigned to the secondary thread is over, it merges
with the main thread.

A thread has a beginning, an execution sequence, and a conclusion. It has an instruction
pointer that keeps track of where it is currently running within its context.
    ? It can be pre-empted (interrupted)
    ? It can temporarily be put on hold (also known as sleeping) while other threads are
        running - this is called yielding'''

''' Thread Handling Modules in Python
Python's standard library provides two main modules for managing threads: _thread and
threading

The _thread Module
The _thread module, also known as the low-level thread module, has been a part of
Python's standard library since version 2. It offers a basic API for thread management,
supporting concurrent execution of threads within a shared global data space. The module
includes simple locks (mutexes) for synchronization purposes.

The threading Module
The threading module, introduced in Python 2.4, builds upon _thread to provide a higher-
level and more comprehensive threading API. It offers powerful tools for managing
threads, making it easier to work with threads in Python applications.'''

''' Key Features of the threading Module
The threading module exposes all the methods of the thread module and provides some
additional methods -
    ? threading.activeCount() - Returns the number of thread objects that are active.
    ? threading.currentThread() - Returns the number of thread objects in the
        caller's thread control.
    ? threading.enumerate() - Returns a list of all thread objects that are currently
        active.
In addition to the methods, the threading module has the Thread class that implements
threading. The methods provided by the Thread class are as follows
    ? run() - The run() method is the entry point for a thread.
    ? start() - The start() method starts a thread by calling the run method.
    ? join([time]) - The join() waits for threads to terminate.
    ? isAlive() - The isAlive() method checks whether a thread is still executing.
    ? getName() - The getName() method returns the name of a thread.
    ? setName() - The setName() method sets the name of a thread.'''

''' Starting a New Thread
To create and start a new thread in Python, you can use either the low-level _thread
module or the higher-level threading module. The threading module is generally
recommended due to its additional features and ease of use. Below, you can see both
approaches.

Starting a New Thread Using the _thread Module
The start_new_thread() method of the _thread module provides a basic way to create and
start new threads. This method provides a fast and efficient way to create new threads in
both Linux and Windows. 

Syntax of the method:- thread.start_new_thread(function, args[, kwargs] )

This method call returns immediately, and the new thread starts executing the specified
function with the given arguments. When the function returns, the thread terminates.

Example
This example demonstrates how to use the _thread module to create and run threads.
Each thread runs the print_name function with different arguments. The time.sleep(0.5)
call ensures that the main program waits for the threads to complete their execution before
exiting.'''

import _thread
import time

def print_name(name, *arg):
    print(name, *arg)

name="Tutorialspoint..."
_thread.start_new_thread(print_name, (name, 1))
_thread.start_new_thread(print_name, (name, 1, 2))
time.sleep(0.5)

''' Starting a New Thread using the Threading Module
The threading module provides the Thread class, which is used to create and manage
threads.
Here are a few steps to start a new thread using the threading module -
    ? Create a function that you want the thread to execute.
    ? Then create a Thread object using the Thread class by passing the target function
        and its arguments.
    ? Call the start method on the Thread object to begin execution.
    ? Optionally, call the join method to wait for the thread to complete before
        proceeding.
        
Example
The following example demonstrates how to create and start threads using the threading
module. It runs a function print_name that prints a name along with some arguments.
This example creates two threads, starts them using the start() method, and waits for
them to complete using the join method.'''

import threading
import time

def print_name(name, *args):
    print(name, *args)

name = "Tutorialspoint..."
# Create and start threads
thread1 = threading.Thread(target=print_name, args=(name, 1))
thread2 = threading.Thread(target=print_name, args=(name, 1, 2))
thread1.start()
thread2.start()
# Wait for threads to complete
thread1.join()
thread2.join()
print("Threads are finished...exiting")

'''Synchronizing Threads
The threading module provided with Python includes a simple-to-implement locking
mechanism that allows you to synchronize threads. A new lock is created by calling the
Lock() method, which returns the new lock.

The acquire(blocking) method of the new lock object is used to force threads to run
synchronously. The optional blocking parameter enables you to control whether the thread
waits to acquire the lock.

If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be
acquired and with a 1 if the lock was acquired. If blocking is set to 1, the thread blocks
and wait for the lock to be released.

The release() method of the new lock object is used to release the lock when it is no longer
required.

Example:-'''


import threading
import time
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []
# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
# Start new Threads
thread1.start()
thread2.start()
# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")    

''' Multithreaded Priority Queue
The Queue module allows you to create a new queue object that can hold a specific number
of items. There are following methods to control the Queue -
    ? get() - The get() removes and returns an item from the queue.
    ? put() - The put adds item to a queue.
    ? qsize() - The qsize() returns the number of items that are currently in the queue.
    ? empty() - The empty( ) returns True if queue is empty; otherwise, False.
    ? full() - the full() returns True if queue is full; otherwise, False.
Example
'''
import queue
import threading
import time
exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("Starting " + self.name)
        process_data(self.name, self.q)
        print ("Exiting " + self.name)
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1
# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()
# Wait for queue to empty
while not workQueue.empty():
pass

# Notify threads it's time to exit
exitFlag = 1
# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")

'''----------------------------- Python - Thread Lifecycle ---------------------------
A thread object goes through different stages during its life cycle. When a new thread
object is created, it must be started, which calls the run() method of thread class. This
method contains the logic of the process to be performed by the new thread. The thread
completes its task as the run() method is over, and the newly created thread merges with
the main thread.

While a thread is running, it may be paused either for a predefined duration or it may be
asked to pause till a certain event occurs. The thread resumes after the specified interval
or the process is over
'''

''' States of a Thread Life Cycle in Python
Following are the stages of the Python Thread life cycle −
     Creating a Thread − To create a new thread in Python, you typically use the Thread
        class from the threading module.
     Starting a Thread − Once a thread object is created, it must be started by calling
        its start() method. This initiates the thread's activity and invokes its run() method
        in a separate thread.
     Paused/Blocked State − Threads can be paused or blocked for various reasons,
        such as waiting for I/O operations to complete or another thread to perform a task.
        This is typically managed by calling its join() method. This blocks the calling thread
        until the thread being joined terminates.
     Synchronizing Threads − Synchronization ensures orderly execution and shared
        resource management among threads. This can be done by using synchronization
        primitives like locks, semaphores, or condition variables.
     Termination − A thread terminates when its run() method completes execution,
        either by finishing its task or encountering an exception.

Example: Python Thread Life Cycle Demonstration
This example demonstrates the thread life cycle in Python by showing thread creation,
starting, execution, and synchronization with the main thread.'''

import threading
def func(x):
    print('Current Thread Details:', threading.current_thread())
    for n in range(x):
        print('{} Running'.format(threading.current_thread().name), n)
    print('Internal Thread Finished...')
# Create thread objects
t1 = threading.Thread(target=func, args=(2,))
t2 = threading.Thread(target=func, args=(3,))
# Start the threads
print('Thread State: CREATED')
t1.start()
t2.start()
# Wait for threads to complete
t1.join()
t2.join()
print('Threads State: FINISHED')
# Simulate main thread work
for i in range(3):
    print('Main Thread Running', i)
print("Main Thread Finished...")

''' Example: Using a Synchronization Primitive
Here is another example demonstrates the thread life cycle in Python, including creation,
starting, running, and termination states, along with synchronization using a semaphore.'''
import threading
import time
# Create a semaphore
semaphore = threading.Semaphore(2)
def worker():
    with semaphore:
        print('{} has started working'.format(threading.current_thread().name))
        time.sleep(2)
        print('{} has finished working'.format(threading.current_thread().name))
# Create a list to keep track of thread objects
threads = []
# Create and start 5 threads
for i in range(5):
    t = threading.Thread(target=worker, name='Thread-{}'.format(i+1))
    threads.append(t)
    print('{} has been created'.format(t.name))
    t.start()
# Wait for all threads to complete
for t in threads:
    t.join()
    print('{} has terminated'.format(t.name))
print('Threads State: All are FINISHED')
print("Main Thread Finished...")


'''------------------------- Python - Creating a Thread ---------------------
Creating a thread in Python involves initiating a separate flow of execution within a
program, allowing multiple operations to run concurrently. This is particularly useful for
performing tasks simultaneously, such as handling various I/O operations in parallel.
Python provides multiple ways to create and manage threads.
     Creating a thread using the threading module is generally recommended due to its
        higher-level interface and additional functionalities.
     On the other hand, the _thread module offers a simpler, lower-level approach to
        create and manage threads, which can be useful for straightforward, low-overhead
        threading tasks.
In this tutorial, you will learn the basics of creating threads in Python using different
approaches. We will cover creating threads using functions, extending the Thread class
from the threading module, and utilizing the _thread module.'''

''' Creating Threads with Functions
You can create threads by using the Thread class from the threading module. In this
approach, you can create a thread by simply passing a function to the Thread object. Here
are the steps to start a new thread −
     Define a function that you want the thread to execute.
     Create a Thread object using the Thread class, passing the target function and its
        arguments.
     Call the start method on the Thread object to begin execution.
     Optionally, call the join method to wait for the thread to complete before
        proceeding.

Example
The following example demonstrates concurrent execution using threads in Python. It
creates and starts multiple threads that execute different tasks concurrently by specifying
user-defined functions as targets within the Thread class.'''

from threading import Thread
def addition_of_numbers(x, y):
    result = x + y
    print('Addition of {} + {} = {}'.format(x, y, result))
def cube_number(i):
    result = i ** 3
    print('Cube of {} = {}'.format(i, result))
def basic_function():
    print("Basic function is running concurrently...")

Thread(target=addition_of_numbers, args=(2, 4)).start()
Thread(target=cube_number, args=(4,)).start()
Thread(target=basic_function).start()

''' Creating Threads by Extending the Thread Class
Another approach to creating a thread is by extending the Thread class. This approach
involves defining a new class that inherits from Thread and overriding its __init__ and run
methods. Here are the steps to start a new thread −
     Define a new subclass of the Thread class.
     Override the __init__ method to add additional arguments.
     Override the run method to implement the thread's behavior.
Example
This example demonstrates how to create and manage multiple threads using a custom
MyThread class that extends the threading.Thread class in Python'''
import threading
import time
exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print ("Exiting " + self.name)
def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
# Start new Threads
thread1.start()
thread2.start()
print ("Exiting Main Thread")

''' Creating Threads using start_new_thread() Function
The start_new_thread() function included in the _thread module is used to create a new
thread in the running program. This module offers a low-level approach to threading. It is
simpler but does not have some of the advanced features provided by the threading module.

Here is the syntax of the _thread.start_new_thread() Function

syntax:- _thread.start_new_thread ( function, args[, kwargs] )

This function starts a new thread and returns its identifier. The function parameter
specifies the function that the new thread will execute. Any arguments required by this
function can be passed using args and kwargs.
Example'''
import _thread
import time
# Define a function for the thread
def thread_task( threadName, delay):
    for count in range(1, 6):
        time.sleep(delay)
        print ("Thread name: {} Count: {}".format ( threadName, count ))
# Create two threads as follows
try:
    _thread.start_new_thread( thread_task, ("Thread-1", 2, ) )
    _thread.start_new_thread( thread_task, ("Thread-2", 4, ) )
except:
    print ("Error: unable to start thread")
while True:
    pass
thread_task("test", 0.3)