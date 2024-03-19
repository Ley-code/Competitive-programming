class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            merged = []
            l = r = 0
            while l<len(left) and r<len(right):
                if left[l]<=right[r]:
                    merged.append(left[l])
                    l+=1
                else:
                    merged.append(right[r])
                    r+=1
            merged += left[l:]
            merged += right[r:]
            return merged
        def mergeSort(l,r,nums):
            if l==r:
                return [nums[l]]
            mid = l + (r-l)//2
            left = mergeSort(l,mid,nums)
            right = mergeSort(mid+1,r,nums)
            return merge(left,right)
        return mergeSort(0,len(nums)-1,nums)