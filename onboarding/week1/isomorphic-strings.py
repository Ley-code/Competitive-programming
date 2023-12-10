class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}
        l = 0
        length = len(s)
        if length != len(t):
            return False
        while l<len(s):
            if s[l] in hashmap:
                if t[l] != hashmap[s[l]]:
                    return False
            elif t[l] in hashmap2:
                if s[l] != hashmap2[t[l]]:
                    return False
            hashmap2[t[l]] = s[l]
            hashmap[s[l]] = t[l]
            l+=1
        return True