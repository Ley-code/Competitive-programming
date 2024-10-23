# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(needle)
        M = len(haystack)
        mode = 26**N
        def encode(char):
            return ord(char) - ord("a")+1
        target = 0
        presum = 0

        for c in needle:
            target *= 26
            target += encode(c)
        
        for ind in range(M):
            presum *= 26
            presum %= mode
            presum += encode(haystack[ind])

            if presum == target:
                return ind-(N-1)
        return -1
