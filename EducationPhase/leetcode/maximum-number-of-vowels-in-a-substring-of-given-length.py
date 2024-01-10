class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxcount = 0
        vowels = set(["a","e","i","o","u"])
        for i in range(k-1):
            if s[i] in vowels:
                maxcount += 1
        r = k-1
        l = 0
        currcount = maxcount
        while r<len(s):
            if s[r] in vowels:
                currcount+=1
            maxcount = max(currcount,maxcount)
            if s[l] in vowels:
                currcount-=1
            l+=1
            r+=1
        return maxcount    