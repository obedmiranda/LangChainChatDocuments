from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres.vectorstores import PGVector

load_dotenv()

async def store_embeddings(chunks: list[str], session_id: str, document_id: str):
    docs = [
        Document(
            page_content=chunk,
            metadata={
                "session_id": session_id,
                "document_id": document_id,
                "source": "pdf"
            }
        )
        for chunk in chunks
    ]

    embedding_model = OpenAIEmbeddings()
    
    PGVector.from_documents(
        documents=docs,
        embedding=embedding_model,
        connection=os.getenv("PGVECTOR_URL"),
        collection_name=f"pdf_embeddings_{document_id}",
        use_jsonb=True
    )

    return {
        "message": "Embeddings stored successfully",
        "chunks_indexed": len(docs)
    }
