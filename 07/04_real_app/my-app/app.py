import socket
import uvicorn
from fastapi import FastAPI, HTTPException
from datetime import datetime
import multiprocessing
import os
from typing import Dict
import yaml

# This var will be used to simulate failure
HEALTH=True

def load_yaml_config(file_path: str) -> Dict:
    """ Load yaml configuration file. If file doesn't exist, return empty dict """
    config = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            config = yaml.load(file.read(), Loader=yaml.FullLoader)
    
    return config

# Load config file if exist
config=load_yaml_config("config.yaml")

app = FastAPI()

@app.get("/health")
async def health():
    if HEALTH:
        return {
            "status": "True", 
        }
    else:
        raise HTTPException(status_code=500, detail="Ooops! I need Aspirin!")

# Please don't do this in your app. It is dangerous to expose env vars to clients! 
# This is just for demo purpose
@app.get("/env_vars")
async def list_env_vars():
    return os.environ


@app.put("/fail")
async def fail():
    global HEALTH
    HEALTH = not HEALTH

@app.put("/simulate-memory-leak")
def simulate_memory_leak():
    leaky_objects = [] 
    while True:
        leaky_objects.append([0] * (10**6)) 
        print(f"Leaked objects count: {len(leaky_objects)}")


@app.put("/simulate-cpu-stress")
def simulate_cpu_stress():
    def cpu_stress():
        while True:
            pass  # Infinite loop to keep the CPU busy
        
    cpu_count = multiprocessing.cpu_count()
    print(f"Starting {cpu_count} processes to max out the CPU.")
    processes = []

    # Start a process for each CPU core
    for _ in range(cpu_count):
        process = multiprocessing.Process(target=cpu_stress)
        process.start()
        processes.append(process)

    # Keep the main thread alive
    for process in processes:
        process.join()

@app.get("/")
async def root():
    return {
        "message": "Hello World", 
        "time": datetime.now(), 
        "hostname": socket.gethostname(),
        "config": config
    }

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)