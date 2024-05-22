# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        ispalindrome = [[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j-i<=2:
                        ispalindrome[i][j] = True
                    else:
                        ispalindrome[i][j] = ispalindrome[i+1][j-1]
        memo = {}
        def dp(st,end):
            if ispalindrome[st][end]:
                return 0
            if (st,end) in memo:
                return memo[(st,end)]
            mini = n-1 
            for i in range(st,end):
                if ispalindrome[st][i]:
                    mini = min(1+dp(i+1,end),mini)
            memo[(st,end)] = mini
            return memo[(st,end)]
        return dp(0,n-1)