'''--------------------------- Python - Inter-Thread Communication -------------------
Inter-Thread Communication refers to the process of enabling communication and
synchronization between threads within a Python multi-threaded program.

Generally, threads in Python share the same memory space within a process, which allows
them to exchange data and coordinate their activities through shared variables, objects,
and specialized synchronization mechanisms provided by the threading module.

To facilitate inter-thread communication, the threading module provides various
synchronization primitives like, Locks, Events, Conditions, and Semaphores objects. In
this tutorial you will learn how to use the Event and Condition object for providing the
communication between threads in a multi-threaded program.'''

''' The Event Object
An Event object manages the state of an internal flag so that threads can wait or set.
Event object provides methods to control the state of this flag, allowing threads to
synchronize their activities based on shared conditions.
The flag is initially false and becomes true with the set() method and reset to false with
the clear() method. The wait() method blocks until the flag is true.

Following are the key methods of the Event object −
     is_set(): Return True if and only if the internal flag is true.
     set(): Set the internal flag to true. All threads waiting for it to become true are
        awakened. Threads that call wait() once the flag is true will not block at all.
     clear(): Reset the internal flag to false. Subsequently, threads calling wait() will
        block until set() is called to set the internal flag to true again.
     wait(timeout=None): Block until the internal flag is true. If the internal flag is
        true on entry, return immediately. Otherwise, block until another thread calls set()
        to set the flag to true, or until the optional timeout occurs. When the timeout
        argument is present and not None, it should be a floating point number specifying
        a timeout for the operation in seconds.

Example
The following code attempts to simulate the traffic flow being controlled by the state of
traffic signal either GREEN or RED.

There are two threads in the program, targeting two different functions. The signal_state()
function periodically sets and resets the event indicating change of signal from GREEN to
RED.

The traffic_flow() function waits for the event to be set, and runs a loop till it remains set'''

from threading import Event, Thread
import time
terminate = False
def signal_state():
    global terminate
    while not terminate:
        time.sleep(0.5)
        print("Traffic Police Giving GREEN Signal")
        event.set()
        time.sleep(1)
        print("Traffic Police Giving RED Signal")
        event.clear()

def traffic_flow():
    global terminate
    num = 0
    while num < 10 and not terminate:
        print("Waiting for GREEN Signal")
        event.wait()
        print("GREEN Signal ... Traffic can move")
        while event.is_set() and not terminate:
            num += 1
            print("Vehicle No:", num," Crossing the Signal")
            time.sleep(1)
        print("RED Signal ... Traffic has to wait")


event = Event()
t1 = Thread(target=signal_state)
t2 = Thread(target=traffic_flow)
t1.start()
t2.start()
# Terminate the threads after some time
time.sleep(5)
terminate = True
# join all threads to complete
t1.join()
t2.join()

''' The Condition Object
The Condition object in Python's threading module provides a more advanced
synchronization mechanism. It allows threads to wait for a notification from another thread
before proceeding. The Condition object are always associated with a lock and provide
mechanisms for signaling between threads.

Syntax:- threading.Condition(lock=None)

Below are the key methods of the Condition object −
     acquire(*args): Acquire the underlying lock. This method calls the corresponding
        method on the underlying lock; the return value is whatever that method returns.
     release(): Release the underlying lock. This method calls the corresponding
        method on the underlying lock; there is no return value.
     wait(timeout=None): This method releases the underlying lock, and then blocks
        until it is awakened by a notify() or notify_all() call for the same condition 
        variable in another thread, or until the optional timeout occurs. Once awakened or timed
        out, it re-acquires the lock and returns.
     wait_for(predicate, timeout=None): This utility method may call wait()
        repeatedly until the predicate is satisfied, or until a timeout occurs. The return
        value is the last return value of the predicate and will evaluate to False if the
        method timed out.
     notify(n=1): This method wakes up at most n of the threads waiting for the
        condition variable; it is a no-op if no threads are waiting.
     notify_all(): Wake up all threads waiting on this condition. This method acts like
        notify(), but wakes up all waiting threads instead of one. If the calling thread has
        not acquired the lock when this method is called, a RuntimeError is raised.
        
Example
This example demonstrates a simple form of inter-thread communication using the
Condition object of the Python's threading module. Here thread_a and thread_b are
communicated using a Condition object, the thread_a waits until it receives a notification
from thread_b. the thread_b sleeps for 2 seconds before notifying thread_a and then
finishes.'''

