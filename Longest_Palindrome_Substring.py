class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLength = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[r] == s[l]:
                if (r-l+1)>resultLength:
                    result = s[l:r+1]
                    resultLength = r-l+1
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r<len(s) and s[r] == s[l]:
                if (r-l+1)>resultLength:
                    result = s[l:r+1]
                    resultLength = r-l+1
                l-=1
                r+=1
        return result