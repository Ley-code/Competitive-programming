class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lettermap = {}
        l,total = 0,0
        longest = 0
        for r in range(len(s)):
            if s[r] in lettermap:
                lettermap[s[r]]+=1
            else:
                lettermap[s[r]] = 1
            total+=1
            while lettermap[s[r]] == 2:
                total-=1
                lettermap[s[l]] -=1
                l+=1
            longest = max(longest,r-l+1)
        return longest