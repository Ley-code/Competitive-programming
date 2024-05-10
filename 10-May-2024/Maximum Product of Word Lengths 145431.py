# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bi=[]
        n = len(words)
        for i in range(n):
            wordtobi=0
            for c in words[i]:
                wordtobi |= 1<<(ord(c)-97)
            bi.append(wordtobi)
        res=0
        for i in range(n):
            for j in range(i+1,n):
                if bi[i]&bi[j]==0:
                    res=max(res,len(words[i])*len(words[j]))
        return res