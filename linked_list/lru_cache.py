class Node:
    def __init__(self, next=None, prev=None,key=None, val=None):
        self.next = next
        self.prev = prev
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()
        # Technique to never access something None 
        # keep boundaries
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def _add_tail(self, node):
        last_node = self.tail.prev

        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_tail(node)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_tail(node)
            return
            
        if len(self.cache) == self.cap:
            lru = self.head.next
            del self.cache[lru.key]
            self._remove(lru)
            
        newNode = Node(key=key, val=value)
        self._add_tail(newNode)
        self.cache[key] = newNode

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
