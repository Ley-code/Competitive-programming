class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        mp = {}
        for i,num in enumerate(intervals):
            mp[num[0]]=i
        intervals.sort()
        ans = [-1]*len(intervals)
        for i,interval in enumerate(intervals):
            l,r = i,len(intervals)-1
            while l<=r:
                mid = l + (r-l)//2
                if intervals[mid][0]<interval[1]:
                    l = mid+1
                else:
                    r = mid-1
            if l==len(intervals):
                continue
            ans[mp[interval[0]]] = mp[intervals[l][0]] 
        return ans
        
        