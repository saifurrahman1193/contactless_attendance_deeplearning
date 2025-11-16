### Command: Docker Compose Setup 
```
sudo docker-compose down
sudo docker-compose build && docker-compose up -d
```

---

### 🌐 Access: 
Visit → [http://localhost:83](http://localhost:83)

API Docs → [http://localhost:83/docs](http://localhost:83/docs)

---


### version
| Tech         | Version |
| ------------ | ------- |
| Python       | 3.13.5  |
| FastAPI      | 0.116.1 |
| Uvicorn      | 0.35.0  |
| PostgreSQL   | 16.4    |
| Asyncpg      | 0.30.0  |
| SQLAlchemy   | 2.0.41  |
| Pydantic     | 2.11.7  |
| Pandas       | 2.3.1   |
| NumPy        | 2.3.2   |
| Scikit-learn | 1.7.1   |


### Version check
```
python --version
uvicorn --version
psql --version
python -c "import fastapi; print(fastapi.__version__)"
python -c "import asyncpg; print(asyncpg.__version__)"
python -c "import sqlalchemy; print(sqlalchemy.__version__)"
python -c "import pydantic; print(pydantic.__version__)"
python -c "import pandas; print(pandas.__version__)"
python -c "import numpy; print(numpy.__version__)"
python -c "import sklearn; print(sklearn.__version__)"
```


## DB Connection check
```
python database.py
```

---

### ✅ Project Structure

```
.
├── main.py
├── routes/
│   └── datascience.py
├── controllers/
│   └── datascience_controller.py
├── schemas/
│   └── datascience.py
├── database.py
├── .env
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

# Dependencies installed
```
pip install fastapi uvicorn[standard] asyncpg sqlalchemy pydantic python-dotenv pandas numpy scikit-learn
```
















To ensure your FastAPI application runs **indefinitely** on Windows Server, automatically **restarts if stopped**, and **launches on system reboot**, follow these methods:

---

### **Method 1: Windows Task Scheduler (Built-in)**

#### **Step 2: Set Up Task Scheduler**
1. Open **Task Scheduler** → **Create Task**.
2. **General Tab**:
   - Name: `FastAPI_Autostart`
   - Check: *Run whether user is logged on or not* (runs in background).
   - Check: *Run with highest privileges* (if using port 80).
3. **Triggers Tab**:
   - Add trigger: *At startup*.
4. **Actions Tab**:
   - Action: *Start a program*.
   - Program: `cmd.exe`
   - Arguments: `/c cd /d D:\project\wintext_ds && uvicorn main:app --host 0.0.0.0 --port 83`
5. **Settings Tab**:
   - Check: *Allow task to be run on demand*.
   - Check: *Restart the task if it fails* (set to restart every 1 minute).

#### **Step 3: Test**
- Reboot the server → The task should auto-start FastAPI.

---

### **Comparison Table**
| Method | Pros | Cons |
|--------|------|------|
| **Task Scheduler** | Built into Windows | Less robust for crashes |
| **NSSM** | Runs as a proper service | Requires manual setup |
| **PM2** | Easy logging/restarts | Needs Node.js installed |
| **Docker** | Best isolation/portability | Requires Docker setup |

---
