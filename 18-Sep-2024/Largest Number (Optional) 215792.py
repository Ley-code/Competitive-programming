# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for _ in range(len(nums)-1):
            for i in range(len(nums)-1):
                x = str(nums[i])
                y = str(nums[i+1])
                if x+y < y+x:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
        
        return str(int("".join(list(map(str,nums))))) 