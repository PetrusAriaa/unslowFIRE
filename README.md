### Basic Setup
- Using pip
```bash
    pip install -r requirements.txt
```
- Using pipenv
```bash
    pipenv shell && pipenv sync
```

### Run server
```bash
    uvicorn main:app --port 3001 --reload
```