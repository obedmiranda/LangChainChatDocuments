from fastapi import APIRouter, UploadFile, File
from app.controllers.pdf_controller import handle_pdf_upload

router = APIRouter(prefix='/api', tags=["PDF"])

@router.post("/upload")
async def upload_pdf(file: UploadFile=File(...)):
    return await handle_pdf_upload(file)
   