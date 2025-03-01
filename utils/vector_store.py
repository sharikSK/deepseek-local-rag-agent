from langchain_qdrant import QdrantVectorStore
from agno.models.ollama import Ollama
from typing import List

class OllamaEmbedder:
    def __init__(self, model_name="snowflake-arctic-embed"):
        self.embedder = Ollama(id=model_name, dimensions=1024)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self.embed_query(text) for text in texts]

    def embed_query(self, text: str) -> List[float]:
        return self.embedder.get_embedding(text)

def create_vector_store(client, texts):
    try:
        vector_store = QdrantVectorStore(
            client=client,
            collection_name="my_collection",
            embedding=OllamaEmbedder()
        )
        
        vector_store.add_documents(texts)
        return vector_store
    except Exception as e:
        print(f"🔴 Vector store error: {str(e)}")
        return None

def check_document_relevance(query: str, vector_store, threshold: float = 0.7):
    if not vector_store:
        return False, []
        
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 5, "score_threshold": threshold}
    )
    docs = retriever.invoke(query)
    return bool(docs), docs
