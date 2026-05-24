from functools import lru_cache

from sentence_transformers import SentenceTransformer, util


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def get_model() -> SentenceTransformer:
    return SentenceTransformer(MODEL_NAME)


def calculate_similarity(word1: str, word2: str) -> tuple[float, float]:
    model = get_model()
    embeddings = model.encode([word1.strip(), word2.strip()], convert_to_tensor=True)
    similarity_score = float(util.cos_sim(embeddings[0], embeddings[1]).item())
    normalized_score = max(0.0, min(1.0, similarity_score))
    similarity_percent = round(normalized_score * 100, 2)
    return round(similarity_score, 4), similarity_percent