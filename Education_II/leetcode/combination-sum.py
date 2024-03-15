class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def backtrack(comb,idx,sums):
            if sums==target:
                ans.append(comb[:])
                return
            if sums>target:
                return
            for i in range(idx,n):
                comb.append(candidates[i])
                backtrack(comb,i,sums+candidates[i])
                comb.pop()
        backtrack([],0,0)
        return ans