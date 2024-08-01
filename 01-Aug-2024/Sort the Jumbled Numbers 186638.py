# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def transform(num):
            new = ""
            for digit in num:
                new += str(mapping[int(digit)])
            return int(new)
        hashmap = {num:transform(str(num)) for num in nums}
        nums.sort(key=lambda x:hashmap[x])
        return nums
        