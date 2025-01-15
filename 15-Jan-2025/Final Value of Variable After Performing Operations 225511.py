# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        maps = {"--X":-1,"X++":1,"++X":1,"X--":-1}
        ans = 0
        for op in operations:
            ans += maps[op]
        return ans