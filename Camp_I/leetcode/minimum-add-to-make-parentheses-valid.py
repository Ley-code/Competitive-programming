class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for par in s:
            if par == ")":
                if len(stack)!= 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(par)
            else:
                stack.append(par)
        return len(stack)