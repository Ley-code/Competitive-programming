class Solution(object):
    def sumZero(self, n):
        ans = [None]*n
        if n%2 ==0:
            temp = n
        else:
            temp = n-1
            ans[n-1] = 0
        for i in range(0,temp,2):
            ans[i] = i+1
            ans[i+1] = -(i+1)
        return ans

