class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        isprime = [True for i in range(n)]
        isprime[0] = isprime[1] = False
        i = 2
        while i*i<=n-1:
            if isprime[i]:
                j = 2 * i
                while j<=n-1:
                    isprime[j] = False
                    j+=i
            i+=1
        count = 0
        for val in isprime:
            if val:
                count+=1
        return count

        