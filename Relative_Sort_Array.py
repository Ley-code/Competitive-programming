class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        remaining = []
        arr1 = Counter(arr1)
        for i in arr2:
            res+=[i]*arr1[i]
        for num in arr1:
            if num not in arr2:
                remaining+=[num]*arr1[num]
        return res+sorted(remaining)