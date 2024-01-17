class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result = Counter(arr)
        value = list(result.values())
        value.sort()
        for i in range(1,len(value)):
            if value[i]==value[i-1]:
                return False
        return True
