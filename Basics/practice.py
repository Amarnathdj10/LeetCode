class Node:

    def __init__(self, key, val):

        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self,capacity):

        self.capacity = capacity
        self.cache = {}

        left, right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):

        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv

    def insert(self, node):

        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev = prv
        node.next = nxt 

    def get(self, key):

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key, val):

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]