class NumArray(object):

    def __init__(self, nums):
        self.prefixsum = []
        curr = 0
        for n in nums:
            curr+=n
            self.prefixsum.append(curr)

    def sumRange(self, left, right):
        rightsum = self.prefixsum[right]
        if left > 0:
            leftsum = self.prefixsum[left - 1 ]
        else:
            leftsum = 0
        return rightsum - leftsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)