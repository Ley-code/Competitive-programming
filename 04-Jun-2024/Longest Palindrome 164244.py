# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = Counter(s)
        length = 0
        flag = False
        for key in mp:
            if mp[key]%2!=0:
                length+=mp[key]-1
                flag = True
            else:
                length+=mp[key]
        if flag: 
            length+=1
        return length