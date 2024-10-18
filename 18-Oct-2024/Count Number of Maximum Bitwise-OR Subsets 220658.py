# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def backtrack(index,currOR,maxOR,count):
            if currOR==maxOR:
                count[0] += 1
            for i in range(index,len(nums)):
                backtrack(i+1,currOR | nums[i],maxOR,count)
        
        maxbit = nums[0] 

        for i in range(1,len(nums)):
            maxbit |= nums[i]

        count = [0]
        backtrack(0,0,maxbit,count)
        return count[0]

        