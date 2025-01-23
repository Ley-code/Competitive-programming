# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = 0
        num = x
        while num!= 0:
            digit = num%10
            reversed = reversed*10 + digit
            num//=10
        return reversed == x
