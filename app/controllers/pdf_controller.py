from fastapi import UploadFile
from app.services.pdf_service import extract_text_from_pdf

async def handle_pdf_upload(file: UploadFile):
    text = await extract_text_from_pdf(file)
    return {
        "filename": file.filename,
        "text_length": len(text),
        "preview": text[:300]  # primeras 300 letras
    }

    