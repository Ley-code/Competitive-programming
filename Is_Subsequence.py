class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = r = 0
        if  s == "":
            return True
        while r<len(t) and l<len(s):
            if t[r] == s[l]:
                l+=1
                r+=1
            else:
                r+=1
        if l == len(s):
            return True
        return False