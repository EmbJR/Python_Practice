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
    time.sleep(5)

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

var = 10

while var:
    ''' If we put the empty while loop, the threads will continously run.'''
    var-=1
    time.sleep(1)
    pass

thread_task("test", 0.3)

'''------------------------------------ Python - Starting a Thread ---------------------------
In Python, starting a thread involves using the start() method provided by the Thread
class in the threading module. This method initiates the thread's activity and automatically
calls its run() method in a separate thread of execution. Meaning that, when you call
start() on each thread object (for example., thread1, thread2, thread3) to initiate their
execution, Python launches separate threads that concurrently execute the run() method defined in
each Thread instance. The main thread continues its execution after starting the child
threads.

In this tutorial, you will see a detailed explanation and example of how to use the start()
method effectively in multi-threaded programming to understand its behavior in multi-
thread applications.'''

''' Starting a Thread in Python
The start() method is fundamental for beginning the execution of a thread. It sets up the
thread's environment and schedules it to run. Importantly, it should only be called once
per Thread object. If this method is called more than once on the same Thread object, it
will raise a RuntimeError.

Here is the syntax for using the start() method on a Thread object −
        threading.thread.start()

Example:-
Let's see the below example, that demonstrates how to start a new thread in Python using
the start() method'''

from threading import Thread
from time import sleep
def my_function(arg):
    for i in range(arg):
        print("child Thread running", i)
        sleep(0.5)
thread = Thread(target = my_function, args = (10, ))
thread.start()
print("thread finished...exiting")

''' Example
Here is another example demonstrating the working of the start() method. You can
observe that, by not calling the start() method on thread2, it remains inactive and does
not begin execution.'''

import threading
import time
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter)
        print("Exiting " + self.name)
def print_time(threadName, counter):
    while counter:
        time.sleep(1)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

thread3 = MyThread(3, "Thread-3", 3)
# Start new Threads
thread1.start()
thread3.start()
print("Exiting Main Thread")

'''----------- Revision till --------------'''
'''------------------------------------ Python - Joining the Threads ------------------------
In Python, joining the threads means using the join() method to wait for one thread to
finish before moving on to others. This is useful in multithreaded programming to make
sure some threads are completed before starting or continuing with other threads. By
using the join() method, you can make sure that one thread has finished running before
another thread or the main program continues. In this tutorial you will get the detailed
explain of the join() method with suitable examples.'''

''' Joining the Threads in Python
To join the threads in Python, you can use the Thread.join() method from the threading
module. Which generally is used to block the calling thread until the thread on which join()
was called terminates. The termination may be either normal, because of an unhandled
exception − or until the optional timeout occurs. You can call join() multiple times.
However, if you try to join the current thread or attempts to join a thread before starting
it with the start() method, will raise the RuntimeError exception.

Following is the syntax of the Thread.join() method −
    thread.join(timeout)

Where, the timeout is an optional parameter that takes a floating-point number specifying
the maximum wait time in seconds (or fractions thereof). If it is not provided or None, the
method will block until the thread terminates.

This method always returns None. After calling join(), you can use is_alive() to check if
the thread is still running. This is useful to determine if the join() call timed out.

Example
The following example demonstrates the use of join() in a multithreaded program. It starts
two threads (thread1 and thread2). Initially, it blocks the main thread until thread1
finishes executing the my_function_1. After thread1 completes, thread2.start() is called,
followed by thread2.join() to ensure that the main thread waits until thread2 finishes
executing my_function_2().'''
from threading import Thread
from time import sleep
def my_function_1(arg):
    for i in range(arg):
        print("Child Thread 1 running", i)
        sleep(0.5)
def my_function_2(arg):
    for i in range(arg):
        print("Child Thread 2 running", i)
        sleep(0.1)
# Create thread objects
thread1 = Thread(target=my_function_1, args=(5,))
thread2 = Thread(target=my_function_2, args=(3,))
# Start the first thread and wait for it to complete
thread1.start()
thread1.join()
# Start the second thread and wait for it to complete
thread2.start()
thread2.join()
print("Main thread finished...exiting")

