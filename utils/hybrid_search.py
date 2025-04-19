from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class HybridSearch:
    def __init__(self, documents: list[str]):
        self.documents = documents
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.embedding_model.encode(documents, convert_to_tensor=True)
        self.vectorizer = TfidfVectorizer().fit(documents)
        self.keyword_matrix = self.vectorizer.transform(documents)

    def search(self, query: str, top_k=3):
        query_embedding = self.embedding_model.encode(query, convert_to_tensor=True)
        sem_scores = util.pytorch_cos_sim(query_embedding, self.embeddings)[0].cpu().numpy()
        key_scores = self.keyword_matrix.dot(self.vectorizer.transform([query]).T).toarray().flatten()
        hybrid_scores = sem_scores + key_scores
        top_indices = hybrid_scores.argsort()[::-1][:top_k]
        return [self.documents[i] for i in top_indices]
