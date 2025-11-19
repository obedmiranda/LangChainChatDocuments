from app.chains.qa_service import run_qa_chain

async def handle_ask_request(query: str, collection_name: str, session_id: str = None, document_id: str = None):
    try:

        real_collection_name = f"{collection_name}_{document_id}" if document_id else collection_name

        print("📩 ASK RECEIVED:", {
            "query": query,
            "collection": real_collection_name,
            "session_id": session_id,
            "document_id": document_id
        })

        qa_response = await run_qa_chain(query, real_collection_name)

        answer = qa_response.get("answer", "🤖 No response generated.")
        sources = qa_response.get("sources", [])

        print(f"🧠 Answer: {answer[:150]}...") 
        print(f"📚 Retrieved {len(sources)} source chunks")

        return {
            "query": query,
            "collection": real_collection_name,
            "session_id": session_id,
            "document_id": document_id,
            "reply": answer,
            "results": sources
        }

    except Exception as e:
        print("Error in handle_ask_request:", e)
        return {
            "error": str(e),
            "message": "Error generating answer from chain."
        }
