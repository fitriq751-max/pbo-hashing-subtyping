from abc import ABC, abstractmethod


# Abstract class sebagai blueprint
# untuk semua algoritma hashing
class HashAlgorithm(ABC):

    def __init__(self, name):
        self.name = name

    # Method abstract yang wajib
    # diimplementasikan oleh subclass
    @abstractmethod
    def hash(self, text):
        pass