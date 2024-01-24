class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        value = set(nums)
        for i in range(1,len(nums)+1):
            if i not in value:
                res.append(i)
        return res