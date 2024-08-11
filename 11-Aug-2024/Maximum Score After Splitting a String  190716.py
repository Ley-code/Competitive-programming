# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        leftZeros = 0
        rightOnes = s.count("1")
        maxScore = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                leftZeros += 1
            else:
                rightOnes -= 1
            maxScore = max(maxScore,leftZeros+rightOnes)
        return maxScore