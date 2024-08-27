# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            leftPtr = i+1
            rightPtr = len(nums)-1
            while leftPtr<rightPtr:
                threesum = nums[leftPtr] + nums[rightPtr] + nums[i]
                if threesum>0:
                    rightPtr-=1
                elif threesum<0:
                    leftPtr+=1
                else:
                    ans.append([nums[i],nums[leftPtr],nums[rightPtr]])
                    leftPtr+=1
                    while leftPtr<rightPtr and nums[leftPtr]==nums[leftPtr-1]:
                        leftPtr+=1
            
        return ans
                