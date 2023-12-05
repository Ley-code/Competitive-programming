class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandy = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxcandy:
                candies[i] = True
            else:
                candies[i] = False
        return candies