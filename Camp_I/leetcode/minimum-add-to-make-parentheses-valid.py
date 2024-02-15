class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        extra = 0
        for c in s:
            if c =="(":
                opening+=1
            else:
                if opening:
                    opening-=1
                else:
                    extra+=1
        return opening+extra