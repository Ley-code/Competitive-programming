# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        def gcd(len1,len2):
            if len2==0:
                return len1
            else:
                return gcd(len2,len1%len2)
        return str1[:gcd(len(str1),len(str2))]   
