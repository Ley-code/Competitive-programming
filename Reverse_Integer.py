class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))
        y = int(y[::-1])
        if abs(y)>2**31:
            return 0
        else:
            return y if x>0 else y*-1
