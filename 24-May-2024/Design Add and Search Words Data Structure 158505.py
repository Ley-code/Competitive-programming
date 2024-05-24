# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isend = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c)-97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isend = True
    def search(self, word: str) -> bool:
        def dfs(st,node):
            curr = node
            for i in range(st,len(word)):
                idx = ord(word[i])-97
                if word[i] == ".":
                    for child in curr.children:
                        if child:
                            if dfs(i+1,child):
                                return True
                    return False
                else:
                    if not curr.children[idx]:
                        return False
                    curr = curr.children[idx]
            return curr.isend
        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)