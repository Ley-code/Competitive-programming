class Solution(object):
    def numIdenticalPairs(self, nums):
        numcount = {}
        res = 0
        for num in nums:
            if num in numcount:
                res+=numcount[num]
                numcount[num]+=1
            else:
                numcount[num] = 1
        return res
