# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        mincount = [float('inf')]*26
        for word in words:
            count = Counter(word)
            for i in range(26):
                c = chr(i+97)
                mincount[i] = min(mincount[i],count[c])
        res = []
        for i in range(26):
            if mincount[i]>0:
                res.extend([chr(i+97)]*mincount[i])
        return res

        