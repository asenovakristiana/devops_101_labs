import os
import threading
import time


# Define a function that the threads will run
def thread_function(name):
    print(f"Thread {name} starting")
    for i in range(30):
        time.sleep(10)  # Simulate work with sleep
        print(f"Print from thread {name}")
    print(f"Thread {name} finishing")

print(f"Show threads on OS level: ps -T -p {os.getpid()}")

# Create two threads
thread1 = threading.Thread(target=thread_function, args=(1,))
thread2 = threading.Thread(target=thread_function, args=(2,))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()