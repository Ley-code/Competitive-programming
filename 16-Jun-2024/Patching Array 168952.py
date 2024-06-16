# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        p = 0
        for i in range(len(nums)):
            while nums[i]>p and nums[i]!=p+1 and p<n:
                temp = p+1
                p+=temp
                patch+=1
                print(i,p)
            p+=nums[i]
            if p>=n:
                break
        while p<n:
            temp = p+1
            patch+=1
            p+=temp
        return patch