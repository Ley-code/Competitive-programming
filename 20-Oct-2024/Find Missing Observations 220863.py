# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot = sum(rolls)
        m = len(rolls)
        missingsum = (n+m)*mean - tot
        if missingsum<1:
            return []
        value = missingsum//n
        if value>6 or value<1:
            return []
        arr = [value]*n
        remainder = missingsum%n
        for i in range(remainder):
            arr[i] += 1
            if arr[i]>6:
                return []
        return arr