''' Example
Here is another example that demonstrates how the join() method with a timeout allows
waiting for a thread to complete for a specified period, then proceeding even if the thread
hasn't finished'''

from threading import Thread
from time import sleep
def my_function_1(arg):
    for i in range(arg):
        print("Child Thread 1 running", i)
        sleep(0.5)
def my_function_2(arg):
    for i in range(arg):
        print("Child Thread 2 running", i)
        sleep(0.1)
# Create thread objects
thread1 = Thread(target=my_function_1, args=(5,))
thread2 = Thread(target=my_function_2, args=(3,))
# Start the first thread and wait for 0.2 seconds
thread1.start()
thread1.join(timeout=0.2)
# Start the second thread and wait for it to complete
thread2.start()
thread2.join()
print("Main thread finished...exiting")

'''---------------------------- Python - Naming the Threads -----------------------------
In Python, naming a thread involves assigning a string as an identifier to the thread object.
Thread names in Python are primarily used for identification purposes only and do not
affect the thread's behavior or semantics. Multiple threads can share the same name, and
names can be specified during the thread's initialization or changed dynamically.'''

''' Naming the Threads in Python
When you create a thread using threading.Thread() class, you can specify its name using
the name parameter. 

If not provided, Python assigns a default name like the following
pattern "Thread-N", where N is a small decimal number. Alternatively, if you specify a
target function, the default name format becomes "Thread-N (target_function_name)".

Example
Here is an example demonstrates assigning custom and default names to threads created
using threading.Thread() class, and displays how names can reflect target functions.'''

from threading import Thread
import threading
from time import sleep
def my_function_1(arg):
    print("This tread name is", threading.current_thread().name)
# Create thread objects
thread1 = Thread(target=my_function_1, name='My_thread', args=(2,))
thread2 = Thread(target=my_function_1, args=(3,))
print("This tread name is", threading.current_thread().name)
# Start the first thread and wait for 0.2 seconds
thread1.start()
thread1.join()
# Start the second thread and wait for it to complete
thread2.start()
thread2.join()

''' Dynamically Assigning Names to the Python Threads
You can assign or change a thread's name dynamically by directly modifying the name
attribute of the thread object.
Example:- '''

from threading import Thread
import threading
from time import sleep
def my_function_1(arg):
    threading.current_thread().name = "custom_name"
    print("This tread name is", threading.current_thread().name)
# Create thread objects
thread1 = Thread(target=my_function_1, name='My_thread', args=(2,))
thread2 = Thread(target=my_function_1, args=(3,))
print("This tread name is", threading.current_thread().name)
# Start the first thread and wait for 0.2 seconds
thread1.start()
thread1.join()
# Start the second thread and wait for it to complete
thread2.start()
thread2.join()

''' Example
Threads can be initialized with custom names and even renamed after creation. This
example demonstrates creating threads with custom names and modifying a thread's
name after creation.'''

import threading
def addition_of_numbers(x, y):
    print("This Thread name is :", threading.current_thread().name)
    result = x + y
def cube_number(i):
    result = i ** 3
    print("This Thread name is :", threading.current_thread().name)
def basic_function():
    print("This Thread name is :", threading.current_thread().name)
# Create threads with custom names
t1 = threading.Thread(target=addition_of_numbers, name='My_thread', args=(2, 4))
t2 = threading.Thread(target=cube_number, args=(4,))
t3 = threading.Thread(target=basic_function)
# Start and join threads
t1.start()
t1.join()
t2.start()
t2.join()
t3.name = 'custom_name' # Assigning name after thread creation
t3.start()
t3.join()
print(threading.current_thread().name) # Print main thread's name


'''---------------------------- Python - Thread Scheduling -------------------------
Thread scheduling in Python is a process of deciding which thread runs at any given time.
In a multi-threaded program, multiple threads are executed independently, allowing for
parallel execution of tasks. However, Python does not have built-in support for controlling
thread priorities or scheduling policies directly. Instead, it relies on the operating system's
thread scheduler.

Python threads are mapped to native threads of the host operating system, such as POSIX
threads (pthreads) on Unix-like systems or Windows threads. The operating system's
scheduler manages the execution of these threads, including context switching, thread
priorities, and scheduling policies. Python provides basic thread scheduling capabilities
through the threading.Timer class and the sched module.

In this tutorial will learn the basics of thread scheduling in Python, including how to use
the sched module for scheduling tasks and the threading.Timer class for delayed execution
of functions.'''

