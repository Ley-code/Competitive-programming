class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()[::-1]
        final = ""
        for i in range(len(res)):
            if i == len(res)-1:
                final+=res[i]    
            else:
                final+=res[i] + " "
        return final