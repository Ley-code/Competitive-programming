class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        sums = 0
        res = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                sums+=nums[i]
        for val,index in queries:
            if nums[index]%2==0:
                sums-=nums[index]
            nums[index] = nums[index]+val
            if nums[index]%2==0:
                sums+=nums[index]
                res.append(sums)
            else:
                res.append(sums)
        return res


        