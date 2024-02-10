class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n
        for i in range(n):
            l = i-1
            r = i+1
            while l>=0 and r<n and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            l = i
            r = i+1
            while l>=0 and r<n and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
        return count




           