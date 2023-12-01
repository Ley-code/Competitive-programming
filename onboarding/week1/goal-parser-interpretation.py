class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        stack = []
        for s in command:
            if s ==")": 
                if stack[-1] == "l":
                    string1 = stack.pop()
                    string2 = stack.pop()
                    stack.pop()
                    stack.append(string2)
                    stack.append(string1)
                else:
                    stack.pop()
                    stack.append("o")
            else:
                stack.append(s)
        return "".join(stack)