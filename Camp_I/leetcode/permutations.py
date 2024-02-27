class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        mp = {}
        def backtrack(permutation, idx):
            nonlocal mp
            if len(permutation) == len(nums):
                ans.append(permutation[:])
                return
            for i in range(len(nums)):
                if nums[i] in mp:
                    continue
                permutation.append(nums[i])
                mp[nums[i]] = 0
                backtrack(permutation, i + 1)
                del mp[nums[i]]
                permutation.pop()

        backtrack([], 0)
        return ans