''' Scheduling Threads using the Timer Class
The Timer class of the Python threading module allows you to schedule a function to be
called after a certain amount of time. This class is a subclass of Thread and serves as an
example of creating custom threads.

You start a timer by calling its start() method, similar to threads. If needed, you can stop
the timer before it begins by using the cancel() method. Note that the actual delay before
the action is executed might not match the exact interval specified.

Example
This example demonstrates how to use the threading.Timer() class to schedule and
manage the execution of tasks (custom threads) in Python.'''
import threading
import time
# Define the event function
def schedule_event(name, start):
    now = time.time()
    elapsed = int(now - start)
    print('Elapsed:', elapsed, 'Name:', name)
# Start time
start = time.time()
print('START:', time.ctime(start))

# Schedule events using Timer
t1 = threading.Timer(3, schedule_event, args=('EVENT_1', start))
t2 = threading.Timer(2, schedule_event, args=('EVENT_2', start))
# Start the timers
t1.start()
t2.start()
t1.join()
t2.join()
# End time
end = time.time()
print('End:', time.ctime(end))

''' Scheduling Threads using the sched Module
The sched module in Python's standard library provides a way to schedule tasks. It
implements a generic event scheduler for running tasks at specific times. It provides
similar tools like task scheduler in windows or Linux.

Key Classes and Methods of the sched Module
The scheduler() class is defined in the sched module is used to create a scheduler object.
Here is the syntax of the class
        scheduler(timefunc=time.monotonic, delayfunc=time.sleep)

The methods defined in scheduler class include −
     scheduler.enter(delay, priority, action, argument=(), kwargs={}) −
        Events can be scheduled to run after a delay, or at a specific time. To schedule
        them with a delay, enter() method is used.
     scheduler.cancel(event) − Remove the event from the queue. If the event is
        not an event currently in the queue, this method will raise a ValueError.
     scheduler.run(blocking=True) − Run all scheduled events.

Events can be scheduled to run after a delay, or at a specific time. To schedule them with
a delay, use the enter() method, which takes four arguments as below.
     A number representing the delay
     A priority value
     The function to call
     A tuple of arguments for the function

Example:- 
This example demonstrates how to schedule events to run after a delay using the sched
module. It schedules two different events'''

import sched
import time
scheduler = sched.scheduler(time.time, time.sleep)
def schedule_event(name, start):
    now = time.time()
    elapsed = int(now - start)
    print('elapsed=',elapsed, 'name=', name)
start = time.time()
print('START:', time.ctime(start))
scheduler.enter(2, 1, schedule_event, ('EVENT_1', start))
scheduler.enter(5, 1, schedule_event, ('EVENT_2', start))
scheduler.run()
# End time
end = time.time()
print('End:', time.ctime(end))

''' Example
Let's take another example to understand the concept better. This example schedules a
function to perform an addition after a 4-second delay using the sched module in Python.'''

import sched
from datetime import datetime
import time
def addition(a,b):
    print("Performing Addition : ", datetime.now())
    print("Time : ", time.monotonic())
    print("Result {}+{} =".format(a, b), a+b)
s = sched.scheduler()
print("Start Time : ", datetime.now())
event1 = s.enter(4, 1, addition, argument = (5,6))
print("Event Created : ", event1)
s.run()
print("End Time : ", datetime.now())

'''------------------------- Python - Thread Pools ---------------------------
A thread pool is a mechanism that automatically manages multiple threads efficiently,
allowing tasks to be executed concurrently. Python does not provide thread pooling directly
through the threading module.

Instead, it offers thread-based pooling through the multiprocessing.dummy module and
the concurrent.futures module. These modules provide convenient interfaces for creating
and managing thread pools, making it easier to perform concurrent task execution.'''

