from collections import Counter


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) <3:
            return 0
        window = Counter(s[:2])
        l = 0
        count = 0
        for r in range(2,len(s)):
            window[s[r]] = window.get(s[r],0)+1
            if len(window) == 3:
                count+=1
            window[s[l]]-=1
            if window[s[l]]==0:
                del window[s[l]]
            l+=1
        return count