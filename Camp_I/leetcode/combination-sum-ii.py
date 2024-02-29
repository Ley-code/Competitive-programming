class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def backtrack(idx,combination,remaining):
            if remaining==0:
                ans.append(combination)
                return
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>remaining:
                    break
                backtrack(i+1,combination+[candidates[i]],remaining-candidates[i])
        candidates.sort()
        backtrack(0,[],target)
        return ans