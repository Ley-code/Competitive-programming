class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(idx,comb,remaining):
            if len(comb)==k and remaining==0:
                ans.append(comb[:])
                return
            if len(comb)>k:
                return
            if remaining<0:
                return    
            for i in range(idx,10):    
                backtrack(i+1,comb+[i],remaining-i)
        backtrack(1,[],n)
        return ans