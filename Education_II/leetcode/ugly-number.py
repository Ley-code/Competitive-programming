class Solution:
    def isUgly(self, n: int) -> bool:
        arr = set()
        i = 2
        while i*i<=n:
            while n%i==0:
                arr.add(i)
                n//=i
            i+=1
        if n>1:
            arr.add(n)
        if not arr and n!=1: return False
        for ele in arr:
            if ele!= 2 and ele!= 3 and ele!= 5:
                return False
        return True