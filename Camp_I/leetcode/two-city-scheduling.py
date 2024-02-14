class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        tot = 0
        nums = sorted(costs,key = lambda x:x[0]-x[1])
        for i in range(len(nums)):
            if i<len(nums)//2:
                tot+=nums[i][0]
            else:
                tot+=nums[i][1]
        return tot