class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j > 0:
                    matrix[i][j] += matrix[i][j-1]
        for k in range(len(matrix[0])):
        #for one iteration of column
            for i in range(k,len(matrix[0])):
                hashmap = {0:1}
                runningsum = 0
                for j in range(len(matrix)):
                    runningsum+= matrix[j][i] - (matrix[j][k-1] if k-1>=0 else 0)
                    if runningsum - target in hashmap:
                        count+=hashmap[runningsum-target]
                    hashmap[runningsum] = hashmap.get(runningsum,0)+1
        return count