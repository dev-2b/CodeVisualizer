from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import ParseRequest
from parsers import factory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/parse")
async def parse_code(request: ParseRequest):
    return factory.get_visualisation(request.files, request.visualization_type)