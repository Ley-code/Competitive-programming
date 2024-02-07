class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = Counter(s)
        value = list(hashmap.items())
        value.sort(key = lambda x:x[1],reverse = True)
        ans = ""
        for i in range(len(value)):
            ans+=value[i][0]*value[i][1]
        return ans

