from pydantic import BaseModel

class DetectRequest(BaseModel):
    text: str  # Example: "Bonjour tout le monde"
