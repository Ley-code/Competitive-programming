class Solution(object):
    def isPalindrome(self, s):
        edited_string = ""
        for letter in s.upper():
            if (ord(letter)<91 and ord(letter)>64) or (ord(letter)>47 and ord(letter)<58):
                edited_string += letter
        if edited_string == edited_string[::-1]:
            return True
        return False