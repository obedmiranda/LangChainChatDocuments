from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres.vectorstores import PGVector
load_dotenv()  # carga variables desde .env

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
    embeddings = embedding_model.embed_documents([doc.page_content for doc in docs])
    # print("Primer embedding:", embeddings[0][:5])  # imprime los primeros 5 valores

    PGVector.from_documents(
        documents=docs,
        embedding=embedding_model,
        connection="postgresql+psycopg://obedmirandapicado:obed12345@localhost:5432/pdf_chat",
        collection_name="pdf_embeddings"
    )


    return {
    "message": "Embeddings stored successfully",
    "chunks_indexed": len(docs)
}
