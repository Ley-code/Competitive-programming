class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = {0:0,1:0,2:0}
        for i in range(len(nums)):
            freq[nums[i]] +=1
        l = 0
        for r in range(len(nums)):
            while freq[l] == 0:
                l+=1
            nums[r] = l
            freq[l]-=1
        return