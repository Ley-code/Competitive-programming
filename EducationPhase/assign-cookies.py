class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        r = len(s)-1
        l = len(g)-1
        count = 0
        while r>=0 and l>=0:
            if s[r] >= g[l]:
                count+=1
                r-=1
                l-=1
            else:
                l-=1
        return count