class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}   # key -> node

        # Dummy nodes
        self.left = Node()   # LRU
        self.right = Node()  # MRU

        self.left.next = self.right
        self.right.prev = self.left

    # Remove node from linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert node at MRU position
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # Move accessed node to MRU
            self.remove(node)
            self.insert(node)

            return node.value

        return -1


    def put(self, key: int, value: int) -> None:

        # If key exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Capacity exceeded
        if len(self.cache) > self.capacity:
            # Remove LRU node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]