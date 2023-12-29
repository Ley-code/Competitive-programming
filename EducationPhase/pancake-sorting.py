class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        def flip(idx):
            for i in range(0,idx//2+1):
                arr[i],arr[idx-i] = arr[idx-i],arr[i]
        l = len(arr)-1
        for i in range(len(arr)):
            maxi = max(arr[:l+1])
            idx = arr.index(maxi)
            ans.append(idx+1)
            flip(idx)
            ans.append(l+1)
            flip(l)
            l-=1
        return ans
