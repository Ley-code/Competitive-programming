class Solution(object):
    import math
    def mySqrt(self, x):
        
        res = math.sqrt(x)
        return int(math.floor(res))
        