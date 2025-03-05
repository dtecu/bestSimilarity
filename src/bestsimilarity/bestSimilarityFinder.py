import typing
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def findBestSimilarity(reference: str, other: typing.List[str]):
    # Decided on SentenceTransformer as it is better suited for sentence embeddings (rather than word embeddings)
    encoder = SentenceTransformer('all-MiniLM-L6-v2')

    referenceEmbedding = encoder.encode([reference])
    otherEmbeddings = encoder.encode(other)
    similarity = cosine_similarity(referenceEmbedding, otherEmbeddings)

    # index will be an ndarray with 1 single element: 
    index = np.argmax(similarity, axis=-1, keepdims=False)

    return other[index[0]]
