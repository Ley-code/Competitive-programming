class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.extend([nums[i]])
        return nums