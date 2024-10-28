# Create python virtual environment
```bash
python -m venv venv
```

# Activate python virtual environment
**Note: ** you must activate the environment everytime you open the project
```bash
source venv/bin/activate
```
# Install dependencies
```bash
pip install fastapi uvicorn websockets
```

# Run application
```bash
uvicorn main:app --reload
```

# Open URL in browser 
http://127.0.0.1:8000/static/index.html