''' What is a Thread Pool?
A thread pool is a collection of threads that are managed by a pool. Each thread in the
pool is called a worker or a worker thread. These threads can be reused to perform multiple
tasks, which reduces the burden of creating and destroying threads repeatedly.

Thread pools control the creation of threads and their life cycle, making them more
efficient for handling large numbers of tasks.
We can implement thread-pools in Python using the following classes −
     Python ThreadPool Class
     Python ThreadPoolExecutor Class'''

''' Using Python ThreadPool Class
The multiprocessing.pool.ThreadPool class provides a thread pool interface within the
multiprocessing module. It manages a pool of worker threads to which jobs can be
submitted for concurrent execution.

A ThreadPool object simplifies the management of multiple threads by handling the
creation and distribution of tasks among the worker threads. It shares an interface with
the Pool class, originally designed for processes, but has been adjusted to work with
threads too.

ThreadPool instances are fully interface-compatible with Pool instances and should be
managed either as a context manager or by calling close() and terminate() manually.

Example:- 
This example demonstrates the parallel execution of the square and cube functions on the
list of numbers using the Python thread pool, where each function is applied to the
numbers concurrently with up to 3 threads, each with a delay of 1 second between
executions.'''

from multiprocessing.dummy import Pool as ThreadPool
import time
def square(number):
    sqr = number * number
    time.sleep(1)
    print("Number:{} Square:{}".format(number, sqr))
def cube(number):
    cub = number*number*number
    time.sleep(1)
    print("Number:{} Cube:{}".format(number, cub))
numbers = [1, 2, 3, 4, 5]
pool = ThreadPool(3)
pool.map(square, numbers)
pool.map(cube, numbers)
pool.close()

''' Using Python ThreadPoolExecutor Class
The ThreadPoolExecutor class of the Python the concurrent.futures module provides a
high-level interface for asynchronously executing functions using threads. The
concurrent.futures module includes Future class and two Executor classes −
ThreadPoolExecutor and ProcessPoolExecutor.'''

''' The Future Class
The concurrent.futures.Future class is responsible for handling asynchronous execution of
any callable such as a function. To obtain a Future object, you should call the submit()
method on any Executor object. It should not be created directly by its constructor.

Important methods in the Future class are
     result(timeout=None): This method returns the value returned by the call. If the
        call hasn't yet completed, then this method will wait up to timeout seconds. If the
        call hasn't completed in timeout seconds, then a TimeoutError will be raised. If
        timeout is not specified, there is no limit to the wait time.
     cancel(): This method, attempt to cancel the call. If the call is currently being
        executed or finished running and cannot be cancelled then the method will return
        a boolean value False. Otherwise the call will be cancelled and the method returns
        True.
     cancelled(): Returns True if the call was successfully cancelled.
     running(): Returns True if the call is currently being executed and cannot be
        cancelled.
     done(): Returns True if the call was successfully cancelled or finished running.
'''

''' The ThreadPoolExecutor Class
This class represents a pool of specified number maximum worker threads to execute calls
asynchronously.
concurrent.futures.ThreadPoolExecutor(max_threads)

Example
Here is an example that uses the concurrent.futures.ThreadPoolExecutor class to manage
and execute tasks asynchronously in Python. Specifically, it shows how to submit multiple
tasks to a thread pool and how to check their execution status.'''

from concurrent.futures import ThreadPoolExecutor
from time import sleep
def square(numbers):
    for val in numbers:
        ret = val*val
        sleep(1)
        print("Number:{} Square:{}".format(val, ret))
def cube(numbers):
    for val in numbers:
        ret = val*val*val
        sleep(1)
        print("Number:{} Cube:{}".format(val, ret))
if __name__ == '__main__':
    numbers = [1,2,3,4,5]
    executor = ThreadPoolExecutor(4)
    thread1 = executor.submit(square, (numbers))
    thread2 = executor.submit(cube, (numbers))
    print("Thread 1 executed ? :",thread1.done())
    print("Thread 2 executed ? :",thread2.done())
    sleep(2)
    print("Thread 1 executed ? :",thread1.done())
    print("Thread 2 executed ? :",thread2.done())

