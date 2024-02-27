class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(combination, comb_sum, idx):
            if comb_sum==target:
                ans.append(combination[:])
                return
            if comb_sum>target:
                return
            for i in range(idx,len(candidates)):
                combination.append(candidates[i])
                backtrack(combination,comb_sum+candidates[i],i)
                combination.pop()

        backtrack([],0,0)
        return ans