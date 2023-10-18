class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ss=sorted(nums)
        res=[]
        for i in nums:
            res.append(ss.index(i))
        return res
