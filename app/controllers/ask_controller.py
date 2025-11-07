from app.services.retrieval_service import retrieve_relevant_chunks

async def handle_ask_request(query: str, collection_name: str, session_id: str = None, document_id: str = None):
    try:
       
        real_collection_name = f"{collection_name}_{document_id}" if document_id else collection_name

        print("📩 ASK RECEIVED:", {
            "query": query,
            "collection": real_collection_name,
            "session_id": session_id,
            "document_id": document_id
        })

        results = await retrieve_relevant_chunks(query, real_collection_name)

        print(f"📚 Retrieved {len(results)} chunks from {real_collection_name}")

        return {
            "query": query,
            "collection": real_collection_name,
            "session_id": session_id,
            "document_id": document_id,
            "results": results
        }

    except Exception as e:
        print("❌ Error in handle_ask_request:", e)
        return {
            "error": str(e),
            "message": "Error retrieving relevant chunks."
        }
