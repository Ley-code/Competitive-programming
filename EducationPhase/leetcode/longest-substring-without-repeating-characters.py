class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = l = 0
        HashMap = {}
        for r in range(len(s)):
            HashMap[s[r]] = HashMap.get(s[r],0)+1
            while HashMap[s[r]] == 2:
                HashMap[s[l]]-=1
                l+=1
            longest = max(longest,r-l+1)
        return longest