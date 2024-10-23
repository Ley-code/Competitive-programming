# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        r = 0
        for l in range(len(haystack)):
            i = l
            while r<len(needle) and i<len(haystack) and haystack[i]==needle[r]:                
                i+=1
                r+=1
            if r==len(needle):
                return l
            r = 0
        return -1