from threading import Condition, Thread
import time
c = Condition()
def thread_a():
    print("Thread A started")
    with c:
        print("Thread A waiting for permission...")
        c.wait()
        print("Thread A got permission!")
    print("Thread A finished")

def thread_b():
    print("Thread B started")
    with c:
        time.sleep(2)
        print("Notifying Thread A...")
        c.notify()
    print("Thread B finished")
Thread(target=thread_a).start()
Thread(target=thread_b).start()

''' Example
Here is another code demonstrating how the Condition object is used for providing the
communication between threads. The thread t2 runs the taskB() function, and the thread
t1 runs the taskA() function. The t1 thread acquires the condition and notifies it.
By that time, the t2 thread is in a waiting state. After the condition is released, the waiting
thread proceeds to consume the random number generated by the notifying function.'''

from threading import Condition, Thread
import time
import random
numbers = []
def taskA(c):
    for _ in range(5):
        with c:
            num = random.randint(1, 10)
            print("Generated random number:", num)
            numbers.append(num)
            print("Notification issued")
            c.notify()
        time.sleep(0.3)
        print("------------------")
def taskB(c):
    for i in range(5):
        with c:
            print("waiting for update")
            while not numbers:
                c.wait()
            print("Obtained random number", numbers.pop())
        time.sleep(0.3)
        print("=====================")

