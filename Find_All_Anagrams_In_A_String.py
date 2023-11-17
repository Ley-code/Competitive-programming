from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        res = []
        target = Counter(p)
        slidingwindow = Counter(s[:len(p)-1])
        l = 0
        for r in range(len(p)-1,len(s)):
            slidingwindow[s[r]]+=1
            if slidingwindow == target:
                res.append(l)
            slidingwindow[s[l]]-=1
            if slidingwindow[s[l]]==0:
                del slidingwindow[s[l]]
            l+=1
        return res