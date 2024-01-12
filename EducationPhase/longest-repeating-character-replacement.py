class Solution(object):
    def characterReplacement(self, s, k):
        l,r = 0,0
        longest,highestfrequencey = 0,0
        freqmap = {letter:0 for letter in s}
        while (r<len(s)):
            freqmap[s[r]]+= 1
            highestfrequencey = max(highestfrequencey, freqmap[s[r]])
            while (r-l+1) - highestfrequencey > k:
                freqmap[s[l]]-=1
                l+=1
            longest = max(longest,r-l+1)
            r+=1
        return longest
        