'''----------------------------------Python - Main Thread -----------------------------
In Python, the main thread is the initial thread that starts when the Python interpreter is
executed. It is the default thread within a Python process, responsible for managing the
program and creating additional threads. Every Python program has at least one thread
of execution called the main thread.

The main thread by default is a non-daemon thread. In this tutorial you will see the
detailed explanation with relevant examples about main thread in Python programming.'''

''' Accessing the Main Thread
The threading module in Python provides functions to access the threads. Here are the
key functions −
     threading.current_thread(): This function returns a threading.Thread instance
        representing the current thread.
     threading.main_thread(): Returns a threading.Thread instance representing the
        main thread.

Example:- 
The threading.current_thread() function returns a threading.Thread instance representing
the current thread.'''

import threading
name = 'Tutorialspoint'
print('Output:', name)
print(threading.current_thread())

''' Example
This example demonstrates how to use the threading.main_thread() function to get a
reference to the main thread. And it is also shows the difference between the main thread
and other threads using threading.current_thread() function.'''

import threading
import time
def func(x):
    time.sleep(x)
    if not threading.current_thread() is threading.main_thread():
        print('threading.current_thread() not threading.main_thread()')
t = threading.Thread(target=func, args=(0.5,))
t.start()
print(threading.main_thread())
print("Main thread finished")

''' Main Thread Behavior in Python
The main thread will exit whenever it has finished executing all the code in your script that
is not started in a separate thread. For instance, when you start a new thread using start()
method, the main thread will continue to execute the remaining code in the script until it
reaches the end and then exit.

Since the other threads are started in a non-daemon mode by default, they will continue
running until they are finished, even if the main thread has exited.

Example
The following example shows the main thread behavior in a python multithreaded
program.'''

import threading
import time
def func(x):
    print('Current Thread Details:',threading.current_thread())
    for n in range(x):
        print('Internal Thread Running', n)
    print('Internal Thread Finished...')
t = threading.Thread(target=func, args=(6,))
t.start()
for i in range(3):
    print('Main Thread Running',i)
print("Main Thread Finished...")

''' Main Thread Waiting for Other Threads
To ensure that the main thread waits for all other threads to finish, you can join the threads
using the join() method. By using the join() method, you can control the execution flow
and ensure that the main thread properly waits for all other threads to complete their
tasks before exiting. This helps in managing the lifecycle of threads in a multi-threaded
Python program effectively.

Example
This example demonstrates how to properly manage the main thread and ensure it does
not exit before the worker threads have finished their tasks.'''

from threading import Thread
from time import sleep
def my_function_1():
    print("Worker 1 started")
    sleep(1)
    print("Worker 1 done")
def my_function_2(main_thread):
    print("Worker 2 waiting for Worker 1 to finish")
    main_thread.join()
    print("Worker 2 started")
    sleep(1)
    print("Worker 2 done")
worker1 = Thread(target=my_function_1)
worker2 = Thread(target=my_function_2, args=(worker1,))
worker1.start()
worker2.start()
for num in range(6):
    print("Main thread is still working on task", num)
    sleep(0.60)
worker1.join()
print("Main thread Completed")

'''----------------------------- Python - Thread Priority ---------------------------
In Python, currently thread priority is not directly supported by the threading module.
unlike Java, Python does not support thread priorities, thread groups, or certain thread
control mechanisms like destroying, stopping, suspending, resuming, or interrupting
threads.

Python threads are designed simple and are loosely based on Java's threading model. This
is because of Python's Global Interpreter Lock (GIL), which manages Python threads.

However, you can simulate priority-based behavior using techniques such as sleep
durations, custom scheduling logic within threads or using the additional module which
manages task priorities'''

