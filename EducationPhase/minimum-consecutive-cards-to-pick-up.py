class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        minilen = float('inf')
        for i in range(len(cards)):
            if cards[i] in seen:
                minilen = min(i - seen[cards[i]]+1,minilen)
            seen[cards[i]] = i
        return minilen if minilen!=float('inf') else -1
