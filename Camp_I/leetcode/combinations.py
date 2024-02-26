class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(nums,combination):
            if len(combination)==k:
                ans.append(combination)
                return
            if nums>n:
                return
            backtrack(nums+1,combination+[nums])
            backtrack(nums+1,combination)
            

        backtrack(1,[])
        return ans