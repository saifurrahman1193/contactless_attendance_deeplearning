from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import routes  # This should contain `register_routes(app)`

app = FastAPI(title="Data Science API", version="1.0")

# ✅ Allow all CORS (not recommended for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routes
routes.register_routes(app)
