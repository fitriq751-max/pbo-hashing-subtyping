import hashlib
from hash_algorithm import HashAlgorithm


# Subclass untuk algoritma SHA1
class SHA1Hash(HashAlgorithm):

    def __init__(self):
        super().__init__("SHA1")

    def hash(self, text):
        return hashlib.sha1(text.encode()).hexdigest()