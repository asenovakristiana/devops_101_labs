import socket
from typing import Dict
import uvicorn
from fastapi import FastAPI
from datetime import datetime
import os
import yaml


def load_yaml_config(file_path: str) -> Dict:
    """ Load yaml configuration file. If file doesn't exist, return empty dict """
    config = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            config = yaml.load(file.read(), Loader=yaml.FullLoader)
    
    return config

# Load config file if exist
config=load_yaml_config("config.yaml")

# Load environment variable
env_var = os.environ.get('MY_APP_ENV_VAR')

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello World", 
        "time": datetime.now(), 
        "hostname": socket.gethostname(),
        "config": config,
        "environment_variable": env_var
        }

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)