# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        directions = [(-1,0),(-1,-1),(-1,1)]
        def inbound(i,j):
            return 0<=i<n and 0<=j<n
        for row in range(n):
            for col in range(n):
                flag = False
                temp = matrix[row][col]
                for dr,dc in directions:
                    if inbound(row+dr,col+dc):
                        if flag:
                            matrix[row][col] = min(matrix[row][col],temp+matrix[row+dr][col+dc])
                        else:
                            matrix[row][col] += matrix[row+dr][col+dc] 
                        flag = True
        return min(matrix[-1])
        