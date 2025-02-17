# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited = set()
        ans = []
        for num in nums:
            if num in visited:
                ans.append(num)
            visited.add(num)
        return ans