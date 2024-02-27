class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        count = 0
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    count+=r-l
                    l+=1
                else:
                    r-=1
        return count


