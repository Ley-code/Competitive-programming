class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        whole = len(arr)
        hashmap = {}
        for i in range(whole):
           hashmap[arr[i]] = hashmap.get(arr[i],0)+1
           if (hashmap[arr[i]]/whole) > 0.25:
               return arr[i]