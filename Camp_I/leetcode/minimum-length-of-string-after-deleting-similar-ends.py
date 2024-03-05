class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s)-1
        while l<r:
            while l<r and l>0 and s[l]==s[l-1]:
                l+=1
            while l<r and r<len(s)-1 and s[r]==s[r+1]:
                r-=1
            if s[l]!=s[r]:
                return r-l+1
            l+=1
            r-=1
        if l==r:
            return 1
        else:
            return 0
            