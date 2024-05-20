# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        num, prev, stack = 0, '+', []
        s = s+"+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
                print(num)
            elif c in "+-*/":
                if prev=='+':
                    stack.append(num)
                elif prev == '-':
                    stack.append(-num)
                elif prev == '*':
                    stack.append(stack.pop()*num)
                elif prev == '/':
                    stack.append(math.trunc(stack.pop()/num))
                prev=c
                num=0             
        return sum(stack)
                