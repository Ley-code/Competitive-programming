class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxcount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
                if count>maxcount:
                    maxcount = count
            else:
                count=0
        return maxcount
            

        

