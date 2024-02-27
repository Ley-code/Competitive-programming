class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(subset,idx):
            ans.append(subset[:])
            for i in range(idx,n):
                subset.append(nums[i])
                backtrack(subset,i+1)
                subset.pop()
        backtrack([],0)
        return ans
