# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self,key,val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key
class LRUCache:
    def __init__(self, capacity: int):
        self.cache =  {}
        self.capacity = capacity 
        self.LRU = Node(None,None)
        self.MRU = Node(None,None)
        self.LRU.next= self.MRU
        self.MRU.prev = self.LRU
        
    def remove(self,node):
        previousNode = node.prev
        nxt = node.next
        previousNode.next = nxt
        nxt.prev = previousNode

    def insert(self,node):
        prev,nxt = self.MRU.prev,self.MRU
        prev.next = nxt.prev = node
        node.prev,node.next = prev,nxt
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.capacity:
            lru = self.LRU.next
            self.remove(lru)
            del self.cache[lru.key]
        




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)