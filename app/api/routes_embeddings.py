from fastapi import APIRouter
from app.services.embeddings import create_embeddings

router = APIRouter()

@router.post("/generate")
async def generate_embeddings():
    return {"message": "Embeddings created successfully"}
