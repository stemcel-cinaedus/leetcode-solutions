#I don't really understand this very well, probably was not a good choice for my first LL one

class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lkp = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        l, n = node.prev, node.next
        l.next, n.prev = n, l

    def insert(self, node):
        self.l, self.r = self.head, self.head.next
        self.l.next = self.r.prev = node
        node.prev, node.next = self.l, self.r 
    
    def get(self, key: int) -> int:
        if key in self.lkp:
            self.remove(self.lkp[key])
            self.insert(self.lkp[key])
            return self.lkp[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lkp:
            self.remove(self.lkp[key])
        self.lkp[key] = Node(key, value)
        self.insert(self.lkp[key])
        if len(self.lkp) > self.cap:
            last_used = self.tail.prev
            self.remove(last_used)
            del self.lkp[last_used.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
