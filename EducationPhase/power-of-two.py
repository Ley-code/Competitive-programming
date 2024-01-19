class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        temp = n
        while temp>1:
            temp = temp/2
        if temp == 1.0:
            return True
        return False