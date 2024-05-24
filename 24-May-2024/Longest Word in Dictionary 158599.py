# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        def insert(word):
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isend = True
        for word in words:
            insert(word)
        words = []
        def recurse(node,word):
            nonlocal words
            curr = node
            for c,child in curr.children.items():
                if child and child.isend:
                    recurse(child,word+c)
            words.append(word)
        recurse(root,"")
        words.sort(key = lambda x:len(x),reverse = True)
        length = len(words[0])
        l = 0
        while l<len(words):
            if len(words[l])==length:
                l+=1
            else:
                break
        res = words[:l]
        res.sort()
        return res[0]

