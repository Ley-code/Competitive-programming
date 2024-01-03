class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        l = 0
        queue = deque()
        while l<len(bank):
            if bank[l].count("1") == 0:
                l+=1
                continue
            if queue:
                total += bank[l].count("1")*queue[0]
                queue.pop()
            queue.append(bank[l].count("1"))
            l+=1
        return total
        
