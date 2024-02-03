class Solution:
    def pivotInteger(self, n: int) -> int:
        rightSum = n * (n + 1) // 2
        leftsum = 0
        for i in range(1, n + 1):
            rightSum -= i
            if leftsum == rightSum:
                return i
            leftsum += i
        return -1