''' Setting the Thread Priority Using Sleep()
You can simulate thread priority by introducing delays or using other mechanisms to
control the execution order of threads. One common approach to simulate thread priority
is by adjusting the sleep duration of your threads.

Threads with a lower priority sleep longer, and threads with a high priority sleep shorter.

Example
Here's a simple example to demonstrate how to customize the thread priorities using the
delays in Python threads. In this example, Thread-2 completes before Thread-1 because
it has a lower priority value, resulting in a shorter sleep time.'''
import threading
import time
class DummyThread(threading.Thread):
    def __init__(self, name, priority):
        threading.Thread.__init__(self)
        self.name = name
        self.priority = priority
    def run(self):
        name = self.name
        time.sleep(1.0 * self.priority)
        print(f"{name} thread with priority {self.priority} is running")
# Creating threads with different priorities
t1 = DummyThread(name='Thread-1', priority=4)
t2 = DummyThread(name='Thread-2', priority=1)
# Starting the threads
t1.start()
t2.start()
# Waiting for both threads to complete
t1.join()
t2.join()
print('All Threads are executed')

''' Adjusting Python Thread Priority on Windows
On Windows Operating system you can manipulate the thread priority using the ctypes
module. This is one of the Python’s standard module used for interacting with the Windows
API.

Example
This example demonstrates how to manually set the priority of threads in Python on a
Windows system using the ctypes module.'''

import threading
import ctypes
import time
# Constants for Windows API
w32 = ctypes.windll.kernel32
SET_THREAD = 0x20
PRIORITIZE_THE_THREAD = 1
class MyThread(threading.Thread):
    def __init__(self, start_event, name, iterations):
        super().__init__()
        self.start_event = start_event
        self.thread_id = None
        self.iterations = iterations
        self.name = name

    def set_priority(self, priority):
        if not self.is_alive():
            print('Cannot set priority for a non-active thread')
            return        
        thread_handle = w32.OpenThread(SET_THREAD, False, self.thread_id)
        success = w32.SetThreadPriority(thread_handle, priority)
        w32.CloseHandle(thread_handle)
        if not success:
            print('Failed to set thread priority:', w32.GetLastError())
    def run(self):
        self.thread_id = w32.GetCurrentThreadId()
        self.start_event.wait()
        while self.iterations:
            print(f"{self.name} running")
            start_time = time.time()
            while time.time() - start_time < 1:
                pass
        self.iterations -= 1

# Create an event to synchronize thread start
start_event = threading.Event()
# Create threads
thread_normal = MyThread(start_event, name='normal', iterations=4)
thread_high = MyThread(start_event, name='high', iterations=4)
# Start the threads
thread_normal.start()
thread_high.start()
# Adjusting priority of 'high' thread
thread_high.set_priority(PRIORITIZE_THE_THREAD)
# Trigger thread execution
start_event.set()

''' Prioritizing Python Threads Using the Queue Module
The queue module in Python's standard library is useful in threaded programming when
information must be exchanged safely between multiple threads. 

The Priority Queue class
in this module implements all the required locking semantics.
With a priority queue, the entries are kept sorted (using the heapq module) and the lowest
valued entry is retrieved first.

The Queue objects have following methods to control the Queue −
     get() − The get() removes and returns an item from the queue.
     put() − The put adds item to a queue.
     qsize() − The qsize() returns the number of items that are currently in the queue.
     empty() − The empty( ) returns True if queue is empty; otherwise, False.
     full() − the full() returns True if queue is full; otherwise, False.`

queue.PriorityQueue(maxsize=0)

This is the Constructor for a priority queue. maxsize is an integer that sets the upper limit
on the number of items that can be placed in the queue. If maxsize is less than or equal
to zero, the queue size is infinite.

The lowest valued entries are retrieved first (the lowest valued entry is the one that would
be returned by min(entries)). 
A typical pattern for entries is a tuple in the form − (priority_number, data)

Example
This example demonstrates the use of the PriorityQueue class in the queue module to
manage task priorities between the two threads.'''

from time import sleep
from random import random, randint
from threading import Thread
from queue import PriorityQueue
queue = PriorityQueue()

def producer(queue):
    print('Producer: Running')
    for i in range(5):
        # create item with priority
        value = random()
        priority = randint(0, 5)
        item = (priority, value)
        queue.put(item)
# wait for all items to be processed
    queue.join()
    queue.put(None)
    print('Producer: Done')

