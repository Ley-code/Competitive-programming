# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        record = []
        for ch in s:
            record.append([ch] if ch.isdigit() else [ch.lower(), ch.upper()])

        return [''.join(v) for v in product(*record)]