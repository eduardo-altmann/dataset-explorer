class Node:
    def __init__(self, key, value, next_node=None):     # construtor
        self.key = key
        self.value = value
        self.next = next_node

class HashTable:
    def __init__(self, size):           # construtor
        self.M = size
        self.buckets = [None] * size

    def _hash(self, key: int) -> int:
        return key % self.M             # função privada que faz o hash mod m

    def insert(self, key, value):
        index = self._hash(key)

        new_node = Node(key, value)

        new_node.next = self.buckets[index]
        self.buckets[index] = new_node

    def query(self, key):
        num_tests = 0
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            num_tests += 1
            if current.key == key:
                return current.value, num_tests
            current = current.next
        return None, num_tests
    
    def get(self, key):         # eh o query sem stats
        value, _ = self.query(key)
        return value

    def items(self):
        for head in self.buckets:
            current = head
            while current is not None:
                yield current.key, current.value
                current = current.next