def consumer(queue):
    print('Consumer: Running')
    while True:
        # get a unit of work
        item = queue.get()
        if item is None:
            break
        sleep(item[1])
        print(item)
        queue.task_done()
    print('Consumer: Done')

producer = Thread(target=producer, args=(queue,))
producer.start()
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
producer.join()
consumer.join()

'''-------------------------------- Python - Daemon Threads ------------------------
Daemon threads in Python are useful for running background tasks that are not critical to
the program's operation. They allow you to run tasks in the background without worrying
about keeping track of them.
Python provides two types of threads: non-daemon and daemon threads. By default,
threads are non-daemon threads. This tutorial provides a detailed explanation with
relevant examples about daemon threads in Python programming.'''

''' Overview of Daemon Threads
Sometimes, it is necessary to execute a task in the background. A special type of thread
is used for background tasks, called a daemon thread. These threads handle non-critical tasks that may be
useful to the application but do not hamper it if they fail or are canceled while they are
active and running.

Also, a daemon thread will not have control over when it is terminated. The program will
terminate once all non-daemon threads finish, even if there are daemon threads still
running at that point of time.

Difference Between Daemon & Non-Daemon Threads

+------------------+------------------+
| Daemon           | Non-daemon       |
+------------------+------------------+
| A process will   | A process will   |
| exit if only     | not exit if at   |
| daemon threads   | least one        |
| are running (or  | non-daemon       |
| if no threads    | thread is        |
| are running).    | running.         |
+------------------+------------------+
| Daemon threads   | Non-daemon       |
| are used for     | threads are used |
| background tasks. | for critical     |
|                  | tasks.           |
+------------------+------------------+
| Daemon threads   | Non-daemon       |
| are terminated    | threads run to   |
| abruptly.        | completion.      |
+------------------+------------------+

Daemon threads can perform tasks such as −
     Create a file that stores Log information in the background.
     Perform web scraping in the background.
     Save the data automatically into a database in the background'''

'''Creating a Daemon Thread in Python
To create a daemon thread, you need to set the daemon property of the Thread constructor
to True.
    t1=threading.Thread(daemon=True)
By default, the daemon property is set to None, If you change it to not None, daemon
explicitly sets whether the thread is daemonic.

Example:- 
Take a look at the following example to create a daemon thread and check whether the
thread isusing the daemon attribute'''

import threading
from time import sleep
# function to be executed in a new thread
def run():
    # get the current thread
    thread = threading.current_thread()
    # is it a daemon thread?
    print(f'Daemon thread: {thread.daemon}')
# Create a new thread and set it as daemon
thread = threading.Thread(target=run, daemon=True)
# start the thread
thread.start()
print('Is Main Thread is Daemon thread:', threading.current_thread().daemon)
# Block for a short time to allow the daemon thread to run
sleep(0.5)

''' If a thread object is created in the main thread without any parameters, then the created
thread will be a non-daemon thread because the main thread is not a daemon thread.
Therefore, all threads created in the main thread default to non-daemon. However, we
can change the daemon property to True by using the Thread.daemon attribute before
starting the thread.
Example
Here is an example'''

import threading
from time import sleep
# function to be executed in a new thread
def run():
    # get the current thread
    thread = threading.current_thread()
    # is it a daemon thread?
    print(f'Daemon thread: {thread.daemon}')
# Create a new thread
thread = threading.Thread(target=run)
# Using the daemon property set the thread as daemon before starting the thread
thread.daemon = True
# start the thread
thread.start()
print('Is Main Thread is Daemon thread:', threading.current_thread().daemon)
# Block for a short time to allow the daemon thread to run
sleep(0.5)

''' Managing the Daemon Thread Attribute
If you attempt to set the daemon status of a thread after starting it, then a RuntimeError
will be raised.
Example
Here is another example that demonstrates getting the RuntimeError when you try to set
the daemon status of a thread after starting it.'''

from time import sleep
from threading import current_thread
from threading import Thread
# function to be executed in a new thread
def run():
    # get the current thread
    thread = current_thread()
    # is it a daemon thread?
    print(f'Daemon thread: {thread.daemon}')
    thread.daemon = True
