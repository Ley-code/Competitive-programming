# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], id: int, vd: int) -> List[int]:
        if id>(len(nums)-1):
            return [-1,-1]
        for i in range(len(nums)):
            for j in range(i+id,len(nums)):
                if abs(nums[i]-nums[j])>=vd:
                    return [i,j]
        return [-1,-1]
