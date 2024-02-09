class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinctele = len(set(nums))
        l = 0
        count = 0
        countmap = defaultdict(int)
        for r in range(len(nums)):
            countmap[nums[r]]+=1
            while len(countmap)==distinctele:
                countmap[nums[l]]-=1
                count+=len(nums)-r
                if countmap[nums[l]]==0:
                    del countmap[nums[l]]
                l+=1       
        return count

