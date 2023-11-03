class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        for i in range(len(s)):
            if s[i]!=")":
                stack.append(s[i])
            else:
                reversedEle = []
                while stack[-1]!="(":
                    reversedEle.append(stack.pop())
                stack.pop()
                stack.extend(reversedEle)
        return "".join(stack)

        