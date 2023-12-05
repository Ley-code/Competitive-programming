class Solution:  
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        def toint(num):
            ans = 0
            for i in num:
                ans = ans*10 +(ord(i) - ord('0'))
            return ans

        def tostring(string):
            newstring = ''
            while string:
                digits = string % 10
                string = string // 10
                newstring = chr(ord('0') + digits) + newstring
            return newstring
        
        return tostring(toint(num1)*toint(num2))