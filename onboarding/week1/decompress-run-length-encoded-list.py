class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        for i in range(0,len(nums)-1,2):
            decompressed.extend([nums[i+1]]*nums[i])
        return decompressed