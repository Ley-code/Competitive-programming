class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsquares(num):
            sums = 0
            while num>0:
                digit = num%10
                sums += digit**2
                num //= 10
            return sums
        hashmap = {}
        while n!=1:
            n = sumofsquares(n)
            if n in hashmap:
                return False
            hashmap[n] = 1
        return True