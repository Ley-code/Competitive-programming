# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        fre = {0:0,1:0,2:0}
        for i in range(len(nums)):
            fre[nums[i]] +=1
        l = 0
        for r in range(len(nums)):
            while fre[l] == 0:
                l+=1
            nums[r] = l
            fre[l]-=1
        return