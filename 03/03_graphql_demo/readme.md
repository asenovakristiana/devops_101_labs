# Create python virtual environment
```bash
python -m venv .venv
```

# Activate python virtual environment
**Note: ** you must activate the environment everytime you open the project
```bash
source .venv/bin/activate
```
# Install dependencies
```bash
pip install --upgrade pip  
pip install fastapi aiosqlite sqlalchemy databases 
pip install 'strawberry-graphql[fastapi]'
```

# Run application
```bash
uvicorn main:app --reload
```

# Execute example query
```bash
curl -X POST http://127.0.0.1:8000/graphql \
-H "Content-Type: application/json" \
-d '{
  "query": "query { movies(where: {year: 2008, director: \"Christopher Nolan\"}) { title } }"
}'
```

# Open GraphQL playground
Open in browser http://127.0.0.1:8000/graphql