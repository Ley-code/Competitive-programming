class Solution(object):
    def decodeString(self, s):
        stack = []

        for i in range(len(s)):
            encoded_string = ""
            
            if s[i]!="]":
                stack.append(s[i])
            else:
                while stack[-1] != "[":
                    encoded_string = stack.pop()+encoded_string
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num= stack.pop()+num
                encoded = int(num)*(encoded_string)
                stack.append(encoded)
            encoded_string = ""
            num = ""
        return "".join(stack)