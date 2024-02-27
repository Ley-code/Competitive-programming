class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            denom = self.myPow(x,-n)
            return 1/denom
        if n == 0:
            return 1
        if n == 1:
            return x
        res = self.myPow(x,n//2)
        return res*res if n % 2 == 0 else res*res*x