# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        pos = 0
        ans = 0
        while pos<target or (pos-target)%2:
            ans+=1
            pos+=ans
        return ans