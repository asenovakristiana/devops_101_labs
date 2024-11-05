import os
import asyncio

# Define an asynchronous function
async def async_task(name):
    print(f"Async task {name} starting")
    for _ in range(30):
        # Simulate async work with sleep
        await asyncio.sleep(10) 
        print(f"Print from async call {name}")
    print(f"Async task {name} finishing")

# Main function to run asynchronous tasks
async def main():
    # Create and run two asynchronous tasks concurrently
    task1 = asyncio.create_task(async_task(1))
    task2 = asyncio.create_task(async_task(2))

    # Wait for both tasks to complete
    await task1
    await task2

print(f"Show threads on OS level: ps -T -p {os.getpid()}")

# Run the main function
asyncio.run(main())