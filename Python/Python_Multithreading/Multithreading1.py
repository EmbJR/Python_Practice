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