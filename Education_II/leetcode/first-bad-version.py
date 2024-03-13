# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        leftmost  = None
        l , r = 1 , n
        while l<=r:
            mid = l + (r-l)//2
            if isBadVersion(mid) == False:
                leftmost = mid
                l = mid+1
            elif isBadVersion(mid) ==True:
                if leftmost:
                    if leftmost+1 == mid:
                        return mid
                r = mid-1
        if leftmost == None:
            return 1
        return leftmost+1

