class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = s.count("1")
        zeros = len(s)-ones
        leftonesum = 0
        leftzerosum = 0
        res = 0
        for i in range(len(s)):
            if s[i]=="0":
                res+=leftonesum * (ones-leftonesum)
                leftzerosum+=1
            else:
                res+=leftzerosum * (zeros-leftzerosum)
                leftonesum+=1
        return res