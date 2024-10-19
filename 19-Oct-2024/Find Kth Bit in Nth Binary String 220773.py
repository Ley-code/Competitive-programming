# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        if n==0:
            return "0"
        while n>1:
            suffix = list(s)
            for i in range(len(suffix)):
                if suffix[i]=="0": suffix[i] = "1"
                elif suffix[i]=="1": suffix[i] = "0"
            s = s + "1" + "".join(suffix[::-1])
            n-=1
        return s[k-1]