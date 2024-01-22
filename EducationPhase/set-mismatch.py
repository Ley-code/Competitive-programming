class Solution:
    def findErrorNums(self, nums):
        dup, missing = -1, -1
        value = Counter(nums)
        for i in range(1, len(nums) + 1):
            if i not in value:
                missing = i
            elif value[i]>1:
                dup = i
        return [dup, missing]

