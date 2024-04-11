# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        l,r = 0,n-1
        while l<=r:
            mid = l + (r-l)//2
            if matrix[mid][0]>target:
                r = mid-1
            else:
                l = mid+1
        row = r
        l,r = 0,m-1
        while l<=r:
            mid = l+(r-l)//2
            if matrix[row][mid]<=target:
                l=mid+1
            else:
                r=mid-1
        if 0<=r<m and matrix[row][r]==target:
            return True
        return False