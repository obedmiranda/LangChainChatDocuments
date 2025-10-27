from fastapi import UploadFile
from app.utils.pdf_utils import read_pdf_content

async def extract_text_from_pdf(file: UploadFile) -> str:
    content = await file.read()
    text = read_pdf_content(content)
    return text