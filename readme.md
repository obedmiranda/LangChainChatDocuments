# 📄 PDF Chat Backend

This backend powers **PDF Chat**, an intelligent document-processing service that allows users to upload PDFs, automatically extract and embed their content using **LangChain**, and store those embeddings in a **PostgreSQL + PGVector** database for semantic search and context-based retrieval.

---

## 🚀 Overview

The project implements an **end-to-end pipeline** for processing and indexing documents using the LangChain ecosystem.

### ✅ Current features
- Upload and read PDF files via FastAPI endpoints.  
- Extract text from PDFs using `PyMuPDF` (`fitz`).  
- Split large documents into chunks with `RecursiveCharacterTextSplitter`.  
- Generate embeddings for each chunk using `OpenAIEmbeddings`.  
- Persist embeddings in **PostgreSQL** using **LangChain PGVector**.  
- Attach useful metadata (`session_id`, `document_id`, `source`) for tracking and filtering.  
- Query and inspect stored embeddings directly from the database.

---

## ⚙️ Coming next

### 🔄 Incremental Indexing & Change Tracking
We’ll integrate the **LangChain Indexing API** using `RecordManager` to:
- Track which documents were already indexed.
- Detect changes and re-embed only updated content.
- Prevent duplicate records inside the vector store.
- Enable incremental cleanup with `cleanup="incremental"` mode.

### 🧠 Semantic Retrieval Endpoint (`/ask`)
An `/ask` route will be added to:
- Accept a user query.
- Perform semantic search over the embeddings (via `similarity_search()`).
- Retrieve top-matching chunks.
- Feed the context to an LLM for accurate answers.

### 🧩 Dynamic Database Setup
Right now, the database connection is **hardcoded** inside the service layer:
```python
connection="postgresql+psycopg://obedmirandapicado:password@localhost:5432/pdf_chat"
In the next update, this will be replaced by an environment-driven configuration using:
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/pdf_chat
and loaded through .env for portability and production deployment.

Project Structure

app/
├── api/
│   └── routes.py               # FastAPI routes definitions
├── controllers/
│   └── pdf_controller.py       # Upload handler and process orchestration
├── services/
│   ├── pdf_service.py          # Extract text from PDF
│   ├── text_splitter.py        # Chunking logic
│   └── embedding_service.py    # Embedding generation + PGVector storage
├── utils/
│   └── pdf_utils.py            # Helper functions (PDF reading)
└── main.py                     # FastAPI app entrypoint

| Layer                  | Technology                     |
| ---------------------- | ------------------------------ |
| Framework              | FastAPI                        |
| Embeddings             | LangChain + OpenAIEmbeddings   |
| Vector Store           | PGVector (PostgreSQL)          |
| Document Parsing       | PyMuPDF (`fitz`)               |
| Chunking               | RecursiveCharacterTextSplitter |
| ORM / DB Connection    | SQLAlchemy + psycopg           |
| Environment Management | python-dotenv                  |


Example Flow

Upload a PDF

POST /api/upload


Reads and extracts text from the uploaded file.

Splits into chunks and generates embeddings.

Stores results in pdf_embeddings collection inside pdf_chat database.

Returns a unique session_id.

Inspect data in PostgreSQL

SELECT document, cmetadata
FROM langchain_pg_embedding
LIMIT 5;


Next phase

Build /ask endpoint to enable semantic Q&A using the stored embeddings.

🧩 Future Enhancements

Full Indexing API support for change tracking (RecordManager).

Multi-format support (Word, text, emails).

Authentication layer (JWT / API key).

