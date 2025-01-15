# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        stack = []
        for c in address:
            if c==".":
                stack.append("[.]")
            else:
                stack.append(c)
        return "".join(stack)