class Solution(object):
    def reverseWords(self, s):
        result = ""
        reverse = s.split()[::-1]
        '''
        for i in range(len(reverse)):
            result+=reverse[i]
            if i == len(reverse)-1:
                break
            result+=' '
        '''
        return " ".join(reverse)
    
        