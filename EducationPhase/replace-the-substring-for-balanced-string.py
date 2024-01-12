class Solution:
    def balancedString(self, s: str) -> int:
        goal = len(s) // 4
        count = Counter(s)
        if max(count.values()) <= goal:
            return 0
        left = 0
        right = 0
        mini = float("inf")
        while right < len(s):
            while right < len(s) and max(count.values()) > goal:
                count[s[right]] -= 1
                right += 1
            while max(count.values()) <= goal:
                mini = min(mini,right-left)    
                count[s[left]] += 1
                left += 1
        return mini