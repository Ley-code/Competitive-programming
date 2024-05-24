# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = defaultdict(int)
        def add(nums):
            val = bin(1<<33 | nums)[3:]
            curr = trie
            for bit in val:
                if bit not in curr:
                    curr[bit] = defaultdict(int)
                curr = curr[bit]
            curr["is_end"] = True
        def search(bitnum):
            curr = trie
            ans = ""
            for c in bitnum:
                if c=="0" and "1" in curr:
                    curr = curr["1"]
                    ans+="1"
                elif c=="1" and "0" in curr:
                    curr = curr["0"]
                    ans+="0"
                else:
                    curr = curr[c]
                    ans+=c
            return int(ans,2)
        for num in nums:
            add(num)
        maxor = 0
        for num in nums:
            val = bin(1<<33 | num)[3:]
            maxor = max(maxor,search(val)^num)
        return maxor