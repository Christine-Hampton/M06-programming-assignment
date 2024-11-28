#15.1 use multiprocessing to create 3 seperate processes. 
import multiprocessing
import time
from datetime import datetime
import random

def worker():
    # Wait for a random amount of time between 0 and 1 second
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    # Print the current time
    print(f"Process ID: {multiprocessing.current_process().pid}, Current Time: {datetime.now()}")

if __name__ == "__main__":
    # Create a list to hold the process objects
    processes = []
    
    # Create and start 3 separate processes
    for _ in range(3):
        process = multiprocessing.Process(target=worker)
        processes.append(process)
        process.start()
    
    # Ensure all processes complete
    for process in processes:
        process.join()