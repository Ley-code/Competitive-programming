class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hashmap = {}
        ans = ""
        for i in range(len(s)):
            hashmap[indices[i]] = s[i]
        for i in range(len(s)):
            ans+=hashmap[i]
        return ans