class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinctele = len(Counter(nums))
        l = 0
        count = 0
        countmap = defaultdict(int)
        for r in range(len(nums)):
            for j in range(r,len(nums)):
                countmap[nums[j]]+=1
                if len(countmap)==distinctele:
                    count+=1
            countmap = defaultdict(int)
            if countmap[nums[r]]==0:
                del countmap[nums[r]]
        return count

