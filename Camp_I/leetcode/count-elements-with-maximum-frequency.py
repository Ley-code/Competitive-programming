class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxfreq = 0
        mp = defaultdict(int)
        for num in nums:
            mp[num]+=1
            if mp[num]>maxfreq:
                maxfreq = mp[num]
        sums = 0
        for ele in mp:
            if mp[ele]==maxfreq:
                sums+=maxfreq
        return sums