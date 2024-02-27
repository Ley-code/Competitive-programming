class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(permutation,idx):
            if len(permutation) == len(nums):
                ans.append(permutation[:])
                return
            for i in range(len(nums)):
                if nums[i] in permutation:
                    continue
                permutation.append(nums[i])
                backtrack(permutation,i+1)
                permutation.pop()
        backtrack([],0)
        return ans