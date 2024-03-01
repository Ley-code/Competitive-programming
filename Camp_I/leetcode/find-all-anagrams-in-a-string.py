class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        target = Counter(p)
        sliding_window = Counter(s[:len(p)-1])
        r = len(p)-1
        l = 0
        while r<len(s):
            sliding_window[s[r]] = sliding_window.get(s[r],0)+1
            if sliding_window == target:
                res.append(l)
            sliding_window[s[l]]-=1
            if sliding_window[s[l]]==0:
                del sliding_window[s[l]]
            l+=1
            r+=1
        return res