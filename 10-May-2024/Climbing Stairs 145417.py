# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = {}
        def recurse(n):
            if n==1:
                return 1
            if n==0:
                return 1
            if n in hashmap:
                return hashmap[n]
            onestep = recurse(n-1)
            twostep = recurse(n-2)
            hashmap[n] = onestep+twostep
            return hashmap[n]
        return recurse(n)