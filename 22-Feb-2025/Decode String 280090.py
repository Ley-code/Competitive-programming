# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        stack = []

        for c in s:
            curr = ""
            if c=="]":
                while stack and stack[-1]!="[":
                    curr = stack.pop() + curr
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(int(num)*curr)
            else:
                stack.append(c)
        return "".join(stack)