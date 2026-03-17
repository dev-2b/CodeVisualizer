from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Hier wird die Variable "app" erstellt, nach der Uvicorn sucht
app = FastAPI()

# CORS-Konfiguration: Erlaubt dem Frontend (das auf einem anderen Port läuft) 
# später Anfragen an dieses Backend zu senden.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ein simpler Test-Endpunkt
@app.get("/")
def read_root():
    return {"status": "Das FastAPI Backend läuft erfolgreich!"}
