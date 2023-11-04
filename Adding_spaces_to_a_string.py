class Solution:
    def addSpaces(self, s, spaces):
        ans = []
        sp = set(spaces)
        for i,c in enumerate(s):
            if i in sp:
                ans.append(" ")
            ans.append(c)
        return "".join(ans)