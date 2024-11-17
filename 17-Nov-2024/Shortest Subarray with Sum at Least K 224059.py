# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float('inf')

        queue = deque() # (presum,index)
        cur_sum = 0

        for r in range(len(nums)):
            cur_sum += nums[r]
            if cur_sum >= k:
                res = min(res,r+1)
            while queue and cur_sum - queue[0][0]>=k:
                presum,end_index = queue.popleft()
                res = min(res, r - end_index)
            while queue and queue[-1][0] >= cur_sum:
                queue.pop()
            queue.append((cur_sum,r))

        return res if res!= float('inf') else -1