class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        result = []
        n = len(nums)
        for i in range(n):
            if nums[i]>0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        l = r = 0
        while l<n//2:
            result.append(positive[l])
            result.append(negative[r])
            l+=1
            r+=1
        return result