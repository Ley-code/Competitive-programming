class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char !=']':
                stack.append(char)
            else:
                string=""
                while stack[-1]!='[':
                    string=stack.pop()+string
                stack.pop()
                digit=""
                while stack and stack[-1].isdigit():
                    digit=stack.pop()+digit
                stack.append(string * int(digit))
        return "".join(stack)