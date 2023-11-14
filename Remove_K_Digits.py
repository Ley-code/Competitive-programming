class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for i in range(len(num)):
            while stack and int(stack[-1])>int(num[i]) and k!=0:
                stack.pop()
                k-=1
            stack.append(num[i])
        while k!=0:
            stack.pop()
            k-=1 
        if not stack:
            return "0"
        return str(int("".join(stack)))
