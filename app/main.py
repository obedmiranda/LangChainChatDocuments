from fastapi import FastAPI
from app.api import routes_pdf, routes_embeddings

app = FastAPI(title="PDF Chat")

app.include_router(routes_pdf.router, prefix="/pdf", tags=["PDF"])
app.include_router(routes_embeddings.router, prefix="/embeddings", tags=["Embeddings"])

@app.get("/")
def root():
    return {"message": "Welcome to PDF Chat API"}
