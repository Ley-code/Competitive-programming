class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        buckets = [None]*(len(nums)+1)
        ans = []
        for key in mp:
            if buckets[mp[key]] == None:
                buckets[mp[key]] = []
            buckets[mp[key]].append(key)
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i] == None:
                continue
            if len(ans)<k:
                ans+=buckets[i]
        return ans
        