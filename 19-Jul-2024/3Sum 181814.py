# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                threesum = nums[l] + nums[r] + nums[i]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
            
        return ans
                