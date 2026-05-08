import hashlib
from hash_algorithm import HashAlgorithm


# Subclass untuk algoritma SHA512
class SHA512Hash(HashAlgorithm):

    def __init__(self):
        super().__init__("SHA512")

    def hash(self, text):
        return hashlib.sha512(text.encode()).hexdigest()