# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        record = []
        def backtrack(i,comb):
            if i==len(s):
                record.append("".join(comb[:]))
                return
            if s[i].isdigit():
                comb.append(s[i])
                backtrack(i+1,comb)
                comb.pop()
            else:
                comb.append(s[i].lower())
                backtrack(i+1,comb)
                comb.pop()
                comb.append(s[i].upper())
                backtrack(i+1,comb)
                comb.pop()
        backtrack(0,[])
        return record