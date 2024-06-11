# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        rem = []
        arr1 = Counter(arr1)
        for i in arr2:
            res+=[i]*arr1[i]
        for num in arr1:
            if num not in arr2:
                rem+=[num]*arr1[num]
        return res+sorted(rem)