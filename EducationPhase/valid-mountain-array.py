class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        else:
            idx = arr.index(max(arr))
            if idx == len(arr)-1 or idx==0:
                return False
            for i in range(idx):
                if arr[i] >= arr[i+1]:
                    return False
            for j in range(idx,len(arr)-1):
                if arr[j] <= arr[j+1]:
                    return False
            return True
            