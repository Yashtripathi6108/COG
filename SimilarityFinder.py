from sentence_transformers import SentenceTransformer, util

class SimilarityFinder:

    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def calculate_embeddings(self, sentences):
        return self.model.encode(sentences, convert_to_tensor=True)

    def calculate_similarity(self, embeddings1, embeddings2):
        return util.cos_sim(embeddings1, embeddings2)