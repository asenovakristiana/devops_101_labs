


# worker.py
from persistqueue import SQLiteQueue as Queue
import time

# Connect to the queue
queue = Queue("message_queue", auto_commit=True)

print("Worker is listening for messages...")

# Continuously check for new messages
while True:
    message = queue.get()
    print("Received message:", message)