class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "#":
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(chr(int(f"{s[i-2]}{s[i-1]}")+96))
            else:
                stack.append(chr(int(s[i])+96))
        return "".join(stack)
