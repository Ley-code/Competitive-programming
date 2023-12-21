class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col_idx in range(len(strs[0])):
            flag = True
            for row_idx in range(len(strs)-1):
                if ord(strs[row_idx][col_idx]) > ord(strs[row_idx+1][col_idx]):
                    flag = False
            if flag!=True:
                count+=1
        return count