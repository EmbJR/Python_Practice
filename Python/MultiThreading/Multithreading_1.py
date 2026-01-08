import _thread
import time

def print_name(name, *arg):
    while(True):
        print(name, *arg)
        time.sleep(3)

name="Tutorialspoint..."

_thread.start_new_thread(print_name, (name, 1))
_thread.start_new_thread(print_name, (name, 1, 2))

tempVal = 10
while(tempVal > 0):
    time.sleep(5)
    print("Main Part---", tempVal)
    tempVal -= 1