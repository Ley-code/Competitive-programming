# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n)
        dp[-1] = questions[-1][0]
        
        for i in range(n-2,-1,-1):
            take = questions[i][0]
            skip = dp[i+1]
            if i+questions[i][1]+1<n:
                take += dp[i+questions[i][1]+1]
            dp[i] = max(skip,take)
        return dp[0] 