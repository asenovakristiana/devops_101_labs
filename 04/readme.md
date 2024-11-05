# Environment Variables
## Review 01_environment_variables.py
```bash
cat 01_environment_variables.py
```

## Run main.py with provided environment variables
```
USERNAME=Bobby python 01_environment_automation.py
```

# Configuration file
## Review 02_config_file.py and config.json
```bash
cat 02_config_file.py
cat 02_config_file.json
```

## Run 02_config_file.py
```
python 02_config_file.py
```


# Simple Web App
## Create python virtual environment
```bash
python -m venv .venv
```

## Activate python virtual environment
**Note: ** you must activate the environment everytime you open the project
```bash
source .venv/bin/activate
```
## Install dependencies
* Install streamlit - a simple library for python used to build quckly UI
```bash
pip install streamlit
```

## Run web app
```bash
streamlit run 03_simple_web_app.py
```

# Simple Web App with DB
## Ensure .venv is create from the previous steps

## Activate python virtual environment
**Note: ** you must activate the environment everytime you open the project
```bash
source .venv/bin/activate
```
## Install dependencies
* Install streamlit - a simple library for python used to build quckly UI
```bash
pip install sqlalchemy
```

## Run web app
```bash
streamlit run 04_simple_web_app.py
```


# Simple Pub/Sub app
## Ensure .venv is create from the previous steps

## Activate python virtual environment
**Note: ** you must activate the environment everytime you open the project
```bash
source .venv/bin/activate
```
## Install dependencies
* Install streamlit - a simple library for python used to build quckly UI
```bash
pip install persist-queue
```

## Run simple queue subscriber
```bash
python 05_simple_queue_subscriber.py
```

## Run simple queue publisher
**Note:** You need to open first another terminal
```bash
streamlit run 05_simple_queue_publisher.py
```

# Show threads on OS level
## Run 
```bash
streamlit run 06_threads.py
```
## Copy the the command from the initial log msessage
Show threads on OS level: ps -T -p XXXXXX

## Execute the command in another terminal
```bash
ps -T -p XXXXXX
```