class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(value):
            sums = 0
            for num in nums:
                sums += ceil(num/value)
            return sums
        low,high = 1,max(nums)
        print(check(5))
        while low<=high:
            mid = low + (high-low)//2
            if check(mid)<=threshold:
                high = mid-1
            else:
                low = mid+1
        return low