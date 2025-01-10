# Create venv and install dependencies
```bash
python -m vevn venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# Run unit test
* Enter lab dir
```bash
cd 1_unit_test
```

* Review calculator.py and tests
```bash
cat calculator.py
cat test_calculator.py
```

* Run pytest
```bash
pytest
```

* Return to parent dir
```bash
cd ..
```

# Run integration test
* Enter lab dir
```bash
cd 2_integration_test
```

* Review main.py and tests
```bash
cat main.py
cat test_items.py
cat test_status.py
```

* Run service in background
```bash
python main.py &
```

* Run pytest
```bash
pytest
```

* Stop background service
```bash
fg
# Then run
CTRL+C
```

* Return to parent dir
```bash
cd ..
```

# Run E2E tests
* Enter lab dir
```bash
cd 3_e2e_tests
```

* Review main.py and tests
```bash
cat main.py
cat test_add_todo.py
```

* Run service in background
```bash
python main.py &
```

* Install playwright and run pytest
```bash
playwright install
pytest
```

* Stop background service
```bash
fg
# Then run
CTRL+C
```

* Return to parent dir
```bash
cd ..
```

# Run testcontainers
* Enter lab dir
```bash
cd 4_testcontainers
```

* Review main.py and tests
```bash
cat main.py
cat test_items.py
```

* Run pytest
```bash
pytest
```


* Return to parent dir
```bash
cd ..
```