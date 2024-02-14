class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        pre = 0
        for i in range(len(nums)):
            while nums[i]>pre and nums[i]!=pre+1 and pre<n:
                temp = pre+1
                pre+=temp
                patch+=1
                print(i,pre)
            pre+=nums[i]
            if pre>=n:
                break
        while pre<n:
            temp = pre+1
            patch+=1
            pre+=temp
        return patch