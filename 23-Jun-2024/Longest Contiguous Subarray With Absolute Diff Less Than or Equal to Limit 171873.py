# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decQ = collections.deque() 
        incQ = collections.deque() 
        ans = 0
        left = 0

        for right, num in enumerate(nums):
            while decQ and num > decQ[-1]:
                decQ.pop()

            decQ.append(num)

            while incQ and num < incQ[-1]:
                incQ.pop()

            incQ.append(num)

            while decQ[0] - incQ[0] > limit:
                if decQ[0] == nums[left]:
                    decQ.popleft()

                if incQ[0] == nums[left]:
                    incQ.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans