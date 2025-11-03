import uuid
from fastapi import UploadFile
from app.services.pdf_service import extract_text_from_pdf
from langchain_postgres.vectorstores import PGVector
from langchain_openai import OpenAIEmbeddings
from app.utils.text_splitter_utils import text_splitter
from app.services.embedding_service import store_embeddings

async def handle_pdf_upload(file: UploadFile):
    text = await extract_text_from_pdf(file)
    session_id = str(uuid.uuid4())
    document_id = str(uuid.uuid4())
    chunks = text_splitter(text)
    result_embedding = await store_embeddings(chunks, session_id,document_id)
    print(result_embedding)
    return {
        "filename": file.filename,
        "text_length": len(text),
        "preview": text[:300]  # primeras 300 letras
    }

    