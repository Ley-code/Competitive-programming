# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        min_value, max_value = min(bloomDay), max(bloomDay)
        answer = max_value

        while min_value <= max_value:
            mid = (min_value + max_value) // 2

            count, bouquets, adjacent = 0, 0, False
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    if count == 0:
                        adjacent = True
                        count += 1
                    elif adjacent:
                        count += 1
                else:
                    count = 0
                    adjacent = False
                
                if count == k:
                    bouquets += 1
                    count, adjacent = 0, False
                
            if bouquets >= m:
                answer = min(answer, mid)
                max_value = mid - 1
            else:
                min_value = mid + 1
        
        return answer
                

                