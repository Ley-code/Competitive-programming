# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 
        length = len(nums1) + len(nums2)
        half = length //2
        if len(B)<len(A):
            A,B = B,A
        left,right = 0,len(A)-1
        while True:
            mid = left + (right-left)//2
            index = half-mid-2

            Aleft = A[mid] if mid>=0 else float('-inf')
            Bleft = B[index] if index>=0 else float('-inf')
            Aright = A[mid+1] if (mid+1)<len(A) else float('inf')
            Bright = B[index+1] if (index+1)<len(B) else float('inf')
            
            if Aleft<=Bright and Bleft<=Aright:
                if length%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft) + min(Aright,Bright))/2
            elif Aleft>Bright:
                right = mid-1
            else:
                left = mid + 1
