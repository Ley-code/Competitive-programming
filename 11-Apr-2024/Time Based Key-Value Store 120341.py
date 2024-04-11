# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.dict = {}
        #key:[[timestamp][value]]
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key][0].append(timestamp)
            self.dict[key][1].append(value)
        else:
            self.dict[key] = [[timestamp],[value]]
    def get(self, key: str, timestamp: int) -> str:
        if key in self.dict:
            timestamps  = self.dict[key][0]
            left,right = 0,len(timestamps)-1
            while left<=right:
                mid = left+(right-left)//2
                if timestamps[mid]<=timestamp:
                    left = mid+1
                else:
                    right = mid-1
            if right>=0:
                return self.dict[key][1][right]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)