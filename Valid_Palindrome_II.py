class Solution(object):
        def validPalindrome(self, s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return self.checkpalindrome(s, l + 1, r) or self.checkpalindrome(s, l, r - 1)
            return True     
        def checkpalindrome(self, s, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False    
            return True