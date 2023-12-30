class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hashmap = {}      
        for word in words:
            for c in word:
                hashmap[c] = hashmap.get(c, 0) + 1
        
        n = len(words)
        for val in hashmap.values():
            if val % n != 0:
                return False
        return True