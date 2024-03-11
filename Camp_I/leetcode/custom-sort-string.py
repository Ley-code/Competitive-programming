class Solution:
    def customSortString(self, order: str, s: str) -> str:
        seen = Counter(s)
        ans = ""
        for c in order:
            if c in seen:
                ans+= c*seen[c]
                del seen[c]
        for c in seen:
            ans+=c*seen[c]
        return ans

