class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        maxlen = 0
        word = ""
        def recurse(left,right):
            nonlocal maxlen
            nonlocal word
            if left>right:
                return
            split = None
            seen = set(s[left:right+1])
            for i in range(left,right+1):
                if s[i].swapcase() not in seen:
                    split = i
                    break
            if split == None:
                if right-left>maxlen:
                    maxlen = right-left
                    word = s[left:right+1]
            else:
                recurse(left,split-1)
                recurse(split+1,right)
        recurse(0,len(s)-1)
        return word