class Solution(object):
    def removeStars(self, s):
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)