from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# Beide Funktionen aus der parser.py importieren
from parser import get_ast, extract_classes_to_visjs

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

class CodeRequest(BaseModel):
    code: str

@app.post("/api/parse")
def parse_java_code(request: CodeRequest):
    # 1. AST generieren (Issue #5 Logik nutzen)
    root_node = get_ast(request.code)
    
    # 2. Daten extrahieren und formatieren (Issue #6 Logik nutzen)
    result = extract_classes_to_visjs(root_node)
    
    # 3. An das Frontend zurücksenden
    return result