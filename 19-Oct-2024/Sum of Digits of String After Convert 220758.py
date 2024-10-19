# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        tot = 0
        for c in s:
            for c in str(ord(c)-96):
                tot+=int(c)
        while k>1:
            curr = 0
            for c in str(tot):
                curr+= int(c)
            tot = curr
            k-=1
        return tot