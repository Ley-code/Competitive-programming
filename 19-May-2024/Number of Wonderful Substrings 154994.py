# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution(object):
    def wonderfulSubstrings(self, word):
        count = [0] * 1024  
        result = 0
        prefix_xor = 0
        count[prefix_xor] = 1
        
        for char in word:
            char_index = ord(char) - ord('a')
            prefix_xor ^= 1 << char_index
            result += count[prefix_xor]
            for i in range(10):
                result += count[prefix_xor ^ (1 << i)]
            count[prefix_xor] += 1
        
        return result
            