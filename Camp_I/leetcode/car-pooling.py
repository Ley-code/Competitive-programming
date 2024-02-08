class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[2])
        length = trips[-1][2]
        values = [0]*(length+1)
        for trip in trips:
            people,start,end = trip
            values[end]-= people
            values[start] += people
        for i in range(len(values)):
            if i>0:
                values[i]+=values[i-1]
            if values[i]>capacity:
                return False
        return True
