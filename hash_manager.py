from hash_algorithm import HashAlgorithm


# Class manager untuk mengatur
# algoritma hashing yang digunakan
class HashManager:

    def __init__(self):
        self.algorithm = None

    # Method untuk memilih algoritma hashing
    def set_algorithm(self, algorithm: HashAlgorithm):
        self.algorithm = algorithm

    # Method untuk menghasilkan hash text
    def generate_hash(self, text):

        if self.algorithm is None:
            return "Algoritma hashing belum dipilih!"

        return self.algorithm.hash(text)