class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        sp = set(spaces)
        for i,c in enumerate(s):
            if i in sp:
                ans.append(" ")
            ans.append(c)
        return "".join(ans)