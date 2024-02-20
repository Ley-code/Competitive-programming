class Solution:
    def reverseString(self, s: List[str]) -> None:
        result = []
        def recurse(l,r):
            if l>=r:
                return
            s[l],s[r] = s[r],s[l]
            recurse(l+1,r-1)
            return
        recurse(0,len(s)-1)