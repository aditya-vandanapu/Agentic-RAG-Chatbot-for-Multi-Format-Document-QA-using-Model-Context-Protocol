from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from utils.mcp import create_mcp_message

class RetrievalAgent:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.chunk_map = []

    def embed_chunks(self, chunks):
        texts = [c["content"] for c in chunks]
        vectors = self.model.encode(texts)
        self.index = faiss.IndexFlatL2(vectors.shape[1])
        self.index.add(np.array(vectors))
        self.chunk_map = chunks

    def retrieve(self, query):
        query_vec = self.model.encode([query])
        D, I = self.index.search(query_vec, k=3)
        results = [self.chunk_map[i] for i in I[0]]
        return create_mcp_message(
            sender="RetrievalAgent",
            receiver="LLMResponseAgent",
            msg_type="RETRIEVAL_RESULT",
            payload={"retrieved_context": results, "query": query}
        )
