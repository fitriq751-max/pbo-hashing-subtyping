import hashlib
from hash_algorithm import HashAlgorithm


# Subclass untuk algoritma SHA256
class SHA256Hash(HashAlgorithm):

    def __init__(self):
        super().__init__("SHA256")

    def hash(self, text):
        return hashlib.sha256(text.encode()).hexdigest()