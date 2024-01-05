class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = 0
        for ind, ele in enumerate(nums):
            max_len = 0
            for i in range(ind) :
                if nums[i]< ele:
                    max_len = max(max_len, count[i])
            max_len +=1
            count[ind] = max_len
            ans  = max(ans, max_len)
        return ans