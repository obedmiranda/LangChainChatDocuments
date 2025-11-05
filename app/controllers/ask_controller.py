from app.services.retrieval_service import retrieve_relevant_chunks

async def handle_ask_request(query: str, collection_name: str):
    try:
        results = await retrieve_relevant_chunks(query, collection_name)

        return {
            "query": query,
            "collection": collection_name,
            "results": results
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "Error retrieving relevant chunks."
        }