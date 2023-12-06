class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        result = []
        while r<2*n:
            result.append(nums[l])
            result.append(nums[r])
            l+=1
            r+=1
        return result