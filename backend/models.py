from pydantic import BaseModel
from typing import List

# Repräsentiert eine einzelne Datei aus dem Editor
class CodeFile(BaseModel):
    filename: str
    code: str
    language: str

# Repräsentiert den gesamten Request, der an /api/parse geschickt wird
class ParseRequest(BaseModel):
    visualization_type: str
    files: List[CodeFile]