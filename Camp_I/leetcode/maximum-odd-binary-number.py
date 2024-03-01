class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        ans = ""
        for i in range(len(s)-1):
            if ones>1:
                ans+="1"
                ones-=1
            else:
                ans+="0"
        ans+="1"
        return ans