# create a new thread
thread = Thread(target=run)
# start the new thread
thread.start()
# block for a 0.5 sec for daemon thread to run
sleep(0.5)

'''-------------------------------- Python - Synchronizing Threads ------------------------
In Python, when multiple threads are working concurrently with shared resources, it's
important to synchronize their access to maintain data integrity and program correctness.

Synchronizing threads in python can be achieved using various synchronization primitives
provided by the threading module, such as locks, conditions, semaphores, and barriers to
control access to shared resources and coordinate the execution of multiple threads.
'''

''' Thread Synchronization using Locks
The lock object in the Python's threading module provide the simplest synchronization
primitive. They allow threads to acquire and release locks around critical sections of code,
ensuring that only one thread can execute the protected code at a time.

A new lock is created by calling the Lock() method, which returns a lock object. The lock
can be acquired using the acquire(blocking) method, which force the threads to run
synchronously. The optional blocking parameter enables you to control whether the thread
waits to acquire the lock and released using the release() method.

Example
The following example demonstrates how to use locks (the threading.Lock() method) to
synchronize threads in Python, ensuring that multiple threads access shared resources
safely and correctly.'''

import threading
counter = 10
def increment(theLock, N):
    global counter
    for i in range(N):
        theLock.acquire()
        counter += 1
        theLock.release()

lock = threading.Lock()
t1 = threading.Thread(target=increment, args=[lock, 2])
t2 = threading.Thread(target=increment, args=[lock, 10])
t3 = threading.Thread(target=increment, args=[lock, 4])

t1.start()
t2.start()
t3.start()
# Wait for all threads to complete
for thread in (t1, t2, t3):
    thread.join()
print("All threads have completed")
print("The Final Counter Value:", counter)

''' Condition Objects for Synchronizing Python Threads
Condition objects enable threads to wait until notified by another thread. They are useful
for providing communication between the threads. The wait() method is used to block a
thread until it is notified by another thread through notify() or notify_all().

Example
This example demonstrates how Condition objects can synchronize threads using the
notify() and wait() methods'''

import threading
counter = 0
# Consumer function
def consumer(cv):
    global counter
    with cv:
        print("Consumer is waiting")
        cv.wait() # Wait until notified by increment
        print("Consumer has been notified. Current Counter value:", counter)

# increment function
def increment(cv, N):
    global counter
    with cv:
        print("increment is producing items")
        for i in range(1, N + 1):
            counter += i # Increment counter by i
        # Notify the consumer
        cv.notify()
        print("Increment has finished")

# Create a Condition object
cv = threading.Condition()
# Create and start threads
consumer_thread = threading.Thread(target=consumer, args=[cv])
increment_thread = threading.Thread(target=increment, args=[cv, 5])
consumer_thread.start()
increment_thread.start()
consumer_thread.join()
increment_thread.join()
print("The Final Counter Value:", counter)

''' Synchronizing threads using the join() Method
The join() method in Python's threading module is used to wait until all threads have
completed their execution. This is a straightforward way to synchronize the main thread
with the completion of other threads.

Example
This demonstrates synchronization of threads using the join() method to ensure that the
main thread waits for all started threads to complete their work before proceeding.'''

import threading
import time
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 3)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threads = []
# Create new threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)
# Start the new Threads
thread1.start()
thread2.start()
# Join the threads
thread1.join()
thread2.join()
print("Exiting Main Thread")

''' Additional Synchronization Primitives
In addition to the above synchronization primitives, Python's threading module offers: −
     RLocks (Reentrant Locks): A variant of locks that allow a thread to acquire the
        same lock multiple times before releasing it, useful in recursive functions or nested
        function calls.
     Semaphores:Similar to locks but with a counter. Threads can acquire the
        semaphore up to a certain limit defined during initialization. Semaphores are useful
        for limiting access to resources with a fixed capacity.
     Barriers: Allows a fixed number of threads to synchronize at a barrier point and
        continue executing only when all threads have reached that point. Barriers are
        useful for coordinating a group of threads that must all complete a certain phase
        of execution before any of them can proceed further.'''