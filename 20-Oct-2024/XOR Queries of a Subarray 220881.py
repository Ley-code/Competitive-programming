# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        presum = [arr[0]]
        for i in range(1,len(arr)):
            presum.append(presum[-1]^arr[i])
        output = []
        for left,right in queries:
            if left>0:
                output.append(presum[right]^presum[left-1])
            else:
                output.append(presum[right])
        return output