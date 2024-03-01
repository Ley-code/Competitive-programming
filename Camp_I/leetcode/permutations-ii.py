class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans= []
        seen = set()
        n = len(nums)
        count = Counter(nums)
        def backtrack(perm):
            nonlocal count
            if len(perm)==n:
                ans.append(perm[:])
                return
            for i in count:
                if count[i]>0:
                    perm.append(i)
                    count[i]-=1
                    backtrack(perm)
                    count[i]+=1
                    perm.pop()
        backtrack([])
        return ans   