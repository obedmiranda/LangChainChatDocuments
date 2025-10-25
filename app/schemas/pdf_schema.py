from pydantic import BaseModel

class PDFResponse(BaseModel):
    filename: str
    content_length: int
