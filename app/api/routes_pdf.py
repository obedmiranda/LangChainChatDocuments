from fastapi import APIRouter, UploadFile, File
from app.utils.file_loader import extract_text_from_pdf

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(await file.read())
    return {"filename": file.filename, "content_length": len(text)}
