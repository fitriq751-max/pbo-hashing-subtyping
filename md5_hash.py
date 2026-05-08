import hashlib
from hash_algorithm import HashAlgorithm


# Subclass untuk algoritma MD5
class MD5Hash(HashAlgorithm):

    def __init__(self):
        super().__init__("MD5")

    def hash(self, text):
        return hashlib.md5(text.encode()).hexdigest()