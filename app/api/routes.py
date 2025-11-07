from fastapi import APIRouter, UploadFile, File
from app.controllers.pdf_controller import handle_pdf_upload
from app.controllers.ask_controller import handle_ask_request
from pydantic import BaseModel
router = APIRouter(prefix='/api', tags=["PDF"])

@router.post("/upload")
async def upload_pdf(file: UploadFile=File(...)):
    return await handle_pdf_upload(file)

class AskRequest(BaseModel):
    query: str
    collection_name: str
    session_id: str | None = None
    document_id: str | None = None

@router.post("/ask")
async def ask_pdf(request: AskRequest):
    return await handle_ask_request(
        query=request.query,
        collection_name=request.collection_name,
        session_id=request.session_id,
        document_id=request.document_id,
    )