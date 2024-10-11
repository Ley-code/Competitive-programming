# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []
        def backtrack(opens,closed):
            if opens == closed == n:
                res.append("".join(stack))
                return
            if opens<n:
                stack.append("(")
                backtrack(opens+1,closed)
                stack.pop()
            if closed<opens:
                stack.append(")")
                backtrack(opens,closed+1)
                stack.pop()
        backtrack(0,0)
        return res
        