c = Condition()
t1 = Thread(target=taskB, args=(c,))
t2 = Thread(target=taskA, args=(c,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Done")

'''----------------------------------- Python - Thread Deadlock ------------------------------
A deadlock may be described as a concurrency failure mode. It is a situation in a program
where one or more threads wait for a condition that never occurs. As a result, the threads
are unable to progress and the program is stuck or frozen and must be terminated
manually.
Deadlock situation may arise in many ways in your concurrent program. Deadlocks are
not developed intentionally, instead, they are a side effect or bug in the code.
Common causes of thread deadlocks are listed below −
     A thread that attempts to acquire the same mutex lock twice.
     Threads that wait on each other (e.g. A waits on B, B waits on A).
     When a thread that fails to release a resource such as lock, semaphore, condition,
        event, etc.
     Threads that acquire mutex locks in different orders (e.g. fail to perform lock
        ordering).'''

'''How to Avoid Deadlocks in Python Threads?
When multiple threads in a multi-threaded application attempt to access the same
resource, such as performing read/write operations on the same file, it can lead to data
inconsistency. Therefore, it is important to synchronize concurrent access to resources by
using locking mechanisms.
'''

''' Locking Mechanism with the Lock Object
An object of the Lock class has two possible states − locked or unlocked, initially in
unlocked state when first created. A lock doesn't belong to any particular thread.
The Lock class defines acquire() and release() methods.

The acquire() Method
The acquire() method of the Lock class changes the lock's state from unlocked to locked.
It returns immediately unless the optional blocking argument is set to True, in which case
it waits until the lock is acquired.
Syntax:- Lock.acquire(blocking, timeout)
Where,
     blocking − If blocking is set to false, the thread will not be blocked. To block a
        thread, set the variable to true.
     timeout − Specifies a timeout period for acquiring the lock.
The return value of this method is True if the lock is acquired successfully; False if not.'''

''' The release() Method
When the state is locked, this method in another thread changes it to unlocked. This can
be called from any thread, not only the thread which has acquired the lock

Syntax:- Lock.release()

The release() method should only be called in the locked state. If an attempt is made to
release an unlocked lock, a RuntimeError will be raised.
When the lock is locked, reset it to unlocked, and return. If any other threads are blocked
and waiting for the lock to become unlocked, it allows exactly one of them to proceed.
There is no return value of this method.

Example
In the following program, two threads try to call the synchronized() method. One of them
acquires the lock and gains the access while the other waits. When the run() method is
completed for the first thread, the lock is released and the synchronized method is
available for second thread.

When both the threads join, the program comes to an end.'''

from threading import Thread, Lock
import time
lock=Lock()
threads=[]
class myThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name=name
    def run(self):
        lock.acquire()
        synchronized(self.name)
        lock.release()

def synchronized(threadName):
    print ("{} has acquired lock and is running synchronized method".format(threadName))
    counter=5
    while counter:
        print ('**', end='')
        time.sleep(2)
        counter=counter-1
    print('\nlock released for', threadName)

t1=myThread('Thread1')
t2=myThread('Thread2')
t1.start()
threads.append(t1)
t2.start()
threads.append(t2)
for t in threads:
    t.join()
print ("end of main thread")

''' Semaphore Object for Synchronization
In addition to locks, Python threading module supports semaphores, which offering
another synchronization technique. It is one of the oldest synchronization techniques
invented by a well-known computer scientist, Edsger W. Dijkstra.

The basic concept of semaphore is to use an internal counter which is decremented by
each acquire() call and incremented by each release() call. The counter can never go below
zero; when acquire() finds that it is zero, it blocks, waiting until some other thread calls
release().

The Semaphore class in threading module defines acquire() and release() methods.
'''

''' The acquire() Method
If the internal counter is larger than zero on entry, decrement it by one and return True
immediately.

If the internal counter is zero on entry, block until awoken by a call to release(). Once
awoken (and the counter is greater than 0), decrement the counter by 1 and return True.
Exactly one thread will be awoken by each call to release(). The order in which threads
awake is arbitrary.

If blocking parameter is set to False, do not block. If a call without an argument would
block, return False immediately; otherwise, do the same thing as when called without
arguments, and return True.

The release() Method
Release a semaphore, incrementing the internal counter by 1. When it was zero on entry
and other threads are waiting for it to become larger than zero again, wake up n of those
threads.

Example
This example demonstrates how to use a Semaphore object in Python to control access to
a shared resource among multiple threads, for avoiding deadlock in Python's multi-
threaded program.'''

from threading import *
import time
# creating thread instance where count = 3
lock = Semaphore(4)
# creating instance
def synchronized(name):
    # calling acquire method
    lock.acquire()
    for n in range(3):
        print('Hello! ', end = '')
        time.sleep(1)
        print( name)
        # calling release method
        lock.release()
# creating multiple thread
thread_1 = Thread(target = synchronized , args = ('Thread 1',))
thread_2 = Thread(target = synchronized , args = ('Thread 2',))
thread_3 = Thread(target = synchronized , args = ('Thread 3',))
# calling the threads
thread_1.start()
thread_2.start()
thread_3.start()

'''-------------------------------- Python - Interrupting a Thread -----------------------
Interrupting a thread in Python is a common requirement in multi-threaded programming,
where a thread's execution needs to be terminated under certain conditions. In a multi-
threaded program, a task in a new thread, may be required to be stopped. This may be
for many reasons, such as − task completion, application shutdown, or other external
conditions.

In Python, interrupting threads can be achieved using threading.Event or by setting a
termination flag within the thread itself. These methods allow you to interrupt the threads
effectively, ensuring that resources are properly released and threads exit cleanly.'''

''' Thread Interruption using Event Object
One of the straightforward ways to interrupt a thread is by using the threading.Event class.
This class allows one thread to signal to another that a particular event has occurred.
Here's how you can implement thread interruption using threading.Event

Example
In this example, we have a MyThread class. Its object starts executing the run() method.
The main thread sleeps for a certain period and then sets an event. Till the event is
detected, loop in the run() method continues. As soon as the event is detected, the loop
terminates.'''

from time import sleep
from threading import Thread
from threading import Event
class MyThread(Thread):
    def __init__(self, event):
        super(MyThread, self).__init__()
        self.event = event
    def run(self):
        i=0
        while True:
            i+=1
            print ('Child thread running...',i)
            sleep(0.5)
            if self.event.is_set():
                break
            print()
        print('Child Thread Interrupted')

event = Event()
thread1 = MyThread(event)
thread1.start()
sleep(3)
print('Main thread stopping child thread')
event.set()
thread1.join()

''' Thread Interruption using a Flag
Another approach to interrupting threads is by using a flag that the thread checks at
regular intervals. This method involves setting a flag attribute in the thread object and
regularly checking its value in the thread's execution loop.

Example
This example demonstrates how to use a flag to control and stop a running thread in
Python multithreaded program.'''
import threading
import time
def foo():
    t = threading.current_thread()
    while getattr(t, "do_run", True):
        print("working on a task")
        time.sleep(1)
    print("Stopping the Thread after some time.")
# Create a thread
t = threading.Thread(target=foo)
t.start()
# Allow the thread to run for 5 seconds
time.sleep(5)
# Set the termination flag to stop the thread
t.do_run = False