class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [nums1[i]-nums2[i] for i in range(len(nums1))]
        count = 0
        def merge(left,right):
            n,m = len(left),len(right)
            nonlocal count
            # counting part
            l , r = 0 , 0
            while l<n:
                while r<m and right[r]+diff>=left[l]:
                    r+=1
                count+=r
                l+=1
            #sorting part
            merged = []
            l,r = 0,0
            while l<n and r<m:
                if left[l]>right[r]:
                    merged.append(left[l])
                    l+=1
                else:
                    merged.append(right[r])
                    r+=1    
            merged += left[l:]
            merged += right[r:]
            return merged
        def mergesort(l,r,arr):
            if l==r:
                return [arr[l]]
            mid = l + (r-l)//2
            left = mergesort(l,mid,arr)
            right = mergesort(mid+1,r,arr)
            return merge(left,right)
        mergesort(0,len(nums1)-1,arr)
        return count