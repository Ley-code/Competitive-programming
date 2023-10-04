class Solution(object):
    def isPalindrome(self, s):
        edited_string = ""
        for letter in s.upper():
            if (ord(letter)<91 and ord(letter)>64) or (ord(letter)>47 and ord(letter)<58):
                edited_string += letter
        print(edited_string)
        start_index = 0
        end_index = len(edited_string)-1
        while start_index < end_index:
            if edited_string[start_index] != edited_string[end_index]:
                return False
            start_index+=1
            end_index-=1
        return True