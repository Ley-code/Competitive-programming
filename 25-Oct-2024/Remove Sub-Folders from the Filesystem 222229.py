# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False
    def add(self,path):
        curr = self
        for f in path.split("/"):
            if f not in curr.children:
                curr.children[f] = TrieNode()
            curr = curr.children[f]
        curr.isend = True
    def prefix_search(self,path):
        curr = self
        folders = path.split("/")
        for i in range(len(folders)-1):
            curr = curr.children[folders[i]]
            if curr.isend == True:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = TrieNode()
        for f in folder:
            trie.add(f)
        
        res = []
        for f in folder:
            if not trie.prefix_search(f):
                res.append(f)
        return res