# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        matrix = []
        if m*n == len(original):
            for i in range(0,len(original),n):
                matrix.append(original[i:i+n])
        return matrix