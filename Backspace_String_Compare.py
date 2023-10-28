from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = deque()
        stack2 = deque()
        for letter in s:
            if letter!="#":
                stack1.append(letter)
            elif letter =="#" and stack1:
                stack1.pop()
        for letter in t:
            if letter!="#":
                stack2.append(letter)
            elif letter=="#" and stack2:
                stack2.pop()
        return "".join(stack1) == "".join(stack2)