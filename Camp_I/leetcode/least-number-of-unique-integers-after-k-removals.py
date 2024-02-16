class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mp = Counter(arr)
        arr.sort(key = lambda x:(mp[x],x))
        print(arr)
        print(mp)
        for i in range(k):
            mp[arr[i]]-=1
            if mp[arr[i]]==0:
                del mp[arr[i]]
        return len(mp)
